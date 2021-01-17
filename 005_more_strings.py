parrot = 'Norwegian Blue'

print(parrot)

print(parrot[3])    
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

# negative indexing
# like in JS
print()
print()
print(parrot[-11])    
print(parrot[-1])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# slicing
# 0 through 6 but not including 6
# just like slice() in JS
print(parrot[0:6])      # Norweg
print(parrot[3:5])      # we
print(parrot[0:9])      # Norwegian
print(parrot[:9])       # Norweg, defaults to the start element of the sequence
print(parrot[10:14])    # Blue
print(parrot[10:])      # Blue, default to the last element of the sequence

print(parrot[:6] + parrot[6:])  # Norwegian Blue
print(parrot[:])                # Norwegian Blue

print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl

# steps
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = '9,223;372:036 854,775;807'
#print(number[1::4]) # prints all the delimiters
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values]) # [9, 223, 372, 36, 854, 775, 807]

