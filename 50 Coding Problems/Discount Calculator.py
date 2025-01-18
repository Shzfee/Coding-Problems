def discountCalc():
    while True:
        try:
            original = float(input('This is a discount calculator. Please enter original price.   '))
            break
        except ValueError:
            print('Invalid input. Please enter the original price.')
    
    while True:
        try:
            discount = float(input('Please enter the percentage of discount.   '))
            break
        except ValueError:
            print('Invalid input. Please enter the percentage value.    ')

    newPrice = original - (original * (discount/100))

    print('Discounted Value is: ', newPrice)

    while True:
        user_input = input('If you would like to continue, type anything. If you would like to end this program type \'end\'.   ')
        if user_input.lower() == 'end':
            break
        else:
            discountCalc()

discountCalc()