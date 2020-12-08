from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import pdb


class ResPartner(models.Model):
    _inherit = 'res.partner'

    foot_size = fields.Float('Foot size')
    foot_type = fields.Char('Foot type')
    chiropody_partner = fields.Boolean("Podiastry Partner", track_visibility='onchange')

    chiro_treatment_ids = fields.One2many('chiropody.treatment', 'partner_id', "Chiropody treatments")
    chiro_treatment_count = fields.Integer(compute='count_chiro_treatments')
    # chiro_treatment_history_ids = fields.One2many('treatment.history', 'partner_id', "Treatment Histories")

    @api.model
    def create(self, values):
        self.check_podiastry(values)
        return super().create(values)

    @api.multi
    def write(self, values):
        self.check_podiastry(values)
        return super().write(values)

    def check_podiastry(self, values):
        """
        Method to mark what partners are chiropody patients also.
        """
        s1 = set(values.keys())
        # Get all chiropody fields and remove no needed standard fields
        treatment_fields = set(['foot_size','foot_type'])
        res = s1.intersection(treatment_fields)
        if res:
            values['chiropody_partner'] = True

    @api.multi
    def count_chiro_treatments(self):
        for p_id in self:
            if p_id.chiro_treatment_ids:
                p_id.chiro_treatment_count = len(p_id.chiro_treatment_ids.ids)

    @api.multi
    def action_make_chiropody_treatment(self):
        action = self.env.ref('chiropody_mgmt.action_treatment_form').read()[0]
        action['context'] = {'search_default_partner_id': self.id}
        if len(self.chiro_treatment_ids) == 1:
            action['res_id'] = self.chiro_treatment_ids.id
            action['target'] = 'current'
            action['view_mode'] = 'form'
            del action['views']
        return action
