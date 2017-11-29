# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_number = fields.Char("Delivery Number")
