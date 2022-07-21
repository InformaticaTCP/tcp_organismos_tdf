# pylint: disable=missing-class-docstring
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TcpCargo(models.Model):

    # Listado de cargos de cargas organismo de TDF.
    
    _name = "tcp.cargo"
    _description = "Modelo TCP - Cargos de cada organismos y/o areas"

    
    name = fields.Char(string='Cargo', Required=True)
    active = fields.Boolean(string='Activo ?', default=True)
    
    # Relaciones entre Areas y cargos 
    area_id = fields.Many2one(
        comodel_name='tcp.area',
        string='Area',
        ondelete='restrict')

    organismo = fields.Many2one(
        comodel_name='tcp.organismo',
        string='Organismo')
    
    
#     @api.onchange('organismo')
#     def _onchange_organismo(self):
#         self.area_id = 0
#         if self.organismo:
#             # filter products by seller
#             product_ids = self.organismo.id
#             return {'domain': {'area_id': [('organismo_id', '=', product_ids)]}}
#         else:
#         # filter all products -> remove domain
#             return {'domain': {'area_id': []}}

#    # @api.onchange('reparticion_id')
#    # def onchange_reparticion_id(self):
#     #    for rec in self:
#     #        return {'domain':{'area_id':[('organismo_id', '=', 'rec.reparticion_id.id')]}}
   