# -*- coding: utf-8 -*-
__author__ = 'MFY'

try:
    from openerp.addons.hw_escpos import escpos
except ImportError:
    pass

# class Escpos
def text(self,txt):
    if not txt:
        return
    try:
        txt = txt.decode('utf-8')
    except:
        try:
            txt = txt.decode('utf-16')
        except:
            pass
    # self._raw('\x1C\x26')
    self._raw(txt.encode('gb18030'))
    return

setattr(escpos.escpos.Escpos, 'text', text)

def count_if(sequence, func):
    count = 0
    for v in sequence:
        if func(ord(v)):
            count += 1
    return count

def get_text_real_width(text):
    ascii_count = count_if(text, lambda v: v >= 0 and v < 256)
    return ascii_count + (len(text) - ascii_count) * 2

# class XmlLineSerializer
def _txt(self,txt):
    if self.left:
        if self.clwidth < self.lwidth:
            txt = txt[:max(0, self.lwidth - self.clwidth)]
            self.lbuffer += txt
            self.clwidth += get_text_real_width(txt)
    else:
        if self.crwidth < self.rwidth:
            txt = txt[:max(0, self.rwidth - self.crwidth)]
            self.rbuffer += txt
            self.crwidth += get_text_real_width(txt)

setattr(escpos.escpos.XmlLineSerializer, '_txt', _txt)

