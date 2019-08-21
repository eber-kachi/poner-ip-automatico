import os
import time

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

while 1:
    os.system('cls')
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
            os.system(f'netsh interface ipv4 set address name="Ethernet" static 192.168.1.{ipNumero} 255.255.255.0 192.168.1.1')
            archivEscribir=open('ip.txt','w')
            ipNumero = int(ipNumero) + 1 
            archivEscribir.write(str(ipNumero))
            archivEscribir.close()
            print('finalizado..')

        elif opcion == "2":
            # ip escrito
            archivo=open('ip.txt','r+')
            ipNumero=archivo.readline() 
            print("Dijite tipo de IP ejm(192.168.1.*automatico)")
            tipoIp=input()
            print("Mascara ejm(/24)")
            tipoMascara=input() 
            print (os.system('netsh interface ipv4 set address name="Ethernet" static {0}{1} {2} 192.168.1.1'.format(tipoIp,ipNumero,tipoMascara)))

    elif opcion=="2":
        print("borrando ip")
        os.system('ipconfig /release')
        time.sleep(10)
        os.system('ipconfig /renew')
        time.sleep(10)
        os.system('ipconfig /flushdns')
        print("ya tiene su nueva ip")
        print(os.system('ipconfig'))
    elif opcion == '0':
        break


raw_input()
    







