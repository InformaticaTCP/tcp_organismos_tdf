# -*- coding: utf-8 -*-

from odoo import models, fields

class TcpOrganismo(models.Model):

    # Listado de organismos de TDF.
    
    _name = "tcp.organismo"
    _description = "Modelo TCP - Datos de los Organismos"

    name = fields.Char(string='Organismo' , required=True)
    letras = fields.Char(string='Iniciales', required=True)
    codigo = fields.Integer(string='Codigo del Organismo')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Telefono')
    correo = fields.Char(string='Correo Electrónico')
    active = fields.Boolean(string='Activo ?', default = True )
    
    #relaciones entre tablas
    area_ids = fields.One2many(
        comodel_name='tcp.area',
        string='Areas',
        inverse_name='organismo_id' )
   

  