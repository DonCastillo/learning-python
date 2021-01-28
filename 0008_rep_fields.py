age = 24
name = "Tim"
# str() parses int to string
print("My age is " + str(age) + " years")
# replaces {0} to age
print("My age is {0} years".format(age))
# using printf version
print("My age is %d years old" % age)
# just like string template literal in JS. No need to use .format(value) function
print(name + f"'s age is {age} years old")
# should always starts with {0}
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
     .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
    
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct, and Dec".format(31))

# {0} => 28
# {1} => 30
# {2} => 31
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
     .format(28, 30, 31))

print()
print("""Jan: {2}, 
Feb: {0} 
Mar: {2} 
Apr: {1} 
May: {2} 
Jun: {1} 
Jul: {2} 
Aug: {2} 
Sep: {1} 
Oct: {2} 
Nov: {1} 
Dec: {2}""".format(28, 30, 31))