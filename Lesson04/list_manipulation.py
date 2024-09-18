pets = ['ant', 'bird', 'cat', 'dog']
pets[1] = 'snake'
print(pets)

pets = ['ant', 'bird', 'cat', 'dog']
pets[1:3] = ['tiger', 'lion', 'jaguar']
print(pets)

pets = ['ant', 'bird', 'cat', 'dog']
farm_animals = ['goat', 'sheep']

animals = pets + farm_animals
print(animals)

pets.extend(farm_animals)
print(pets)

pets.append('emu')
print(pets)

pets = ['ant', 'bird', 'cat', 'dog']
pets.insert(2, 'pig')
print(pets)

pets = ['ant', 'bird', 'cat', 'dog']
pets.remove('cat')
print(pets)

pets = ['ant', 'bird', 'cat', 'dog']
pet = pets.pop(1)
print(pet)
print(pets)

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[2] = 'Code'
print(numbers)

numbers[1:4] = [12.3, 45.12, 123.21, True]
print(numbers)

words = ['hi', 'Python', 'Code', 'fun']
print(numbers + words)

words.append('C#')
print(words)

words.insert(1, 'Web Dev')
print(words)

words.remove('hi')
print(words)

word = words.pop()
print(word)
print(words)

del words[1:3]
print(words)

artists = ['Picasso', 'Matisse', 'Kusama']
artists.insert(-3,'Khalo')
print(artists)

del artists[2]
print(artists)

artist = artists.pop()
print(artist)
print(artists)


