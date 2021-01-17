letters = 'abcdefghijklmnopqrstuvwxyz'
backwards = letters[25:0:-1]    # step value can be negative
print(backwards)    # zyxwvutsrqponmlkjihgfedcb

backwards = letters[25::-1] 
print(backwards)    # zyxwvutsrqponmlkjihgfedcba

backwards = letters[::-1] 
print(backwards)    # zyxwvutsrqponmlkjihgfedcba

backwards = letters[-10:-13:-1]
print(backwards)    # qpo

backwards = letters[-22::-1]
print(backwards)    # edcba

backwards = letters[:-9:-1]
print(backwards)    # zyxwvuts