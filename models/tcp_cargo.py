# pylint: disable=missing-class-docstring
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TcpCargo(models.Model):

    # Listado de cargos de cargas organismo de TDF.
    
    _name = "tcp.cargo"
    _description = "Modelo TCP - Cargos de cada organismos y/o areas"

    name = fields.Char(string='Cargo', Required=True)
    active = fields.Boolean(string='Activo ?', default=True)
    nombre_organismo = fields.Char(related='area_id.organismo_id.name', string='Organismo') 
    # Relaciones entre Areas y cargos 
    area_id = fields.Many2one(string='Area', comodel_name='tcp.area', ondelete='restrict')
    organismo = fields.Many2one(string='Organismo', related=('area_id.organismo_id'))