# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        dev = root.branch(u"Develop")
        dev.packageBranch("System", pkg='sys')
        dev.packageBranch("Admin", pkg='adm')
        auto = root.branch(u"App")
        auto.thpage(u"!!Pratiche", table="ttt.pratica")
        auto.thpage(u"!!Evento", table="ttt.evento")
        auto.thpage(u"!!Contabile", table="ttt.contabile")
        auto.thpage(u"!!Totali Anno-Mese", table="ttt.totale_anno_mese")