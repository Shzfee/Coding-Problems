

def listNums():
    a = input('This program will make a list of all numbers in the order they were in, given in any sentence. please enter your sentence:   ')
    aList = list(a)
    print(aList)
    newList = []
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    '''for i in aList:
        print(type(i))'''

    for i in aList:
        for x in numbers:
                if i == x:
                    newList.append(i)
    
    print(newList)
            

        



listNums()