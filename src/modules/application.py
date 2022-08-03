from validator import *

class Application:
    def __init__(self):
        self.outputName = './src/outputs/receiver.txt'
        self.val = Validator()
        self.file = open(self.outputName, 'w')

    def sendMessage(self):
        msg = input('Insert message here... ')
        self.val.asciiToBinary(msg)

    def receiveMessage(self):
        result = self.val.binaryToAscii()
        self.file.write(result + '\n')
    
    def clean(self):
        self.file.close()

