import os
# file = open("ip.txt", "w")
# file.write("2" + os.linesep)
# file.close()

# metodo para menu dinamico 
def menu(mensajes):
    cont=1
    for  mensaje in mensajes:
        print("•÷±‡±( {0}. {1} )±‡±÷ ".format(cont, mensaje))
        cont+=1

    print("•÷±‡±( 0. Salir )±‡±÷ ")

menu(["Crear archivo ip.txt","Poner Ip ", "Borrar Ip"])

opcion=input()
if opcion=="1":
    file = open("ip.txt", "w")
    file.write("2" + os.linesep)
    file.close()
    print("se creo con exito")
elif opcion=="2":
    menu(["IP por defecto (192.168.1.{})","Opcion Avanzada","Configurar"])
    opcion=input()
    if opcion=="1":
        # ip por defecto

    elif opcion =="2":
        # ip escrito
        print("Dijite tipo de IP ejm(192.168.1.*automatico)")
        tipoIp=input()
        print("Mascara ejm(/24)")
        tipoMascara=input()
    







