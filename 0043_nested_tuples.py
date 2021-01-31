albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]

print(len(albums))

for name, artist, year in albums:       # destructutring an album tuple
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))


# same way

for album in albums:
    name, artist, year = album       # destructutring an album tuple
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

