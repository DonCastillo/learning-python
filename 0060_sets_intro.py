farm_animals = {"sheep", "cow", "hen"} # sets are unordered, can set the order randomly every time the code is ran
print(farm_animals)                    # sets only contains one copy of each element

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])    # converting list to set
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")   # adding an element
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)


empty_set = set()   # this is an empty set, should be specificied explicitly
empty_set_2 = {}    # this is an empty dictionary not an array
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
# adds all the elements of the two sets together
print(even.union(squares))
print(len(even.union(squares)))
print(squares.union(even))
print("-" *40)
# gets all the intersection
# add only the common elements from each set
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

# removes all the elements in squares from even set
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

print("=" * 40)
print(sorted(even))
print(squares)
even.difference(squares)
print(sorted(even))

print("-" * 40)
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print((squares.symmetric_difference(even)))

print()
print(squares)
squares.discard(4)
squares.remove(16) # throws an error if the element does not exist
squares.discard(8) # no error, does nothing if the element does not exist
print(squares)

try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")


print("-" * 40)
even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(sorted(squares))

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of square")

print("-" * 40)

even = frozenset(range(0, 100, 2))  # just like set but is constant, cannot add or manipulate

print(even)
even.add(3)
