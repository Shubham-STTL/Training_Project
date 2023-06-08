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
    'depends': ['base', 'sale', 'sale_stock', 'sale_management'],
    'data': [
        'security/security_access.xml',
        'security/ir.model.access.csv',
        'wizard/prescription_wizard_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/hospital_view.xml',
        'views/patient_tags.xml',
        'views/sale_order_view.xml',
        'reports/patient_report.xml',
        ],
    'application': True,
    'installable': True,
    'auto_install' : False,
    'demo' : [],
    'license': 'LGPL-3',
    'assets' : {}
}
