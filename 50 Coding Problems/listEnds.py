print('This program will return the first and last of a list you type in. please type \'end\' when you want the list to end.')


def listEnds():
    list1 = []
    newList = []

    while True:
        user_input = input('Type to add to your list:       ').lower()
        if user_input == 'end':
            break
        else:
            list1.append(user_input)
    
    print(list1)

    newList.insert(0,list1[0])
    newList.append(list1[-1])
    print(newList)


listEnds()