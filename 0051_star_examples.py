numbers = (0, 1, 2, 3, 4, 5)
print(numbers, sep=";")
print(*numbers, sep=";")  # asterisks unpacks the elements from the container
print(0, 1, 2, 3, 4, 5, sep=";")

def test_star(*args):   # just like in JS when dealing with spread operator
    print(args)         # prints a tuple of args
    for x in args:
        print(x)

test_star(0,1,2,3,4,5)
print()

test_star()


# print()
# numbers = [0, 1, 2, 3, 4, 5]
# print(numbers)
# print(*numbers)
