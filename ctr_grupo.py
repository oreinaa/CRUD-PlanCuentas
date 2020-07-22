from dao_grupo import DaoGrupo
from mod_grupo import modgrupo

class CtrGrupo:
    def __init__(self, gru=None):  #Significa que el dato del grupo esta vacio
        self.grupo = gru
    
    def consulta(self, buscar):
        objDaogrupo = DaoGrupo()
        return objDaogrupo.consultar(buscar)
    
    def ingresar(self, gru):
        objDaogrupo= DaoGrupo()
        return objDaogrupo.ingresar(gru)
    
    def modificar(self, gru):
        objDaogrupo= DaoGrupo()
        return objDaogrupo.modificar(gru)
    
    def eliminar(self, gru):
        objDaogrupo= DaoGrupo()
        return objDaogrupo.eliminar(gru)
    
""" gru = modgrupo(0,'Pasivo')
ctr = CtrGrupo()
#ingresar un grupo
ctr.ingresar(gru)
grupos = ctr.consulta("")
print(grupos)
for gru in grupos:
    print(gru[0], gru[1]) """