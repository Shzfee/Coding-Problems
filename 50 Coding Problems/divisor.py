num = int(input('Input a number and it will return all the numbers that divide into it.   '))

divisors = []
list = list(range(1, num+1))

#print(list)

for i in list:
    if num % i == 0:
        divisors.append(i)
    
print(divisors)