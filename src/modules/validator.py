from bitarray import bitarray

# ascii_string = bitarray('string')

class Validator:
    def __init__(self):
        self.ba = bitarray()

    def asciiToBinary(self, message):
        if type(message) != str:
            return None
        self.ba.frombytes(message.encode('utf-8'))
        return self.ba

    def binaryToAscii(self):
        l = self.ba.tolist()
        return bitarray(l).tobytes().decode('utf-8')

    def listToBitArray(self, list):
        self.ba = bitarray(list)

