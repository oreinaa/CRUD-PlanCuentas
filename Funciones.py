
def menu(opciones, titulo):
    print('*'*20)    #imprimir caracteres especiales
    print('{}'.format(titulo)) 
    print('*'*20)
    for op in range(0,len(opciones)):
        print("{}) {}".format(op, opciones[op]))
    opc = input('Elija opcion [0...{}]: '.format(len(opciones)-1))
    return opc


def menugrupo(opciones, titulo):
    print('*'*20)    #imprimir caracteres especiales
    print('{}'.format(titulo)) 
    print('*'*20)
    for op in range(0,len(opciones)):
        print("{}) {}".format(op, opciones[op]))
    opc = input('Elija opcion [0...{}]: '.format(len(opciones)-1))
    return opc

def menuplan(opciones, titulo):
    print('*'*20)    #imprimir caracteres especiales
    print('{}'.format(titulo)) 
    print('*'*20)
    for op in range(0,len(opciones)):
        print("{}) {}".format(op, opciones[op]))
    opc = input('Elija opcion [0...{}]: '.format(len(opciones)-1))
    return opc