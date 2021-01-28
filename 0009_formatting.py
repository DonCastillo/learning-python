for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))    # {index : width length which is the number or characters that will fit into the width}
                                                                                    # right aligned (default)

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))  # left aligned

for i in range(1, 13):   
    print("No. {0:2} squared is {1:^4} and cubed is {2:^4}".format(i, i**2, i**3))  # center aligned

for i in range(1, 13):   
    print("No. {0:2} squared is {1:>4} and cubed is {2:>4}".format(i, i**2, i**3))  # right aligned

print()

print("Pi is approximately {0:12}".format(22 / 7))          # general format
print("Pi is approximately {0:12f}".format(22 / 7))         # 6 digits after the decimal point
print("Pi is approximately {0:12.50f}".format(22 / 7))      # 50 digits after the decimal point
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
