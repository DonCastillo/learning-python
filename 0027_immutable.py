# immutable objects cannot be changed. 
# Once it is created changing its value would result to creation of another reference
# of memory address or creation of another object

# built-in types that are immutable: int, float, bool, string, unicode, tuple

print('Immutable')
result = 'Correct'
another_result = result

print(id(result))
print(id(another_result))

result += 'ish'
print(id(result))
print(id(another_result))


# mutable objects can be changed. 
# Once it is created, changing its values does not change the memory address or create another object

# built-in types that are mutable: list, dict, set, Bytearray

print('Mutable')
shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ['cookies'] # merges into the existing list
print(id(shopping_list))    # still have the same memory address
print(shopping_list)
print(another_list)

a = b = c = d = e = f = another_list  # same as
# a = another_list
# b = another_list
# c = another_list
# d = another_list
# e = another_list
# f = another_list
print(a)
print('Adding cream')
b.append('cream')
print(c)
print(d)
print(shopping_list)
