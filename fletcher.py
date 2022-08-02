from bitarray import bitarray

class FletcherChecksum:
    #Los datos binarios se protegen de errores en bloques
    def generate_checksum(self, mes: bytes):
        size, fetch, a, b = 255, 8, 0, 0
        #Modulo de 255, Se almacena en 8 bits cada caracter
        for b in mes:
            a = (a + b) % size
            b = (b + a) % size
            # las dos sumas, cada una con 255 valores posibles, dan como resultado 
            # n valores posibles para la suma de comprobación combinada.