grades = [45, 50, 37, 60, 70, 47, 77, 68, 90]
# grades[1]

# for i in range(len(grades)):
#     print(f'I am grading studen number {i}.')
#     print(f'My current grade is {grades[i]}.')
#     grades[i] = grades[i] + 5
#     print(f'My new grade is {grades[i]}.\n') 

# [(0, 45), (1, 50), (2, 37).....]

# for i, grade in enumerate(grades):
#     print(i)
#     print(grade)

for i in range(10):
    print(i)
    if i == 5:
        break   # exit when matches the condition
print('Break loop finished!')

for i in range(10):
    if i%3 == 0:
        continue # skip the ones matching the condition
    print(i)
print('Continue loop finished!')