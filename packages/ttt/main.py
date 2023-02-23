#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='ttt package',sqlschema='ttt',sqlprefix=True,
                    name_short='Ttt', name_long='Ttt', name_full='Ttt')
                    
    def config_db(self, pkg):
        pass
    
    def custom_type_percent(self):
        return dict(dtype='N',format='##.00')
        
    def custom_type_money(self):
        return dict(dtype='N', format='#,##0.00')

    def custom_type_anno(self):
        return dict(dtype='N', format='#')

    def custom_type_intero(self):
        return dict(dtype='N', format='#') 

class Table(GnrDboTable):
    pass
