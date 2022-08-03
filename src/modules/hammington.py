# codigo extraido de: https://www.geeksforgeeks.org/hamming-code-implementation-in-python/#:~:text=Hamming%20code%20is%20a%20set,the%20sender%20to%20the%20receiver.&text=Hamming%20for%20error%20correction

class Hammington: 
    def detectError(arr, nr): 
        n = len(arr)
        result = 0

        for i in range(nr):
            value = 0
            for j in range(1, n+1):
                if(j & (2**i) == (2**i)):
                    value = value ^ arr[-1*j]

        result = result + value(10**i)
        return int(str(result),2)
