# -*- coding: utf-8 -*-
{
    'name': "oecn_module_translation_fix",

    'summary': """
        修正各个模块的翻译bug""",

    'description': """
已修正：
1，stock模块库位列表中库位名字显示的翻译问题
    """,

    'author': "Manfred Lee(MFY)",
    'website': "https://github.com/ManfredLee",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}