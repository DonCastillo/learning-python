def factorial(x: int) -> int:
    """Solves the factorial of the inputted number

    :param x: number to be calculated for the factorial
    :type x: int
    :return: factorial which is the product of 
    1 * ... (x-1) * (x)
    :rtype: int
    """
    if x == 0:
        return 1
    else:
        y = 1
        for i in range(1, x+1):
            y *= i
        return y


# testing

for i in range(36):
    print("{} {}".format(i, factorial(i)))
