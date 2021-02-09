fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit", 
    "apple": "round and crunchy" # replaces value of the first apple
} # format just like JSON, can access value via key in string format

# fruit.keys()   = dict_keys(['orange', 
#                             'apple', 
#                             'lemon', 
#                             'grape', 
#                             'lime', 
#                             'apple'])
# fruit.values() = dict_values(['a sweet, orange, citrus fruit', 
#                               'good for making cider', 
#                               'a sour, yellow citrus fruit', 
#                               'a small, sweet fruit growing in bunches', 
#                               'a sour, green citrus fruit', 
#                               'round and crunchy'])

print(fruit)
print()
print(fruit["orange"])
print()
fruit["pear"] = "an odd-shaped fruit"  # appending a new key-value pair
print(fruit)
fruit["pear"] = "great with tequila"
print()
print(fruit)

del fruit["lemon"]  # deletes lemon item
# del fruit  # deletes the entire dictionary
print()
print(fruit)

# fruit.clear()   # removes all element in the dictionary. dictionary stil exists but empty
print()
print(fruit)

# print(fruit["tomato"])  # error. tomato does not exist in the dictionary
print()
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     # description = fruit.get(dict_key, "We don't have a "+ dict_key) # like a ternary
#     # fruit.has_key(dict_key) # alternative to "if dict_key in"
#     # print(description)
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)
#     # retrives the value based on the key entered. 
#     # like accessing through fruit["orange"]
#     # print(description)

# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

ordered_keys = sorted(list(fruit.keys()))
# ordered_keys.sort() # sorts the keys in place
for f in ordered_keys:
    print(f + " - " + fruit[f]) 
# print(ordered_keys)
print()
for f in sorted(list(fruit.keys())):
    print(f + " - " + fruit[f]) 

print()
for val in fruit.values():
    print(val)

print()
for val in fruit.values():
    print(val)
print('-' * 40)

print()
for key in fruit.keys():
    print(key)

fruit["tomato"] = "not nice with ice cream"
print(tuple(fruit.keys()))
print('*' * 40)
print(tuple(fruit.items()))
print('*' * 40)

for snack in tuple(fruit.items()):
    item, description = snack
    print(item + " is " + description)

print('*' * 40)
print(dict(tuple(fruit.items())))