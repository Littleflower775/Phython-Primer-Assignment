user_word = input('Enter your word: ')
lowercase_user_word = user_word.lower()
letters_in_word = list(lowercase_user_word)
# print(letters_in_word)

letters_in_word.reverse()
# print(letters_in_word)

string_from_list = "".join(letters_in_word)
# print(string_from_list)

is_palindrome = lowercase_user_word == string_from_list
print(f'Is this word palindome?:', is_palindrome)
