# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TcpArea(models.Model):

    # Listado de areas de cada organismo de TDF.
    
    _name = "tcp.area"
    _description = "Modelo TCP - Datos de las Areas"

    name = fields.Char(string='Area', Required=True)
    letras = fields.Char(string='Iniciales', Required=True)
    codigo = fields.Integer(string='Código del Area')
    estado = fields.Selection(string='Activo ?', selection=[('si', 'SI'),('no', 'NO')])
    telefono = fields.Char(string='Teléfono')
    
    # Relaciones de tablas con Organismos
    organismo_id = fields.Many2one(string='Organismo', comodel_name='tcp.organismo', ondelete='restrict')
    cargo_ids = fields.Many2many(string='Cargos', comodel_name='tcp.cargo')

    # esto es de pruebas para ver si se pueden guardar los datos
     