fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit", 
}

print(fruit)

veg = {
    "cabbage": "every child's favourite",
    "sprouts": "mmmm, lovely",
    "splinach": "can I have some more fruit, please"
}

print(veg)

veg.update(fruit) # includes all the items of fruit to veg dictionary. modifies the veg dictionary
print(veg)
print()
print()
print(fruit.update(veg))    # does not return anything. includes all the items of veg to fruit dictionary. modifies the fruit dictionary
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print("Nice and Nasty")
print(nice_and_nasty)
print("Veg")
print(veg)
print("Fruit")
print(fruit)