import random

def playAgain():
    user_input=input('would you like to play again? Type \'y\' for yes and anything for no:  ')
    if user_input.lower() == 'y':
        cowsAndbulls()
    else:
        while True:
            print('Finished')
            break

def cowsAndbulls():
    bulls = 0                       
    cows = 0
    
    numList = [i for i in range(1,10)]
    target = []

    for i in range(4):
        target.append(random.choice(numList))

    #print('[1,2,3,4]')
    #print(target)
    #target = [1,2,3,4]

    while True:
        bulls = 0                       
        cows = 0
        while True:
            guess = input('please guess the 4 digit number:   ')
            if len(guess) == 4:
                guess = [int(digit) for digit in str(guess)]
                break
        if guess == target:
            print('You won!')
            print(target[0] == guess[0])
            break

        while target[0] == guess[0]:
            bulls = bulls + 1
            #print(f'{bulls} bulls')
            break
        while target[1] == guess[1]:
            bulls = bulls + 1
            #print(f'{bulls} bulls')
            break
        while target[2] == guess[2]:
            bulls = bulls + 1
            #print(f'{bulls} bulls')
            break
        while target[3] == guess[3]:
            bulls = bulls + 1
            #print(f'{bulls} bulls')
            break

        for i in guess:
            if i == target[0]:
                cows = cows + 1
                #print(f'{cows} cows')
            elif i == target[1]:
                cows +=1
                #print(f'{cows} cows')
            elif i == target[2]:
                cows +=1
                #print(f'{cows} cows')
            elif i == target[3]:
                cows+=1
                #print(f'{cows} cows')
        if bulls == 0:
            print(f'You have {cows} cows and {bulls} bulls')
        else:
            print(f'You have {cows-bulls} cows and {bulls} bulls')
        
    playAgain()

    

cowsAndbulls()