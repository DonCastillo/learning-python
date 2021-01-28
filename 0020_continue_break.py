shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

# print everythin except the spam
# using break
for item in shopping_list:
    if item == 'spam':
        break
    print('Buy ' + item)


print('-' * 20)

# using continue
for item in shopping_list:
    if item == 'spam':
        continue
    print('Buy ' + item)

# stop printing when i is more than 0 and a divisible by 11
for i in range(0, 100, 7):
    print(i)
    if (i % 11 == 0) and (i > 0):
        break

# print all numbers from 0 to 20 that aren't divisble by 3 or 5
for i in range(1, 21):
    if (i % 3 == 0) or (i % 5 == 0):
        continue
    print(i)