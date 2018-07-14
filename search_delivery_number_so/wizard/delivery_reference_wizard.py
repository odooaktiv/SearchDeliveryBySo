# -*- coding: utf-8 -*-

from openerp import api, models


class DeliveryReferenceSale(models.TransientModel):
    _name = 'delivery.reference.sale'

    @api.multi
    def add_delivery_refrence_in_so(self):
        sale_id = self.env['sale.order'].search([])
        for sale in sale_id:
            if not sale.delivery_number:
                picking_list = [picking_id.name for picking_id
                                in sale.picking_ids if picking_id]
                for picking in picking_list:
                    if sale.delivery_number:
                        delivery_number = sale.delivery_number
                        delivery_number += ',' + picking
                        sale.delivery_number = delivery_number
                    else:
                        sale.delivery_number = picking
