cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]


# writing to file
with open('./data/cities.txt', mode='w') as city_file:
    for city in cities:
        print(city, file=city_file)

# reading to file
cities_2 = []
with open('./data/cities.txt', mode='r') as city_file:
    for city in city_file:
        cities_2.append(city.strip("\n")) # strip not only removes the leading and trailing spaces, it also removes new line chars

print(cities_2)
for city in cities:
    print(city, end="")


print()

imelda = "More Mayhem", "Imelda MAy", "2011", ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("./data/imelda3.txt", mode="w") as imelda_file:
    print(imelda, file=imelda_file)

print()

with open("./data/imelda3.txt", mode="r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents) # evaluates the format of string in the file and determines its data structure

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
