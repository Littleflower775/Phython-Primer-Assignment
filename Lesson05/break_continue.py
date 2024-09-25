# while

#     break

#     continue

for attempt in range(5):
    if attempt%3 == 2:
        break   # terminate the loop

    print('Attempt' + str(attempt))

for attempt in range(5):
    if attempt%2 == 0:
        continue    # continue looping
    print('Attempt' + str(attempt))

for number in range(10):
    if number%5 == 4:
        break   # break here
    print('Number is ' + str(number), 'break')
print('Break loop ended!!!\n')

for number in range(10):
    if number%3 == 1:
        continue   # continue looping
    print('Number is ' + str(number), 'continue')
print('Continue loop ended!!!\n')
