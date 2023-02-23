# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('pratica', pkey='id', name_long='Pratica', name_plural='Pratiche',caption_field='prat_num')
        self.sysFields(tbl)
        tbl.column('prat_num', dtype='N', name_long='Numero Pratica')