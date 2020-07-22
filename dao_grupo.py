import sys
import pymysql

from Conexion import Conector

class DaoGrupo(Conector):   #Herencia conector(clase base)
    def __init__(self):
        super().__init__()  #Llamando al constructor de la clase base

    def consultar(self, buscar):
        result = False
        try:
            sql = "Select idgrupo, descripcion from grupo where descripcion like '%" + \
                str(buscar) + "%' order by idgrupo"
            self.conectar()
            self.conector.execute(sql)   #conector para sentencias sql
            result = self.conector.fetchall()  #Fetchall.- devuelve la informacion en forma de lista
            self.conn.commit()  #Evalua si todo esta bien
        except Exception as e:
            print("Error en la consulta de grupo", e)
            self.conn.rollback()  #Regresa al proceso anterior si algo esta mal
        finally:
            self.cerrar()
        return result 
    
    def ingresar(self, gru):
        correcto = True
        try:
            sql = "Insert into grupo (descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql, (gru.descripcion))    
            self.conn.commit()  
        except Exception as e:
            print("Error al ingresar el grupo", e)
            correcto = False
            self.conn.rollback()  
        finally:
            self.cerrar()
        return correcto 
    
    def modificar(self, gru):
        correcto = True
        try:
            sql = "Update grupo set descripcion = %s where idgrupo = %s"
            self.conectar()
            self.conector.execute(sql, (gru.descripcion, gru.idgrupo))     
            self.conn.commit()  
        except Exception as e:
            print("Error al modificar el grupo", e)
            correcto = False
            self.conn.rollback()  
        finally:
            self.cerrar()
        return correcto 
    
    def eliminar(self, gru):
        correcto = True
        try:
            sql = "Delete from grupo where idgrupo = %s"
            self.conectar()
            self.conector.execute(sql, (gru.idgrupo))     
            self.conn.commit()  
        except Exception as e:
            print("Error al eliminar el grupo", e)
            correcto = False
            self.conn.rollback()  
        finally:
            self.cerrar()
        return correcto 

""" con = DaoGrupo()
grupos = con.consultar("")
print(grupos)
for gru in grupos:
    print(gru[1]) """
