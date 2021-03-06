# -*- coding: UTF-8 -*-

{
    'name': "TCP Lista de Organismos de Tierra del Fuego",
    'version': '0.1',
    'category': 'TCP',
    'summary': """
        Módulo para obtener un listado de Organismos de Tierra del Fuego
    """,
    'description': """
        Módulo para obtener un listado de Organismos de Tierra del Fuego
    """,
    'author': "Carlos Vargas -Informatica y Comunicaciones",
    'maintainer': "Informática y Comunicaciones",
    'website': "http://www.tcptdf.gob.ar",
    'license': 'LGPL-3',
    'depends': [
        'base'
        ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/tcp_organismo_view.xml',
        'views/tcp_area_view.xml',
        'views/tcp_cargo_view.xml'
       
    ],
    'application': True,
    'installable': True,
}
