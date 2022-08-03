#codigo de referencia de https://rosettacode.org/wiki/CRC-32

from bitarray import bitarray

class Crc:
    def xor(self, a, b):
        if a == b:
            return '0'
        else:
            return '1'


    def operateXor(self, divisor, dividend):
        result = ''
        for i in range(4):
            a = divisor[i]
            b = dividend[i]
            temp = self.xor(a, b)
            result += str(temp)

        if result[0] == '0':
            result = result[1:]

        return result

    def algorithmCRC(self, ba):
        result = '000'
        dividend = '1001'
        dv = result + ba
        division = dv[0:4]
        result2 = self.operateXor(division, dividend)

        for i in range(4, len(ba)):
            division = result2 + dv[i]

            if division[0] == '1':
                result2 = self.operateXor(division, dividend)

            else:
                temp = division[1:]
                result2 = temp
            
        return result2