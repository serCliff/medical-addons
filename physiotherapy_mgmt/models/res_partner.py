from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import pdb


class ResPartner(models.Model):
    _inherit = 'res.partner'

    treatment_ids = fields.One2many('partner.treatment', 'partner_id', "Treatments")
    treatment_count = fields.Integer(compute='count_treatments')
    treatment_history_ids = fields.One2many('treatment.history', 'partner_id', "Treatment Histories")
    physiotherapy_partner = fields.Boolean("Physiotherapy Partner", track_visibility='onchange')

    @api.model
    def create(self, values):
        self.check_physiotherapy(values)
        return super().create(values)

    @api.multi
    def write(self, values):
        self.check_physiotherapy(values)
        return super().write(values)

    def check_physiotherapy(self, values):
        """
        Method to mark what partners are physiotherapy patients also.
        """
        s1 = set(values.keys())
        # Get all physiotherapy fields and remove no needed standard fields
        treatment_fields = set(self.env['physiotherapy.fields'].fields_get().keys())
        s2 = treatment_fields.difference(['__last_update',
                                          'active',
                                          'id',
                                          'company_id',
                                          'create_date',
                                          'display_name',
                                          'function',
                                          'partner_id'])
        res = s1.intersection(s2)
        if res:
            values['physiotherapy_partner'] = True

    @api.multi
    def count_treatments(self):
        for self in self:
            if self.treatment_ids:
                self.treatment_count = len(self.treatment_ids.ids)

    @api.multi
    def action_make_treatment(self):
        action = self.env.ref('physiotherapy_mgmt.action_treatment_form').read()[0]
        action['context'] = {'search_default_partner_id': self.id}
        if len(self.treatment_ids) == 1:
            action['res_id'] = self.treatment_ids.id
            action['target'] = 'current'
            action['view_mode'] = 'form'
            del action['views']
        return action
