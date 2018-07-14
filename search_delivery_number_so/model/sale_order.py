# -*- coding: utf-8 -*-

from openerp import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_number = fields.Char("Delivery Number", copy=False)
