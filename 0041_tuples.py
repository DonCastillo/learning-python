t = ("a", "b", "c") # => this is a tuple. Always enclosed within parentheses
print(t)

name = "Tim"
age = 10
print(name, age, "Python", 2020)
print((name, age, "Python", 2020))  # printing a tuple literal

print()
print()

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984


print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Mater of Puppets"   # error! tuples are immutable while a list is mutable
# tuples protect the integrity of the data
metallica2 = list(metallica)    # converts tuple to list
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)   # no error! lists are mutable

print()
print()

# unpack the list of tuples

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
name, length, width, height, price = table
print(length * width)