for i in range(0, 20):  # prints from 0 through 19, by 1 step => 0, 1, ... 19
    print('i is now {}'.format(i))

print('-' * 20)

for i in range(0, 20, 2):   # prints from 0 through 19, by 2 steps => 0, 2, 4, ... 18
    print('i is now {}'.format(i))

print('-' * 20)

for i in range(10, 0, -2):   # prints from 10 through 2, by -2 steps => 10, 8, 6, ... 2
    print('i is now {}'.format(i))


# range can be used in conditional statement
age = int(input('Enter age: '))

if age in range(16, 66):
    print('Have a good day at work')
else:
    print('Enjoy your free time')
    