print()

# opening, reading, and explicitly closing the file 
jabber = open("./data/sample.txt",mode="r")
for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')
jabber.close()

print()

# no need to explicitly close a file.
# 'with' does that
with open("./data/sample.txt", mode="r") as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end="")

print()

# print each line
with open("./data/sample.txt", "r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end="")
        line = jabber.readline()


print()

# print each line
with open("./data/sample.txt", "r") as jabber:
    lines = jabber.readlines()  # access all the file text in one go
print(lines) # prints the lines as elements in the list

for line in lines:
    print(line, end="")

print()

# print each line
with open("./data/sample.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines) # prints the lines as elements in the list

for line in lines[::-1]:
    print(line, end="")