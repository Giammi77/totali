# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('contabile', pkey='id', name_long='Contabile', name_plural='Contabile',caption_field='data',
                    totalizer_totale_anno_mese='ttt.totale_anno_mese')
        self.sysFields(tbl)
        tbl.column('evento_id',size='22', group='_', name_long='Evento'
                    ).relation('ttt.evento.id', relation_name='contabile', mode='foreignkey', onDelete='raise')
        tbl.column('debito', dtype='N', name_long='Debito')
        tbl.aliasColumn('pratica_id','@evento_id.pratica_id', static=True)
        tbl.aliasColumn('data','@evento_id.data',static=True)
        tbl.aliasColumn('prat_num','@evento_id.prat_num')