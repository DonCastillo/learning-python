import random


def get_integer(prompt):
    """Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, untial a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{0} is not a valid number".format(temp))


help(get_integer)
# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)

highest = 10
answer = random.randint(1, highest)
print(answer)   # todo: remove after testing



print("Please guess number between 1 and {}: ".format(highest))
while True:
    guess = get_integer(": ")
    if guess < answer:
        print('Please guess higher')
    elif guess > answer:
        print('Please guess lower')
    else:
        print('You\'ve guessed it right')
        break;
    
