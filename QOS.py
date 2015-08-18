from scapy.all import *
import sys
import os
os.system('clear')
op=''
def construir_class_service():
    print("el grupo 802.1 ha trabajado en una extension de la capa MAC que tiene en cuenta CoS. 802.1p es un estandar para la priorizacion de trafico en tramas de la red etiquetados con uno de los ocho niveles de prioridad, donde 7 es alta y 0 es bajo de la siguiente manera: ")
    print("las posibles alternativas para establecer prioridad en class of service son: ")
    print(  "0 - Routine\n"+
    "1 - Priority\n"+
    "2 - Immediate\n"+
    "3 - Flash\n"+
    "4 - Flash Override\n"+
    "5 - Critical\n"+
    "6 - Internetwork Control\n"+
    "7 - Network Control\n")
    prio=input("ingrese un numero de 0-7 de acuerdo con el menu anterior:  ")
    os.system('clear')
    return prio

def envio_paquete(dec_tos,dest):
    os.system('clear')
    paquete=IP(tos=dec_tos,dst=dest)
    print("el paquete construido es: ")
    paquete.show()
    print("\nAgregando class of service:")
    prio_cos=construir_class_service()
    paquete=paquete/Dot1Q(prio=prio_cos)
    print("el paquete de precedencia IP con la cabecera de class of service especificada queda:")
    paquete.show()
    myport=input("ingrese el puerto de destino:  ")
    print("\n Finalmente Agregamos UDP a nuestro paquete, Quedando: ")
    paquete=paquete/UDP(dport=myport)
    paquete.show()
    print("El paquete en hexadecimal es:")
    print(hexdump(paquete))
    op=raw_input("desea enviar el paquete? \n 1 Si \n 2 No\n")
    os.system('clear')
    print("\n \n")
    if(op=='1'):
        send(paquete, loop=1, inter=1)
    print("\n \n")

def construir_precedencia():
    print("Para la precedencia IP se maneja el campo TOS compuesto de 8 bits de la siguiente manera:")
    print("|Precedence|Delay|Throughput|Reliability|Cost| MBZ |")
    print("|  3 bits  |1 bit|  1 bit   |   1 bit   |1bit| 1bit| ")
    print("las posibles alternativas para precedence son: ")
    print(  "000 - Rutina\n"+
            "001 - Prioridad\n"+
            "010 - Inmediata\n"+
            "011 - Flash\n"+
            "100 - Anulacion de Flash\n"+
            "101 - Critico\n"+
            "110 - Control Internetwork\n"+
            "111 - Control de Red")
    print("ingrese estos campos para la construccion de su paquete:")
    precedence=raw_input("Precedence: ")
    delay=raw_input("Delay: ")
    throughput=raw_input("throughput: ")
    realiability=raw_input("Realiability: ")
    cost=raw_input("Cost: ")
    mbz=raw_input("MBZ: ")
    tos=''+precedence+delay+throughput+realiability+cost+mbz
    dec_tos=int(tos,2)
    print("campo TOS: "+tos+" Decimal: "+str(dec_tos))
    dest=raw_input("Ingrese la Direccion destino: ")
    envio_paquete(dec_tos,dest)

def construir_dscp():
    print("DiffServ maneja 6 bits de la siguiente manera:")
    print("|  DiffServ Code Point | no usado |")
    print("|        6 bits        | 2 bits   | ")
    print("Donde DiffServ Code Point es un valor que determina la probabilidad de descartar un paquete y si el reenvio es acelerado o asegurado de la siguiente manera:\n")
    print("comportamiento por salto|             DiffServ Code Point                |")
    print("Default                 |                   000000                       |")
    print("                        |bajo % descarte|medio % descarte|alto % descarte|")
    print("Reenvio Asegurado class1|AF11: 001010   |AF12: 001100    |AF13: 001110   |")
    print("Reenvio Asegurado class2|AF21: 010010   |AF22: 010100    |AF23: 010110   |")
    print("Reenvio Asegurado class3|AF31: 011010   |AF32: 011100    |AF33: 011110   |")
    print("Reenvio Asegurado class4|AF41: 100010   |AF42: 100100    |AF43: 100110   |")
    print("Reenvio Acelerado       |EF:   101110   |                |               |\n")
    dscp=raw_input("ingrese el valor de los 6 bits que desee de acuerdo a la tabla anterior: ")
    tos=dscp+"00"
    dec_tos=int(tos,2)
    print("campo TOS: "+tos+" Decimal: "+str(dec_tos))
    dest=raw_input("Ingrese la Direccion destino: ")
    envio_paquete(dec_tos,dest)


def construir_paquete():
    print("De que manera desea construir su paquete: \n 1 TOS con precedencia IP \n 2 TOS con DSCP \n 0 Para salir")
    op=input("digite la opcion: ")
    os.system('clear')
    if(op==1):
        construir_precedencia()
    if(op==2):
        construir_dscp()

while(op!=2):
    print("desea Construir un paquete? \n 1 Si \n 2 No")
    op=input("digite la opcion: ")
    os.system('clear')
    if(op==1):
        construir_paquete()
