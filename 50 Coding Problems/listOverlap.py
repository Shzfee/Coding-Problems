import random

list1 = []
list2 = []
sameList = []
n = 1

for i in range(10):
    list1.append(random.randint(1,10))

for i in range(10):
    list2.append(random.randint(1,10))

range1 = len(list1)
range2 = len(list2)

print (list1)
print(range1)
print (list2)
print(range2)
limit = 0

for i in range(11):
    for i in list1:
        for z in list2:
            if z in sameList:
                continue
            elif z == i:
                sameList.append(z)
                
print(sameList)