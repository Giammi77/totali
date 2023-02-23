
# encoding: utf-8
from gnr.app.gnrdbo import TotalizeTable
from gnr.core.gnrbag import Bag
from datetime import date

class Table(TotalizeTable):
    def config_db(self,pkg):
        tbl = pkg.table('totale_anno_mese', pkey='codekey',pkey_columns='pratica_id,anno_mese',
                        name_long='!!Totale Anno Mese', name_plural='!!Totali Anno Mese',
                        caption_field='totale_anno_mese_caption',
                        totalize_maintable='ttt.contabile')
        self.sysFields(tbl,id=False, ins=False, upd=False, ldel=False,user_ins=False)
        tbl.column('codekey',name_long='key')
        tbl.column('pratica_id',size = '22', name_long = '!!Pratica',
                    totalize_key=True).relation('ttt.pratica.id', relation_name = 'totale_anno', mode = 'foreignkey')
        tbl.column('anno_mese', size=':7', name_long='Anno-Mese', totalize_key='*')

        tbl.column('debito', dtype = 'money' , name_long = '!![it]Debito',totalize_value=True)        
        tbl.formulaColumn('totale_anno_mese_caption',"@pratica_id.prat_num || ' - '|| $anno_mese")
        
    def totalize_key_anno_mese(self, contabile, **kwargs):
        dc=contabile.get('data_contabile')
        return '%s-%02i' %(dc.year,dc.month)


    def totalize_realign_sql(self,empty=False):
        if empty:
            self.empty()
            self.db.commit()
        if self.countRecords():
            return
        sql = """
            INSERT INTO ttt.ttt_totale_anno_mese (codekey,pratica_id,anno_mese,debito,"_refcount")
                (SELECT (SELECT pratica_id FROM evento  WHERE id=evento_id
               
                INNER JOIN ttt.ttt_evento  AS t1 ON t1.id = t0.evento_id

                GROUP BY t1.pratica_id, anno_mese;
            """


        _sql = """
            INSERT INTO ttt.ttt_totale_anno_mese (codekey,pratica_id,anno_mese,debito,"_refcount")
                (SELECT pratica_id||'_'||to_char((SELECT t2.data FROM ttt.ttt_evento AS t2 WHERE t2.id=t0.evento_id),'YYYY-MM'),
                pratica_id,
                to_char((SELECT t3.data FROM ttt.ttt_evento AS t3 WHERE t3.id=t0.evento_id),'YYYY-MM') AS anno_mese,
                SUM(debito),
                count(*)
                FROM ttt.ttt_contabile AS t0
                INNER JOIN ttt.ttt_evento  AS t1 ON t1.id = t0.evento_id
                GROUP BY t1.pratica_id, anno_mese;
            """




        self.db.execute(sql)
        self.db.commit()
        


    # def defaultValues(self):
    #         return dict(cliente_id=self.db.currentEnv.get('current_cliente_id'), data=self.db.workdate)

        # cliente_id=self.db.currentEnv.get('current_cliente_id')
        # _sql = """
        #     INSERT INTO  rcweb.rcweb_conto_residuo (codekey,pratica_anag_id,debito,credito,"_refcount",cliente_id)
        #     (SELECT 
        #         t1.pratica_anag_id,
        #         t1.pratica_anag_id,
        #         COALESCE(sum(debito),0),
        #         COALESCE(sum(credito),0),
        #         count(*),
        #         (SELECT 
        #             t2.cliente_id as clinete_id
        #          FROM
        #             rcweb.rcweb_pratica_anag as t2 
        #          WHERE
        #             t2.id = t1.pratica_anag_id)
        #     FROM  rcweb.rcweb_contabile AS t0
        #         INNER JOIN rcweb.rcweb_evento  AS t1 ON t1.id = t0.evento_id
        #     GROUP BY t1.pratica_anag_id)
        #     """:w