def palindrom():
    while True:
        user_input=input('Enter a word and it will return whter its a palindrom or not.   ')
        reverse = user_input[::-1]
        print(reverse)

        if user_input == reverse:
            print('Its a palindrom.')
        else:
            print('Not a palindrom.')

palindrom()