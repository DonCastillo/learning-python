split_string = 'This string has been \nsplit over\nseveral\nline'
print(split_string)

tabbed_string = '1\t2\t3\t4\t5'
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# can have multiple lines when enclosed with triple quotes
# This string has been
# split over
# several
# lines
another_split_string = """This string has been 
split over 
several 
lines"""

print(another_split_string)

# escapes the new line
# This string has been split over several lines
another_split_string = """This string has been \
split over \
several \
lines"""

print(another_split_string)

print("C:\\Users\\donqc\\notes.txt");
print(r"C:\Users\donqc\notes.txt")  # raw string