# -*- coding: utf-8 -*-
{
    'name': "oecn_hw_escpos",

    'summary': """
        pos打印模块修改""",

    'description': """
        修改小票打印中文时出现乱码和行宽度问题。官方默认是usb连接方式，因为国内没有找到兼容的usb小票打印机,智能使用串口打印机测试。代码硬编码使用COM3，请自行修改。
		如果使用官方默认的，请把代码注释掉。
    """,

    'author': "Manfred Lee(MFY)",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hw_escpos'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}