from bitarray import bitarray
import random
from validator import *

class Noiser:
    def __init__(self, validator):
        self.errProbability = 0.01
        self.list = []
        self.val = validator
        self.indexList = []
    
    def addNoise(self, arrBit):
        self.list = arrBit.tolist() # [False, True, False] = 010
        weights = [self.errProbability*len(self.list)] * len(self.list)
        weights = tuple(weights)

        for i in range(len(self.list)):
            self.indexList.append(i)
        
        for bit in range(len(arrBit)):
            chosen = random.choices(self.indexList, weights=weights, k=1)
            if bit == chosen:
                self.list[bit] = not self.list[bit]
        
        self.val.listToBitArray(self.list)

