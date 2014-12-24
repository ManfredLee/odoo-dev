# -*- coding: utf-8 -*-

__author__ = 'MFY'
from openerp.osv import fields, osv
from openerp.addons.stock import stock_location as _stock_location


class stock_location(osv.osv):
    _inherit = "stock.location"

    _columns = {
        'complete_name': fields.function(_stock_location._complete_name, type='char', string="Location Name",
                                         store=False), }

    def update_name(self, cr, uid):
        ids = self.search(cr, uid, [])
        for id in ids:
            obj = self.browse(cr, uid, id)
            self.write(self, cr, uid, ids, {'name': obj.name})