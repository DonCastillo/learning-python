computer_parts = ['computer', 
                  'monitor', 
                  'keyboard', 
                  'mouse', 
                  'mouse mat'
                  ]

for part in computer_parts: # can loop through a sequence
    print(part)

print()
print(computer_parts[2])

print(computer_parts[0:3])
print(computer_parts[-1])

# replacing an element
print(computer_parts)
computer_parts[3] = 'trackball'
print(computer_parts)

# replacing multiple elements using slice
print(computer_parts[3:])
computer_parts[3:] = ["trackball"]  # don't forget to put the string into a list, or else each character
                                    # in the string will be added as if they are separate element
print(computer_parts)