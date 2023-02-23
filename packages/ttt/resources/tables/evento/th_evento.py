#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('caption_evento')

    def th_order(self):
        return 'data'

    def th_query(self):
        return dict(column='id', op='contains', val='')

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('pratica_id' )
        fb.field('data' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
