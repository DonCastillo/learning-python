

while True:
    text = input("Enter a text here: ")
    if text.casefold() == "quit":
        break
    else:
        print(sorted(set(text).difference(set("aeiou"))))