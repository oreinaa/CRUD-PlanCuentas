import sys
import pymysql

from Conexion import Conector


class DaoPlanC(Conector):   #Herencia conector(clase base)
    def __init__(self):
        super().__init__()  #Llamando al constructor de la clase base
    
    def consultar(self, buscar):
        result = False
        try:
            sql = "Select idplan, codigo, idgrupo, descripcion, naturaleza, estado from plancuenta where descripcion like '%" + \
                str(buscar) + "%' order by idplan"
            self.conectar()
            self.conector.execute(sql)   #conector para sentencias sql
            result = self.conector.fetchall()  #Fetchall.- devuelve la informacion en forma de lista
            self.conn.commit()  #Evalua si todo esta bien
        except Exception as e:
            print("Error en la consulta del Plan de cuentas", e)
            self.conn.rollback()  #Regresa al proceso anterior si algo esta mal
        finally:
            self.cerrar()
        return result 
    
    def ingresar(self, plan):
        correcto = True
        try:
            sql = "Insert into plancuenta (codigo, idgrupo, descripcion, naturaleza, estado) values (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql, (plan.codigo,plan.idgrupo,plan.descripcion,plan.naturaleza,plan.estado))    
            self.conn.commit()  
        except Exception as e:
            print("Error al ingresar el plan de cuentas", e)
            correcto = False
            self.conn.rollback()  
        finally:
            self.cerrar()
        return correcto 
    
    def modificar(self, plan):
        correcto = True
        try:
            sql = "Update plancuenta set codigo= %s,idgrupo= %s,descripcion= %s,naturaleza= %s,estado = %s where idplan = %s"
            self.conectar()
            self.conector.execute(sql, (plan.codigo,plan.idgrupo,plan.descripcion,plan.naturaleza,plan.estado, plan.idplan))     
            self.conn.commit()  
        except Exception as e:
            print("Error al modificar el plan de cuentas", e)
            correcto = False
            self.conn.rollback()  
        finally:
            self.cerrar()
        return correcto 
    
    def eliminar(self, plan):
        correcto = True
        try:
            sql = "Delete from plancuenta where idplan = %s"
            self.conectar()
            self.conector.execute(sql, (plan.idplan))     
            self.conn.commit()  
        except Exception as e:
            print("Error al eliminar el plan de cuentas", e)
            correcto = False
            self.conn.rollback()  
        finally:
            self.cerrar()
        return correcto 

""" con = DaoPlanC()
planes = con.consultar("")
print(planes)
for plan in planes:
    print(plan[2])  """

  
