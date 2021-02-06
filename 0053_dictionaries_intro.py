fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit", 
    "apple": "round and crunchy" # replaces value of the first apple
} # format just like JSON, can access value via key in string format

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
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)
    # retrives the value based on the key entered. 
    # like accessing through fruit["orange"]
    # print(description)