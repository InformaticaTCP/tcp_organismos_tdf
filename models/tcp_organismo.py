# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TcpOrganismo(models.Model):

    # Listado de organismos de TDF.
    
    _name = "tcp.organismo"
    _description = "Modelo TCP - Datos de los Organismos"

    name = fields.Char(string='Organismo' , Required=True)
    letras = fields.Char(string='Iniciales', Required=True)
    codigo = fields.Integer(string='Codigo del Organismo')
    estado = fields.Selection(string='Activo ?', selection=[('si', 'SI'),('no', 'NO')])
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Telefono')
    correo = fields.Char(string='Correo Electrónico')
    delegacion = fields.Selection(string='Delegacion', selection=[('U', 'Ushuaia'), ('R', 'Río Grande'), ('T', 'Tolhuin')], Required=True)
    
    #relaciones entre tablas
    area_ids = fields.One2many(string='Areas', comodel_name='tcp.area', inverse_name='organismo_id' )
   
