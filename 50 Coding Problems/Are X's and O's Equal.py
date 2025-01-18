sentence = input('Please Input a sentence and the X\'s and O\'s will be counted:    ')

sList = list(sentence)

def xandoCounter(sentence):
    sList = list(sentence)
    x_Counter = 0
    o_Counter = 0

    for i in sList:
        if i == 'x':
            x_Counter = x_Counter + 1
        elif i == 'o':
            o_Counter = o_Counter + 1
    
    print(x_Counter == o_Counter)

xandoCounter(sentence)