from bitarray import bitarray
from application import *
from noiser import *
from enum import Enum
from hammington import Hammington
from crc32 import Crc
from fletcher import FletcherChecksum

class Algorithm(Enum):
    FLETCHER = 0
    CRC32 = 1
    HAMMINGTON = 2


class Transmitter:
    def __init__(self, algthm):
        self.original = None
        self.final = None
        self.app = Application()
        self.valid = self.app.val
        self.noiser = Noiser(self.valid)
        self.alg = algthm
    
    def startSession(self):
        # Ask for message
        self.app.sendMessage()
        self.original = self.valid.ba

        # Add some noise (error) to the message
        self.noiser.addNoise(self.valid.ba)

        self.final = self.valid.ba

        if self.original == None or self.final == None:
            return

        # Check for error
        if self.alg == 0:
            algo = FletcherChecksum(self.original, self.final)
        elif self.alg == 1:
            algo = Crc()
            pass
        elif self.alg == 2:
            algo = Hammington()
            pass

        # Receive message
        self.app.receiveMessage()
        
        # Close output files
        self.app.clean()

