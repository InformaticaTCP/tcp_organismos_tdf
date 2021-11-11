# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TcpCargo(models.Model):

    # Listado de cargos de cargas organismo de TDF.
    
    _name = "tcp.cargo"
    _description = "Modelo TCP - Cargos de cada organismos y/o areas"

    name = fields.Char(string='Cargo', Required=True)
    estado = fields.Selection(string='Activo ?', selection=[('si', 'SI'), ('no', 'NO')])
    
    # Relaciones entre Areas y cargos 
    area_id= fields.Many2one(string='Area', comodel_name='tcp.area', ondelete='restrict')