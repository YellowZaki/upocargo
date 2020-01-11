# -*- coding: utf-8 -*-
{
    'name': "upocargo",

    'summary': "Gestion de mudanzas",

    'description': "Crear mudanzas, administrar clientes...",

    'author': "UPO",
    'website': "http://www.upo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/upocargoservicio_view.xml',
        'views/upocargomudanza_view.xml',
        'views/upocargoguardamueble_view.xml',
        'views/upocargocliente_view.xml',
        'views/upocargobien_view.xml',
        'views/upocargotransporte_view.xml',
        'views/upocargoalmacen_view.xml',
        'views/upocargofactura_view.xml',
        'views/upocargoempleado_view.xml'
        
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml'],
    'application': True,
}
