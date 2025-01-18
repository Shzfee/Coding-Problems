list = []
def creatingList():
    while True:
        value = input('Please input a number (press enter when done adding the the list)')
        if value == '':
            break
        else:
            list.append(value)
            print(list)

def sortOrder():
    order = input ('What order would you like? asc or desc?')
    if order == 'asc':
        sortedList = sorted(list)
        print(sortedList)

    elif order == 'desc':
        sortedList = sorted(list, reverse=True)
        print(sortedList)

    else:
        sortOrder()

creatingList()
sortOrder()