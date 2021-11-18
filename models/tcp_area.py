# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TcpArea(models.Model):

    # Listado de areas de cada organismo de TDF.
    
    _name = "tcp.area"
    _description = "Modelo TCP - Datos de las Areas"

    name = fields.Char(string='Area', Required=True)
    letras = fields.Char(string='Iniciales', Required=True)
    codigo = fields.Integer(string='Código del Area')
    telefono = fields.Char(string='Teléfono')
    active = fields.Boolean(string='Activo ?', default = True )
    
    # Relaciones de tablas con Organismos
    organismo_id = fields.Many2one(string='Organismo', comodel_name='tcp.organismo', ondelete='restrict')
    cargo_ids = fields.One2many(string='Cargo', comodel_name='tcp.cargo', inverse_name='area_id', ondelete='restrict')

    