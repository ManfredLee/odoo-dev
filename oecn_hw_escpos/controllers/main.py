# -*- coding: utf-8 -*-
__author__ = 'MFY'

import openerp.addons.hw_escpos.controllers.main as hw_escpos
try:
    from openerp.addons.hw_escpos import escpos
    from openerp.addons.hw_escpos.escpos import printer
    from openerp.addons.hw_escpos.escpos import supported_devices
except ImportError:
    escpos = printer = None

#class EscposDriver
def print_status(self, eprinter):
    return

_printer = None
# class EscposDriver
def get_escpos_printer(self):
    global _printer
    try:
        # self.set_status('connected','Connected to '+printers[0]['name'])
        if not _printer or _printer.device.closed:
            _printer = escpos.printer.Serial("COM3")
            self.set_status('connected','Connected to '+ "COM3")
        return _printer

        # else:
        #     self.set_status('disconnected','Printer Not Found')
        #     return None
    except Exception as e:
        self.set_status('error',str(e))
        return None


setattr(hw_escpos.EscposDriver, 'print_status', print_status)
setattr(hw_escpos.EscposDriver, 'get_escpos_printer', get_escpos_printer)


