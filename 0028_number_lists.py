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