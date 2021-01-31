for index, character in enumerate('abcdefgh'):
    print(index, character)

    # outputs
    # 0 a
    # 1 b
    # 2 c
    # 3 d
    # 4 e
    # 5 f
    # 6 g
    # 7 h

print()
print()

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)