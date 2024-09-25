#score_string = input('What is your score?: ')
# score_int = int(score_string)

# if score_int > 20:
#     print('Congratulations!')
# elif score_int > 18:
#     print('Not bad!')
# elif score_int > 16:
#     print('Almost there!')
# else:
#     print('Try again')

# year = 2024
# year_of_birth = input('Enter year of birth: ')

# age = year - int(year_of_birth)

# if age > 17:
#     print('You pay full price.')
# else:
#     print('You can travel for free!')

password = input('Enter your password: ')

if len(password) < 6:
    print('Password is too short.')
elif len(password) > 18:
    print('Password is too long.')
else:
    print('Password is long enough.')

