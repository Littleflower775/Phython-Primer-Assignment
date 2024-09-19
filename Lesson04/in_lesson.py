class_grades = [85, 74, 90, 80, 63.5, 92, 85]

quiz_answers = [True, True, False, False]

colours = ['blue', 'green', 'purple', 'orange']
print(colours == colours[:])
del colours[1]
print(colours)

colour = colours.pop()
print(colour)

ratings = [2, 4, 1, 4, 2, 4, 5, 3, 1, 5, 2]
number = 3
count = ratings.count(number)
print(f'We have {count} {number}s in our ratings')

name = 'Jodie'
print(' '.join(name))

print(name.split())
print(list(name))

full_name = "Jodie Ip"
print(full_name.split())

print(' '.join(name))