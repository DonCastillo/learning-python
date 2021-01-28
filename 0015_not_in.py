activity = input('What would you like to do today? ')

if 'cinema' not in activity.casefold(): # casefold ignores the case of the string. cinema and Cinema are valid
    print('But I want to go to the cinema')

if 'Don' in ['Don', 'Peter', 'Michael']:    # true
    print('okay!')
