from odoo import fields, models, api


class TreatmentHistory(models.Model):
    _name = 'chiropody.session'
    _inherit = ['chiropody.fields']
    _description = "Each of sessions of a treatment"

    name = fields.Char("Name", required=True)
    observations = fields.Text("Observations", help="Duration? Origins? Influences?")

    treatment_id = fields.Many2one("chiropody.treatment", "Treatment")

    @api.onchange('treatment_id')
    def _onchange_treatment_id(self):
        if self.treatment_id:
            self.partner_id = self.treatment_id.partner_id


