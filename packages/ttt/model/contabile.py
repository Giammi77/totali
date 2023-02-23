# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('contabile', pkey='id', name_long='Contabile', name_plural='Contabile',caption_field='data',
                    totalizer_totale_anno_mese='ttt.totale_anno_mese')
        self.sysFields(tbl)
        tbl.column('evento_id',size='22', group='_', name_long='Evento'
                    ).relation('ttt.evento.id', relation_name='contabile', mode='foreignkey', onDelete='raise')
        tbl.column('debito', dtype='N', name_long='Debito')
        tbl.column('pratica_id',size='22', group='_', name_long='Pratica'
                    ).relation('ttt.pratica.id', relation_name='contabile', mode='foreignkey', onDelete='raise')
        tbl.column('data_contabile', dtype='D', name_long='Data Contabile')
        tbl.aliasColumn('prat_num','@evento_id.prat_num')