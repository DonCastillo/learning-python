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