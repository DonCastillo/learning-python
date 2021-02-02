def multiply(x: float, y: float) -> float:
    """Multiplies two number

    :param x: multiplicand
    :type x: int/float
    :param y: multiplier
    :type y: int/float
    :return: The product of `x` and `y`
    :rtype: int/float
    """
    result = x * y
    return result


def isPalindrome(string: str) -> bool:
    """Checks if a string is a palindrome or not

    :param string: string to be examined
    :type string: string
    :return: True if palindrome, False if not
    :rtype: Boolean
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """Checks if a string or sentence is a palindrome 
        ignoring whitespance and non alphanumeric characters

    :param sentence: string to be examined
    :type sentence: string
    :return: True if palindrome, False if not
    :rtype: Boolean
    """
    sentence = sentence.replace(" ", "")
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return isPalindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n`th fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result
    

for i in range(36):
    print(i, fibonacci(i))


p = palindrome_sentence("radar")

# answer = multiply(10.5, 4)
# print(answer)

# forty_two = multiply(6, 7)
# print(forty_two)

# print()

# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

# # word
# word = input("Please enter a word to check: ")
# if isPalindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# # sentence
# sentence = input("Please enter a sentence to check: ")
# print((palindrome_sentence(sentence)))
