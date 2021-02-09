myList = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

newString = ""
# for c in myList:
    # newString += c + ", "         # with trailing comma
newString = ", ".join(letters)   # no trailing comma
print(newString)

print()

newString = " mississippi ".join(numbers)
print(newString)
