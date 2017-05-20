# -*- coding: utf-8 -*-
{
    'name': "Tiny ERP",

    'summary': """
    Tiny ERP Project
        """,

    'description': """
        Tiny ERP Project
    """,

    'author': "Leantic",
    'website': "http://www.leantic.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Other',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['l10n_py', 'l10n_py_toponyms', 'stock', 'sale'],

    # always loaded
    'data': [
        'views/sale_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'auto_install': False,

}
