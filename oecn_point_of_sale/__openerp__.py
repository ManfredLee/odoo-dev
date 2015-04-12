# -*- coding: utf-8 -*-
{
    'name': "oecn_point_of_sale",

    'summary': """
        修正小票打印宽度和打印内容。width的计算方式是width=有效打印宽度*打印密度 / 点阵字符宽度
		如：58mm的纸张，有效打印宽度=48mm，打印密度=8点/mm，点阵字符宽度=12点/字
		widht=48mm*8点/mm*12点/字=32字""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Manfred Lee(MFY)",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ]
}