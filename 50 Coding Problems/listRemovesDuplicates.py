import random



def removeDupes():
    list1 = []
    noDupes = []
    
    for i in range(30):
        list1.append(random.randint(1,10))
    
    print(list1)

    while True:
        for i in list1:
            if i not in noDupes:
                noDupes.append(i)
            elif i in noDupes:
                continue
        break
    print(noDupes)


removeDupes()