splitSpring = 'This string has been \nsplit over\nseveral\nline'
print(splitSpring)

tabbedString = '1\t2\t3\t4\t5'
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# can have multiple lines when enclosed with triple quotes
# This string has been
# split over
# several
# lines
anotherSplitSpring = """This string has been 
split over 
several 
lines"""

print(anotherSplitSpring)

# escapes the new line
# This string has been split over several lines
anotherSplitSpring = """This string has been \
split over \
several \
lines"""

print(anotherSplitSpring)

print("C:\\Users\\donqc\\notes.txt");
print(r"C:\Users\donqc\notes.txt")  # raw string