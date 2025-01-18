

def primality():
    while True:
        try:
            num = int(input('Input a number and it will return whether or not it is a prime number.   '))
            break
        except ValueError:
            print('invalid input. Please enter a number')

    divisors = []
    list1 = list(range(1, num+1))

    #print(list)

    for i in list1:
        if num % i == 0:
            divisors.append(i)
        
    print(divisors)

    if divisors == [1,num]:
        print(f'{num} is a prime number.')
    else:
        print(f'{num} is not a prime number.')

primality()