import random


highest = 10
answer = random.randint(1, highest)
print(answer)   # todo: remove after testing




while True:
    guess = int(input('Please guess a number between 1 and {}: '.format(highest)))
    if guess < answer:
        print('Please guess higher')
    elif guess > answer:
        print('Please guess lower')
    else:
        print('You\'ve guessed it right')
        break;
    
