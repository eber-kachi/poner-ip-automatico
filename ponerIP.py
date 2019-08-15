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

os.system('color a')
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
        archivo=open('ip.txt','r+')
        ipNumero=archivo.readline() 
        print("estas es la ip "+ipNumero)
        os.system(f'netsh interface ipv4 set address name="Wi-Fi" static 192.168.1.{ipNumero} 255.255.255.0 192.168.1.1')
        # archivEscribir=open('ip.txt','w')
        ipNumero = int(ipNumero) + 1 
        archivo.write(str(ipNumero))
        archivo.close()
        print('finalizado..')

    elif opcion == "2":
        # ip escrito
        print("Dijite tipo de IP ejm(192.168.1.*automatico)")
        tipoIp=input()
        print("Mascara ejm(/24)")
        tipoMascara=input()

# raw_input()
    







