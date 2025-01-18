import random

def playAgain():
    user_input = input('Would you like to play again? type \'y\' for yes and \'n\' for no or anything.   ')
    if user_input.lower() == 'y':
        numberGame()
    else:
        while True:
            print('Finished.')
            break
        
        

def numberGame():
    target = random.randint(0,100)

    while True:
        while True:
            try:
                user_guess = int(input('Guess a number between 0 and 100.   '))
                break
            except ValueError:
                print('Invalid input. Guess a number.   ')
        if user_guess == target:
            print('Correct!')
            break
            

        elif user_guess > target:
            print('Too high. Guess again.   ')
        
        else:
            print('Too low! Guess again.    ')
    
    playAgain()
    
numberGame()