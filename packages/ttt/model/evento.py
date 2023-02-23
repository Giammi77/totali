# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('evento', pkey='id', name_long='Evento', name_plural='Eventi',caption_field='caption_evento')
        self.sysFields(tbl)
        tbl.column('pratica_id',size='22', group='_', name_long='Pratica'
                    ).relation('ttt.pratica.id', relation_name='evento', mode='foreignkey', onDelete='raise')
        tbl.column('data', dtype='D', name_long='Data')
        tbl.aliasColumn('prat_num','@pratica_id.prat_num')
        tbl.formulaColumn('caption_evento',"$data||' - ' ||$prat_num", name_long='Evento')
