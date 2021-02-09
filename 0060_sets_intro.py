farm_animals = {"sheep", "cow", "hen"} # sets are unordered, can set the order randomly every time the code is ran
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)


empty_set = set()
empty_set_2 = {}
empty_set.add("a")
# empty_set_2.add("a")

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# gets all the union
print(even.union(squares))
print(len(even.union(squares)))
print(squares.union(even))
print("-" *40)
# gets all the intersection
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)
# set operation
print("-" * 40)
even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))
