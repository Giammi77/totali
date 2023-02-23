#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codekey')
        r.fieldcell('pratica_id')
        r.fieldcell('anno_mese')
        r.fieldcell('debito')

    def th_order(self):
        return 'codekey'

    def th_query(self):
        return dict(column='totale_anno_mese_caption', op='contains', val='')

    def th_top_custom(self,top):
        bar = top.slotToolbar('5,ricalcolo,5',childname='upper',_position='<bar')
        bar.ricalcolo.div().slotButton("Ricalcola",_tags='admin',fire='.ricalcola')
        bar.dataRpc(None,self.ricalcolaTotale,_fired='^.ricalcola',_lockScreen=True)

    @public_method
    def ricalcolaTotale(self,**kwargs):
        self.db.table('ttt.totale_anno_mese').totalize_realign_sql(empty=True)


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codekey' )
        fb.field('pratica_id' )
        fb.field('anno_mese' )
        fb.field('debito' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
