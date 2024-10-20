def vowel_counting(name):
    name_lower = list(name.lower())

name = 'Jodie Ip'
# print(name.lower())
name_lower = name.lower()
print(name_lower)
# print(list(name_lower))

length = len(name_lower)
print(length)

vowels = ["a", "e", "i", "o", "u"]
count = 0

for i in range(len(name_lower)):
    if name_lower[i] in vowels:
        count += 1

print(count)
print(f"My full name is {name}.")
print(f"I have {count} vowels in my name.")


               