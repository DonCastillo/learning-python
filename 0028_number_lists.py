even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]


print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()

print(len(even))
print(len(odd))

print()
print('mississippi'.count('issi'))  # count returns the number of occurences group of letters in the word


even.extend(odd)    # add contents of odd to even
print(even)
another_even = even
print(another_even)
even.sort() # sort, does not create a copy of the list. it rearranges the original list
print(even)
even.sort(reverse=True) 
print(even)
print(another_even)


empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = list("432985617")  # creates a list from any iterable
print(digits)

more_numbers = list(numbers)
# more_numbers = numbers[:]       # copies the list of numbers
# more_numbers = numbers.copy()   # copies the list of numbers
print(more_numbers)
print(numbers is more_numbers)  # do they refer to the same copy of object
print(numbers == more_numbers)  # do they have the same value
