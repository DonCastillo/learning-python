shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

item_to_find = 'spam'
found_at = None     # like null, does have a value


for index in range(len(shopping_list)):  # len is the size of the array
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print('Item found at position {}'.format(found_at))