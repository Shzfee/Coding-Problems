

def calc():
    valid_operators = ['*', '/', '+', '-']
    while True:
        try:
            int1 = float(input('This is a calculator. Please enter the first number of the equation.    '))
            break
        except ValueError:
            print('invalid input: Please enter the first number.    ')

    while True:
            operator =input('Please input desired operator (e.g *, /, +, -)     ')
            if operator == '*': #or '/' or '+' or '-':
                break
            elif operator == '/':
                break
            elif operator == '+':
                break
            elif operator == '-':
                break
            else:
                print('Invalid input. please type a valid operator. (e.g *, /, +, -)    ')

            
    while True:
        try:
            int2 = float(input('Please enter second number.     '))
            break
        except ValueError:
            print('Invalid input. Please enter the second number.   ')
            
    result = 0
    while True:
        if operator == '*':
            result = (int1 * int2)
            print(result)
            break
        elif operator == '/':
            result = (int1 / int2)
            print(result)
            break
        elif operator == '+':
            result = (int1 + int2)
            print(result)
            break
        elif operator == '-':
            result = (int1 - int2)
            print(result)
            break

    while True:
        user_input=input('if you would like to continue type anything. If you would like to end this program type \'end \' in lowercase      ')
        if user_input.lower() == 'end':
            break
        else:
            calc()
    

calc()