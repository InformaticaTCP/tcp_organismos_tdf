# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TcpOrganismo(models.Model):

    # Listado de organismos de TDF.
    
    _name = "tcp.organismo"
    _description = "Modelo TCP - Datos de los Organismos"

    name = fields.Char(string='Organismo' , Required=True)
    letras = fields.Char(string='Iniciales', Required=True)
    codigo = fields.Integer(string='Codigo del Organismo')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Telefono')
    correo = fields.Char(string='Correo Electrónico')
    delegacion = fields.Selection(string='Delegacion', selection=[('U', 'Ushuaia'), ('R', 'Río Grande'), ('T', 'Tolhuin')], Required=True)
    active = fields.Boolean(string='Activo ?', default = True )
    
    #relaciones entre tablas
    area_ids = fields.One2many(string='Areas', comodel_name='tcp.area', inverse_name='organismo_id' )
   

    # Funcion que permite mostrar campos concatenados
    def name_get(self):
        result = []
        for record in self:
            new_name = '%s - %s' % (record.name, record.delegacion)
            result.append((record.id, new_name))
        return result
