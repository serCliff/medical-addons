from odoo import fields, models, api, _
import pdb


class PartnerTreatment(models.Model):
    _name = 'chiropody.treatment'
    _inherit = ['chiropody.fields']
    _description = "Historical of some illness treatment. A treatment have some treatment.sessions"

    active = fields.Boolean(default=True)

    name = fields.Char("Name", required=True)
    observations = fields.Text("Observations", help="Duration? Origins? Influences?")

    chiropody_session_ids = fields.One2many("chiropody.session", "treatment_id", "Sessions")
    chiropody_sessions_count = fields.Integer(compute='count_chiropody_sessions')

    @api.multi
    def count_chiropody_sessions(self):
        if self.chiropody_session_ids:
            self.chiropody_sessions_count = len(self.chiropody_session_ids.ids)

    # @api.multi
    # def action_make_session(self):
    #     action = self.env.ref('physiotherapy_mgmt.action_treatment_history_form').read()[0]
    #     action['context'] = {'search_default_treatment_id': self.id}
    #     if len(self.treatment_history_ids) == 1:
    #         action['res_id'] = self.treatment_history_ids.id
    #         action['target'] = 'current'
    #         action['view_mode'] = 'form'
    #         del action['views']
    #     return action
