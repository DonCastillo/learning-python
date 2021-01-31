a = b = c = d = e = f = 42
print(c)

# like desctructuing an array in JS
x, y, z = 1, 2, 76  # => this is a tuple

print(x)
print(y)
print(z)

print("Unpackign a tuple")

data = 1, 2, 76 # data represents a tuple
x, y, z = data  # again destructuring

print(x)
print(y)
print(z)


print("Unpacking a list")

data_list = [12, 13, 14]    # data destructuing also works in list
# data_list.append(15)    # gives an error. too many values in data_list

p, q, r = data_list
print(p)
print(q)
print(r)