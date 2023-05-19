# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# -*- coding: utf-8 -*-
{
    "name": "Hospital management TEST custom addon",
    "version": "15.0.1",
    "author": "Silver Touch Technologies Limited",
    'category': 'Hospital Management',
    'sequence': -100,
    "website": "https://www.silvertouch.com",
    "description": """TEST description of Hospital managements Team""",
    'depends': ['base'],
    'data': [
        'security/security_access.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/hospital_view.xml',
        'views/patient_tags.xml',
        ],
    'application': True,
    'installable': True,
    'auto_install' : False,
    'demo' : [],
    'license': 'LGPL-3',
    'assets' : {}
}
