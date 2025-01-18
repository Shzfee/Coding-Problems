import random
print('This program simulates a rock, paper and scissors game.')


def playAgain():
    print('Would you like to play again?')
    user_input = input('Type \'y\' for yes and anything for no.   ').lower()
    
    if user_input == 'y':
        rockPaperScissors()
    else:
        while True:
            break


def rockPaperScissors():
    options = ['rock', 'paper', 'scissors']
    target = random.choice(options)

    while True:
        user_input=input('Please enter Rock Paper or Scissors:   ').lower()
        if user_input not in options:
            print('Invalid input.')
        elif user_input in options:
            break
    
    if user_input == target:
        print('You won!')
    else:
        print(f'you lose! The computer chose {target}!')
    
    playAgain()

    
rockPaperScissors()