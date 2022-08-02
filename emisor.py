import socket
import pickle
from random import randrange
from bitarray import bitarray
from fletcher import FletcherChecksum

class Emisor:
    def __init__(self, name):
        self.name = name
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Se usa socket para el envío y recepción de mensajes
        self.sckt.bind((socket.gethostname(), 1234)) #Número del puerto
        self.sckt.listen(3)
        print("Emisor creado") #Se establece la conexión y se enlaza con el cliente

    def verification(self, cadena): #Envia la cadena segura
        fletcher = FletcherChecksum()
        print(fletcher.generate_checksum(cadena))

    def cadena_Ruido(self, cadena): #Se agrega ruido
        caracter = randrange(0, 2)
        pos = randrange(0, len(cadena) - 1)
        cadena = cadena[:pos] + str(caracter) + cadena[pos+1:]
        return cadena

    def enviar_objeto(self, data): #Se transmite
        clientsocket, address = self.sckt.accept()
        clientsocket.send(data)

    def enviar_CadenaSegu(self, msg):
        cadena__binascii = bin(int.from_bytes(msg.encode(), 'big'))
        cadena__ruido = self.cadena_Ruido(cadena__binascii[2:])
        cadena__bitarray = bitarray(cadena__ruido)
        data = pickle.dumps(cadena__bitarray) #Se serializa el bitarray
        self.enviar_objeto(data)

    def enviar_cadena(self):
        self.enviar_CadenaSegu("Hola")   


em = Emisor("Emisor")
em.enviar_cadena()