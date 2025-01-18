print('This program generates a chosen legnth of a fibbonacci sequence.')

def fibbonacciNumbers():
    fib_list = []
    a =0               
    b = 0             
    c =0               

    while True:
        try:
            n = int(input('Please choose the length of the Fibbonacci sequence.   '))       #Range
            break
        except ValueError:
            print('Invalid input.')

    for i in range(n):
        c = a + b
        fib_list.append(c)
        a = b
        b = c
        if b == 0:
            b = b + 1
            fib_list.append(1)
        
    
    print(fib_list)
            




fibbonacciNumbers()