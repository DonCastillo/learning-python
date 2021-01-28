string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

print("he's " "probably " "pining " "for the " "jfords") # no need to add + to concatenate

print("Hello " * 5) # prints "Hello" five times

# print("Hello " * 5 + 4) => gives an error

print("Hello " * (5 + 4))   # prints "Hello" 9 times
print("Hello " * 5 + "4")   # prints "Hello" 5 times followed by 4 string

# checks if a word contains a subword
today = "friday"
print("day" in today)       # true
print("fri" in today)       # true
print("thur" in today)      # false
print("parrot" in "fjord")  # false