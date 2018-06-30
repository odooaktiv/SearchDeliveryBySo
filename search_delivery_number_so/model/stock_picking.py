# -*- coding: utf-8 -*-

from odoo import api, fields, models


class stock_picking(models.Model):
    _inherit = 'stock.picking'

    sale_order_ids = fields.Many2many('sale.order', string='Sales Order\
        associated to this picking')

    """ Inherit method for get picking id and search origin in \
    sale order then get sale order id"""
    @api.model
    def create(self, vals):
        res = super(stock_picking, self).create(vals)
        if vals.get('origin'):
            Flag = True
            origin = vals.get('origin')
            while(Flag):
                sale = self.env['sale.order'].search(
                    [('name', 'ilike', origin)])
                if sale:
                    if sale.delivery_number:
                        delivery_number = sale.delivery_number
                        delivery_number += ',' + res.name
                        sale.delivery_number = delivery_number
                    else:
                        sale.delivery_number = res.name
                    Flag = False
                else:
                    existing_picking_id = self.search(
                        [('name', 'ilike', origin)])
                    if existing_picking_id:
                        origin = existing_picking_id.origin
                    else:
                        Flag = False
        return res
