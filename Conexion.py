import sys
import pymysql

class Conector:
    def __init__(self, server='localhost',usuario='root', password=''
    ,basedato='plancuenta'):
         self.__server= server       #variables privadas
         self.__usuario= usuario
         self.__password= password
         self.__basedato= basedato
         self.__conn= ''          #permite realizar la conexion con la base de datos
         self.__conector= ''

    def conectar(self):
        try:
            self.__conn = pymysql.connect(              #el metodo connect realiza la conexion, enviandoles los parametros anteriores
                host=self.__server, user=self.__usuario, passwd=self.__password, 
                db=self.__basedato)
            self.__conector = self.__conn.cursor()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Error en la conexion", e)
            sys.exit(1)  #cerrar en caso de un problema

    def cerrar(self):
       self.__conn.close()
       self.__conector.close()

    @property
    def conector(self):
        return self.__conector

    @property
    def conn(self):
        return self.__conn


con = Conector () #llamando a la clase conector (los parametros son por defecto)
con.conectar()


