# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TcpArea(models.Model):

    # Listado de areas de cada organismo de TDF.
    
    _name = "tcp.area"
    _description = "Modelo TCP - Datos de las Areas"

    name = fields.Char(string='Area', required=True)
    delegacion = fields.Selection(string='Delegacion', selection=[('U', 'Ushuaia'), ('R', 'Río Grande'), ('T', 'Tolhuin'), ('BS', 'Buenos Aires')], required=True)
    letras = fields.Char(string='Iniciales', required=True)
    codigo = fields.Integer(string='Código del Area')
    telefono = fields.Char(string='Teléfono')
    active = fields.Boolean(string='Activo ?', default = True )
    
    # Relaciones de tablas con Organismos
    organismo_id = fields.Many2one(
        comodel_name='tcp.organismo',
        string='Organismo',
        ondelete='restrict')

    cargo_ids = fields.One2many(
        comodel_name='tcp.cargo',
        string='Cargo',
        inverse_name='area_id',
        ondelete='restrict')
