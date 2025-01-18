num = int(input('Input a number that you want to convert into binary. (max num 255)'))

#print(num)

def numToBinary(num):
    order = 8
    binary = []
    while order == 8:
        if num >= 128:
            binary.insert(0,1)
            num = num-128 
            print(binary)
            print(num)
            order = order - 1
            
        elif num < 128:
            binary.insert(0,0)
            order = order- 1
            
    while order == 7:
        if num >= 64:
            binary.insert(0,1)
            num = num - 64
            print(binary)
            print(num)
            order = order - 1
            
        elif num <= 64:
            binary.insert(0,0)
            order = order - 1
            
    while order == 6:
        if num >= 32:
            binary.insert(0,1)
            num = num - 32
            print(binary)
            print(num)
            order = order - 1
        elif num <= 32:
            binary.insert(0,0)
            order = order - 1

    while order == 5:
        if num >= 16:
            binary.insert(0,1)
            num = num - 16
            print(binary)
            print(num)
            order = order - 1
        elif num <= 16:
            binary.insert(0,0)
            order= order -1
    
    while order == 4:
        if num >= 8:
            binary.insert(0,1)
            num = num - 8
            print(binary)
            print(num)
            order = order - 1
        elif num <= 8:
            binary.insert(0,0)
            order =order - 8
    
    while order == 3:
        if num >= 4:
            binary.insert(0,1)
            num = num - 4
            print(binary)
            print(num)
            order = order -1
        elif num <= 4:
            binary.insert(0,0)
            order = order -1
    while order == 2:
        if num >= 2:
            binary.insert(0,1)
            num = num - 2
            print(binary)
            print(num)
            order = order - 1
        elif num <= 2 :
            binary.insert(0,0)
            order = order - 1
    
    while order == 1:
        if num >= 1:
            binary.insert(0,1)
            num = num - 1
            print(binary)
            print(num)
            print('Done!')
            return
        elif num <= 1:
            binary.insert(0,0)
            print(binary)
            print(num)
            print('Done!')
            return


numToBinary(num)