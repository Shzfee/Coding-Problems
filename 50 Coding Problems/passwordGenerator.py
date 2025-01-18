import random
import string
a = string.ascii_lowercase
b = string.ascii_uppercase
def passwordGenarator():
    lowCase = list(a)
    upCase  = list(b)
    symbols = ['!', '£', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
    password = []

    for i in range(15):
        password.append(random.choice(lowCase))
        password.append(random.choice(upCase))
        password.append(random.choice(symbols))

    #print(lowCase)
    #print(upCase)
    print(''.join(password))

passwordGenarator()