# Referencia de código https://www.geeksforgeeks.org/implementing-checksum-using-python/

from bitarray import bitarray

class FletcherChecksum:

    def __init__(self, arrayBitsSent, arrayBitsReceived):
        self.bitsSent = arrayBitsSent
        self.bitListSent = self.bitsSent.tolist()
        self.bitsRec = arrayBitsReceived
        self.bitListRec = self.bitsRec.tolist()
    
    def checkSumSeparator(self, k): #Mensaje que envia
        c1 = self.bitsSent[0:k]
        c2 = self.bitsSent[k:2*k]
        c3 = self.bitsSent[2*k:3*k]
        c4 = self.bitsSent[3*k:4*k]
       
        sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]

        if(len(sum) > k):
            x = len(sum)-k
            sum = bin(int(sum[0:x], 2)+int(sum[x:], 2))[2:]
        if(len(sum) < k):
            sum = '0'*(k-len(sum))+sum
        

        Checksum = ''
        for i in sum:
            if(i == '1'):
                Checksum += '0'
            else:
                Checksum += '1'
        return Checksum

    def checkReceiver(self, k, Checksum): #Mensaje recibido
        c1 = self.bitsRec[0:k]
        c2 = self.bitsRec[k:2*k]
        c3 = self.bitsRec[2*k:3*k]
        c4 = self.bitsRec[3*k:4*k]

        sumReceiver = bin(int(c1, 2)+int(c2, 2)+int(Checksum, 2) + int(c3, 2)+int(c4, 2)+int(Checksum, 2))[2:]

        if(len(sumReceiver) > k):
            x = len(sumReceiver)-k
            sumReceiver = bin(int(sumReceiver[0:x], 2)+int(sumReceiver[x:], 2))[2:]

        checkSum_receiver = ''
        for i in sumReceiver:
            if(i == '1'):
                checkSum_receiver += '0'
            else:
                checkSum_receiver += '1'
        return checkSum_receiver

    def execFletcher(self):
        k=8 
        Checksum = self.checkSumSeparator(k)
        sumReceiver = self.checkReceiver(k, Checksum)

        print("Sent checksum: ", Checksum)
        print("Checksum Received: ", sumReceiver)

        finalsum=bin(int(Checksum,2)+int(sumReceiver,2))[2:]

        #Se encuentra la suma de la suma de la verificación enviada y la suma de la verificación recibida
        finalComparation=''
        for i in finalsum:
            if(i == '1'):
                finalComparation += '0'
            else:
                finalComparation += '1'

        if(int(finalComparation,2) == 0):
            print("Receiver checksum is 0.")
            print("This was accepted")
            
        else:
            print("Checksum was not 0.")
            print("An error has been detected")
