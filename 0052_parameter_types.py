def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:....{}, {}".format(p1, p2))
    print("var-positional (*args):...{}".format(args))
    print("keyword:..................{}".format(k))
    print("var-keyword:..............{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)


def sum_numbers(*args: float) -> float:
    """numbers to be added to each other

    :return: sum
    :rtype: int
    """
    return sum(args)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
