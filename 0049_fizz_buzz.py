def fizz_buzz(x: int) -> str:
    """Returns an appropiate phrase or word based
    on wether the x is divisible either by 3 or 5. If not,
    it returns the string of x

    :param x: any integer
    :type x: int
    :return: returns "fizz buzz" when `x` is both divisible by 3 or 5;
    returns "fizz" if `x` is divisible by 3, returns "buzz" if `x` is divisible
    by 5. Returns the `x` itself when any of the conditions above are not met
    :rtype: str
    """
    if x % 3 == 0 and x % 5 == 0:
        return "fizz buzz"
    elif x % 3 == 0:
        return "fizz"
    elif x % 5 == 0:
        return "buzz"
    else:
        return str(x)


input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    players_answer = correct_answer
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))
