# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Test module fof learning purposes""",

    'description': """
        Some description
    """,

    'author': "S.P.O.C",
    'website': "https://spoc.com.ua/",
    'license': "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'wizards/wizard_view.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/templates.xml',
        'data/data.xml',
        'reports/session_template.xml',
        'reports/session_report.xml',
        'views/dashboard.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
