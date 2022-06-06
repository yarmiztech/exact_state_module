from odoo import fields,models,api
import logging


logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    extract_state = fields.Many2one('res.country.state')


