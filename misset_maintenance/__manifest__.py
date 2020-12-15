# -*- coding: utf-8 -*-
{
    'name': "misset_maintenance",

    'summary': """
        new menu called "Maintenance" ,
        in this menu we'd like a submenu with user defined filters,
        where all filters of other users should be visible, and deletable""",

    'description': """
        new menu called "Maintenance" Visible to group Beheer - Aanpassen Filters
    """,

    'author': "Magnus-Sify",
    'website': "http://www.magnus.nl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}