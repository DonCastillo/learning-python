number = '9,223;372:036 854,775;807'
separators = ''

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)   # prints    ,;: ,;

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values]) # [9, 223, 372, 36, 854, 775, 807]

print(sum([1, 2, 3, 4, 5, 6]))      # using built-in sum function


# print all the uppercase letter in the quote variable
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

capital = ''
for char in quote:
    if char.isupper():
        capital += char

print(capital)  # ASMEWPOIRFWSPHR