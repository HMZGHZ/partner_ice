from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ice = fields.Char(string='ICE')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ice = fields.Char(related='partner_id.ice', store=True)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    ice = fields.Char(related='partner_id.ice', store=True)


class AccountMove(models.Model):
    _inherit = 'account.move'

    ice = fields.Char(related='partner_id.ice', store=True)
