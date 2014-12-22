# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

from openerp import tools
import openerp.modules
from openerp.osv import fields, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class ir_translation(osv.osv):
    _inherit = "ir.translation"

    @tools.ormcache(skiparg=3)
    def _get_source(self, cr, uid, name, types, lang, source=None, res_id=None):
        """
        Returns the translation for the given combination of name, type, language
        and source. All values passed to this method should be unicode (not byte strings),
        especially ``source``.

        :param name: identification of the term to translate, such as field name (optional if source is passed)
        :param types: single string defining type of term to translate (see ``type`` field on ir.translation), or sequence of allowed types (strings)
        :param lang: language code of the desired translation
        :param source: optional source term to translate (should be unicode)
        :param res_id: optional resource id to translate (if used, ``source`` should be set)
        :rtype: unicode
        :return: the request translation, or an empty unicode string if no translation was
                 found and `source` was not passed
        """
        # FIXME: should assert that `source` is unicode and fix all callers to always pass unicode
        # so we can remove the string encoding/decoding.
        if not lang:
            return tools.ustr(source or '')
        if isinstance(types, basestring):
            types = (types,)
        # if source :
        #     str = ','.join([name, source])
        #     str1 = ','.join(list(types))
        #     _logger.info(','.join([str, str1]))

        query, params = self._get_source_query(cr, uid, name, types, lang, source, res_id)

        cr.execute(query, params)
        res = cr.fetchone()
        trad = res and res[0] or u''

        if trad:
            return trad

        if set(types) & set(['view', 'sql_constraint', 'xsl', 'constraint']):#model
            if name in self.pool:
                cls_ins = self.pool[name]
                if hasattr(cls_ins, '_name') and hasattr(cls_ins, '_inherit'):
                    inherit = cls_ins._inherit[0] if isinstance(cls_ins._inherit, (list,)) and cls_ins._inherit else cls_ins._inherit
                    if cls_ins._name != inherit:
                        trad = self._get_source(cr, uid, inherit, types, lang, source=source, res_id=res_id)
                        if trad:
                            return trad

                if hasattr(cls_ins, '_inherits'):
                    for parent in cls_ins._inherits.iterkeys():
                        trad = self._get_source(cr, uid, parent, types, lang, source=source, res_id=res_id)
                        if trad:
                            return trad

        elif set(types) & set(['field', 'selection', 'help', 'model', 'help', 'selection']):#(model, field)
            model, value = name.split(',')
            if model in self.pool:
                cls_ins = self.pool[model]
                if hasattr(cls_ins, '_name') and hasattr(cls_ins, '_inherit'):
                    inherit = cls_ins._inherit[0] if isinstance(cls_ins._inherit, (list,)) and cls_ins._inherit else cls_ins._inherit
                    if cls_ins._name != inherit:
                        name='%s,%s' %(inherit, value)
                        trad = self._get_source(cr, uid, name, types, lang, source=source, res_id=res_id)
                        if trad:
                            return trad

                if hasattr(cls_ins, '_inherits'):
                    for parent in cls_ins._inherits.iterkeys():
                        name='%s,%s' %(parent, value)
                        trad = self._get_source(cr, uid, name, types, lang, source=source, res_id=res_id)
                        if trad:
                            return trad

        # elif type in ['sql_constraint', 'xsl', 'constraint']:#model
        #     if name in self.pool:
        #         cls_ins = self.pool[name]
        #         if cls_ins._name != cls_ins._inherit:
        #             trad = self._get_source(cr, uid, cls_ins._inherit, types, lang, source=source, res_id=res_id)
        #             if trad:
        #                 return trad
        #
        #         for parent in cls_ins._inherits.iterkeys():
        #             trad = self._get_source(cr, uid, parent, types, lang, source=source, res_id=res_id)
        #             if trad:
        #                 return trad
        #     return None

        if source:
            trad = tools.ustr(source)

        return trad

class ir_filters(osv.osv):
    _inherit = 'ir.filters'

    def get_filters(self, cr, uid, model, action_id=None):
        my_filters = super(ir_filters, self).get_filters(cr, uid, model, action_id=action_id)

        if model and my_filters:
            for filter in my_filters:
                if 'name' not in filter:
                    continue
                lang = self.pool.get('res.users').browse(cr, uid, uid)
                if lang:
                    lang = lang.partner_id.lang
                    filter['name'] = self.pool['ir.translation']._get_source(cr, uid, 'ir.filters,name', 'model', lang, source=filter['name'])

        return my_filters