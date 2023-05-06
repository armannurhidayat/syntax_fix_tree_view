# -*- coding: utf-8 -*-
{
    'name': "syntax_fix_tree_view",

    'summary': """
        Fix Header tree view""",

    'description': """
        Fix Header tree view
    """,

    'author': "armannurhidayat7@gmail.com",
    'website': "http://www.armannurhidayat.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
}