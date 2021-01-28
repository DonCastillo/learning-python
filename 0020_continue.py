shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

# print everythin except the spam
# for item in shopping_list:
#     if item != 'spam':
#         print('Buy ' + item)


for item in shopping_list:
    if item == 'spam':
        continue
    print('Buy ' + item)