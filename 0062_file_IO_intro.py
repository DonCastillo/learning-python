print()

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