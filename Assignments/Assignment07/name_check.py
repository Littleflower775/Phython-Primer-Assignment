def vowel_counting(name):
    name_lower = name.lower()

    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for i in range(len(name_lower)):
        if name_lower[i] in vowels:
            count += 1

    print(f"My full name is {name}.")
    print(f"I have {count} vowels in my name.")

