# -*- coding: utf-8 -*-
{
    'name': "oecn_web_graph",

    'summary': """
        修正web_graph模块翻译问题""",

    'description': """
        修正web_graph模块翻译问题
    """,

    'author': "Manfred Lee(MFY)",
    'website': "https://github.com/ManfredLee",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web_graph'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'view/web_graph.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}