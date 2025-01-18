card = input('Please input card number')

def censor(card):
    counter = 0
    cardList = list(card)
    newList = []

    for i in cardList:
        counter = counter + 1
        if counter in range(13):
            newList.append('*')
        else:
            newList.append(i)
    
    print('Your censored card number is:')
    print(' '.join(newList))

censor(card)