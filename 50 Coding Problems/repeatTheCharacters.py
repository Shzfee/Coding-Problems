

def repeater():
    a = input('Please enter a sentence and it will be doubled.  ')
    aList = list(a)
    register = ''


    for i in aList:
        register += i*2
    print(register)

repeater()
