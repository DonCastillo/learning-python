menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# removes all the occurence of spam
for meal in menu:
    if meal.count("spam") > 1:
        for index in range(len(meal) - 1, -1, -1):
            if meal[index] == "spam":
                del meal[index]
    elif meal.count("spam") == 1:
        meal.remove("spam")
    print(", ".join(meal))

print('\n'*2)

flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

separator = ", "
# outputs Daffodil | Evening Primrose | Hydrangea | Iris | Lavender | Sunflower | Tiger Lily
output = separator.join(flowers)
print(output)
