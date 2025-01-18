import random

def playAgain():
    user_input = input('Would you like to play again? if yes type \'y\' if not type anything.   ')
    if user_input.lower() == 'y':
        wordGuessingGame()
    else:
        while True:
            print('Finished!')
            break

def wordGuessingGame():
    lives = 3
    words = ['access', 'young' ,'list', 'sphere', 'indirect', 'offend', 'can' ,'remind', 'peanut' ,'looting']
    target = random.choice(words)
    print(target)
    while lives > 0:
        guess = input(f'Guess a word from this list: {words}  ')
        if guess == target:
            print('Correct!')
            break
        elif guess != target:
            lives = lives - 1
            print(f'Incorrect, try again. You have {lives} lives left.')
        elif lives == 0:
            print('You lose!')
            print(f'the answer was: {target}')
            break
    if lives == 0:
        print('You lose!')
        print(f'the answer was: {target}')
    
    playAgain()



wordGuessingGame()