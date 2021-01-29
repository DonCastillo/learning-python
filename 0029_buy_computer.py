available_parts = ['computer',
                    'monitor',
                    'keyboard',
                    'mouse',
                    'HDMI cable',
                    'dvd drive'
                    ]
current_choice = '-'
computer_parts = []
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choices)

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
            print('Removing {}'.format(current_choice))
        else:
            computer_parts.append(available_parts[int(current_choice) - 1])
            print('Adding {}'.format(current_choice))
        print('Your list now contains: {}'.format(computer_parts))
    else:
        print('Please add options from the list below')
        for number, part in enumerate(available_parts):
            print('{0}:\t{1}'.format(number + 1, part))

    current_choice = input()

print(computer_parts)