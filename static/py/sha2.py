def charToBin(char):
    


def sha2(userIn="hello world"):
    binary=''.join(format(ord(i), 'b') for i in userIn)
    binlength = len(binary)
    print(str(binary))
    print(str(binlength))

    binary += '1'
    
    print(str(binary))
    
    while((len(binary) % 512) != 0):
        binary += '0'

    print(str(binary))
    print(len(binary))
    
    binary += format(len(userIn), 'b')

    print(str(binary))
    print(len(binary))


def __main__():
    sha2()
