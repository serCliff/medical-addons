from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import pdb


class PartnerRelatedFields(models.AbstractModel):
    _name = "chiropody.fields"
    _description = "Fields related with partner to be used on chiropody"

    active = fields.Boolean(default=True)
    partner_id = fields.Many2one("res.partner", "Partner", required=True)
    create_date = fields.Datetime(default=lambda self: fields.Datetime.now())
    company_id = fields.Many2one('res.company', string='Company', index=True,
                                 default=lambda self: self.env.user.company_id.id)

    # Partner related fields
    birth_date = fields.Date(related='partner_id.birth_date')
    gender = fields.Selection(related='partner_id.gender')
    civil_state = fields.Selection(related='partner_id.civil_state')
    allergies = fields.Char(related='partner_id.allergies')
    function = fields.Char(related='partner_id.function')
    style_of_life = fields.Char(related='partner_id.style_of_life')
    sport_practice = fields.Boolean(related='partner_id.sport_practice')
    sport_id = fields.Many2one(related='partner_id.sport_id')
    sport_periodicity = fields.Selection(related='partner_id.sport_periodicity')
    personal_history_id = fields.Many2many(related='partner_id.personal_history_id')
    familiar_history_id = fields.Many2many(related='partner_id.familiar_history_id')
    weight = fields.Float(related='partner_id.weight')
    height = fields.Float(related='partner_id.height')
    foot_size = fields.Float(related='partner_id.foot_size')
    foot_type = fields.Char(related='partner_id.foot_type')
    current_medication = fields.Char(related='partner_id.current_medication')


