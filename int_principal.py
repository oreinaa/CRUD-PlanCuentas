from ctr_grupo import CtrGrupo
from mod_grupo import modgrupo
from ctr_planc import CtrPlanc
from mod_PlanC import planC
from Funciones import menugrupo
from Funciones import menuplan
from Funciones import menu
import os 

ctrgr = CtrGrupo()

def ingresargr(rango):  #Dependera del numero que se desea ingresar
    for i in range(int(rango)):
        while True:
            try:
                descripcion = input('Ingrese la descripcion: ')
            except ValueError:
                continue
            if not(descripcion.isalpha()):
                  print("Escribir nuevamente, solo se admiten letras")
                  continue
            else:
                break

        gru = modgrupo(des=descripcion)
        respuesta = input(f"Deseas guardar el grupo:  {descripcion}[s/n]:")
        if not respuesta or respuesta[0].lower() != 's':
            input('Presione una tecla para continuar')
            ejecutar_grupo()
        else:
            if ctrgr.ingresar(gru):  #Proceso de validacion con la variable "correcto" (booleano)
                print("Registro ingresado correctamente")
            else:
                print('Error al ingresar el registro')
           
def modificargr():  
    while True:
            try:
                codigo = int(input('Ingrese el codigo: '))
            except ValueError:
                print("Debes escribir un codigo correcto")
                continue
            if codigo < 0:
                  print("Escribir nuevamente, solo admite numeros positivos")
                  continue
            else:
                break
    while True:
            try:
               descripcion = input('Ingrese la descripcion: ')
            except ValueError:
                continue
            if not(descripcion.isalpha()):
                  print("Escribir nuevamente, solo admite letras")
                  continue
            else:
                break
        
    gru = modgrupo(cod=codigo, des=descripcion)
    respuesta = input(f"Deseas modificar el grupo:  {descripcion}[s/n]:")
    if not respuesta or respuesta[0].lower() != 's':
        input('Presione una tecla para continuar')
        ejecutar_grupo()
    else:
        if ctrgr.modificar(gru):  
           print("Registro modificado correctamente")
        else:
           print('Error al modificar el registro')
    

def eliminargr():
    while True:
            try:
                codigo = int(input('Ingrese el codigo: '))
            except ValueError:
                print("Debes escribir un codigo correcto")
                continue
            if codigo < 0:
                  print("Escribir nuevamente, solo admite numeros positivos")
                  continue
            else:
                break

    gru = modgrupo(cod=codigo)
    respuesta = input(f"Deseas eliminar el grupo:  {codigo}[s/n]:")
    if not respuesta or respuesta[0].lower() != 's':
        input('Presione una tecla para continuar')
        ejecutar_grupo()
    else:
        if ctrgr.modificar(gru):  
           print("Registro eliminado correctamente")
        else:
           print('Error al eliminar el registro')

    
def consultargr():  
    buscar = input('Ingrese descripcion a buscar: ')
    gru = ctrgr.consulta(buscar)
    for registro in gru:  
        print('{:7} {:3} '.format(registro[0],registro[1]))  #{:7} .- que de 7 espacios

def ejecutar_grupo():
    opcg = ''
    while True:
        opcg= str(menugrupo(
            ['Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Retornar a Menú principal'],
            'Menú Grupo de cuentas'))
        if opcg == '0':
            print('\n<<<Ingresar datos>>> ')
            valor = input(' Ingrese cantidad de datos a ingresar')
            ingresargr(valor)
        elif opcg == '1':
            print('\n<<<Modificar datos>>> ')
            modificargr()
        elif opcg == '2':
            print('\n<<<Eliminar datos>>> ')
            eliminargr()
        elif opcg == '3':
            print('\n<<<Consultar datos>>> ')
            consultargr()

        elif opcg == '4':
            ejecutar_menu()
            break
        elif opcg != '4':
            print('Seleccione una opcion correcta')
        input('Presione una tecla para continuar')
        os.system('cls')


ctrplan = CtrPlanc()

def ingresar(rango):  #Dependera del numero que se desea ingresar
    for i in range(int(rango)):
        while True:
            try:
                codigo = input('Ingrese el codigo: ')
                idgrupo = input('Ingrese el codigo del grupo: ')
                descripcion = input('Ingrese la descripcion: ') 
                naturaleza = input('Ingrese la naturaleza de la cuenta: ')
                estado = input('Ingrese el estado: ')
            except ValueError:
                continue
            if not(descripcion.isalpha()):
                  print("Escribir nuevamente, solo se admiten letras")
                  continue
            else:
                break
        plan = planC(cod=codigo,idgru=idgrupo,des=descripcion,natu=naturaleza,est=estado)
        respuesta = input(f"Deseas guardar el grupo:  {codigo,idgrupo,descripcion,naturaleza,estado} [s/n]:")
        if not respuesta or respuesta[0].lower() != 's':
            input('Presione una tecla para continuar')
            ejecutar_plan()
        else:
            if ctrplan.ingresar(plan):  #Proceso de validacion con la variable "correcto" (booleano)
               print("Registro ingresado correctamente")
            else:
               print('Error al ingresar el registro')
        

def modificar():  
    while True:
            try:
                idplan = int(input('Ingrese el id del plan: '))
            except ValueError:
                print("Debes escribir un codigo correcto")
                continue
            if idplan < 0:
                print("Escribir nuevamente, solo admite numeros positivos")
                continue
            else:
                break
    while True:
            try:
                codigo = int(input('Ingrese el codigo: '))
            except ValueError:
                print("Debes escribir un codigo correcto")
                continue
            if codigo < 0:
                print("Escribir nuevamente, solo admite numeros positivos")
                continue
            else:
                break
    while True:
            try:
                idgrupo = int(input('Ingrese el codigo del grupo: '))
            except ValueError:
                print("Debes escribir un codigo correcto")
                continue
            if idgrupo < 0:
                print("Escribir nuevamente, solo admite numeros positivos")
                continue
            else:
                break
    while True:
            try:
                descripcion = input('Ingrese la descripcion: ') 
                naturaleza = input('Ingrese la naturaleza de la cuenta (A-D): ')
                estado = input('Ingrese el estado: ')            
            except ValueError:
                continue
            if not(descripcion.isalpha()):
                  print("Escribir nuevamente, solo admite letras")
                  continue
            else:
                break
    plan = planC(id=idplan, cod=codigo, idgru=idgrupo, des=descripcion, natu=naturaleza,est=estado)
    respuesta = input(f"Deseas modificar el grupo:  {idplan,codigo,idgrupo,descripcion,naturaleza,estado}[s/n]:")
    if not respuesta or respuesta[0].lower() != 's':
        input('Presione una tecla para continuar')
        ejecutar_plan()
    else:
        if ctrplan.modificar(plan):  
             print("Registro modificado correctamente")
        else:
             print('Error al modificar el registro')
    

def eliminar():  
    while True:
            try:
               idplan = int(input('Ingrese el id del plan: '))
            except ValueError:
                print("Debes escribir un codigo correcto")
                continue
            if idplan < 0:
                  print("Escribir nuevamente, solo admite numeros positivos")
                  continue
            else:
                break

    plan = planC(id=idplan)
    respuesta = input(f"Deseas eliminar el grupo:  {idplan}[s/n]:")
    if not respuesta or respuesta[0].lower() != 's':
        input('Presione una tecla para continuar')
        ejecutar_plan()
    else:
        if ctrplan.eliminar(plan):  
            print("Registro eliminado correctamente")
        else:
            print('Error al eliminar el registro')
    

def consultar():  
    buscar = input('Ingrese descripcion a buscar: ')
    plan = ctrplan.consulta(buscar)
    for registro in plan:  
        print('{:7}    {:3}    {:3}    {:3}   {:3}  {:}'.format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5]))  

def ejecutar_plan():
    opcp = ''
    while True:
        opcp= str(menuplan(
            ['Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Retornar a Menú principal'],
            'Menú Plan de cuentas'))
        if opcp == '0':
            print('\n<<<Ingresar datos>>> ')
            valor = input(' Ingrese cantidad de datos a ingresar')
            ingresar(valor)
        elif opcp == '1':
            print('\n<<<Modificar datos>>> ')
            modificar()
        elif opcp == '2':
            print('\n<<<Eliminar datos>>> ')
            eliminar()
        elif opcp == '3':
            print('\n<<<Consultar datos>>> ')
            consultar()
        elif opcp == '4':
            ejecutar_menu()
            
            break
        elif opcp != '4':
            print('Seleccione una opcion correcta')
        input('Presione una tecla para continuar')
        os.system('cls')
    
def ejecutar_menu():
    opc = ''
    while True:
        opc= str(menu(
            ['Grupo de cuentas', 'Plan de cuentas', 'Salir'],
            'Menú Principal'))
        if opc == '0':
            ejecutar_grupo()   
        elif opc == '1':
               ejecutar_plan()
    
        elif opc == '2':
            print('Gracias por usar el Sistema')
        input('Presione una tecla para continuar')
        exit()
        break
        os.system('cls') #limpia pantalla

ejecutar_menu()