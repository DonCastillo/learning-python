data= [4,5,104,105,110,120, 130, 130, 150, 160, 170, 183,185,187, 188, 191, 350, 360]

# del data[0:2]
# print(data)

# del data[-2:]
# print(data)

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]

# print(data)

# process the low values in the list
# only works in a sorted list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)


# process the high values in the list
# only works in a sorted list
# no need to process values in between, start iterating from the end of the list

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # We hace the index of the last item to keep
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break

print(start)
del data[start:]
print(data)


# for index, value in enumerate(data):
#     if value > max_valid:
#         stop = index
#         break
# print(stop)
# del data[stop:]
# print(data)