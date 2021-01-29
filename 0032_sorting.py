# sort characters

pangram = "The quick brown fox jumps over the lazy dog"
letter = sorted(pangram)
print(letter)
print()

# sort numbers

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print()

another_sorted_numbers = numbers.sort()
print(numbers)  # sort() method sort the original copy of the object
print(another_sorted_numbers)   # returns None since numbers.sort() returns nothing
print()

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)   # ignores capitalization
print(missing_letter)

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort(key=str.casefold)
print(names)