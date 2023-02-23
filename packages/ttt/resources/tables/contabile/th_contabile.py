#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('pratica_id')
        r.fieldcell('evento_id')
        r.fieldcell('debito')

    def th_order(self):
        return 'evento_id'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('pratica_id' )
        fb.field('evento_id' )
        fb.field('data_contabile' )
        fb.field('debito' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
