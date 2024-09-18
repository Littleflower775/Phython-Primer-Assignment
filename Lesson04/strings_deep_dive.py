title = 'Code Like a Girl'
print(title[3])
print(title[-4:])

email = 'jodie@email.com'
domain_index = email.find('emai.com')
print(domain_index)

email = 'jodie@email.com'
email = email.replace('email.com', 'hotmail.com')
print(email)

a = 'abcd'
b = ''
c = '12fad'
d = 'apple orange'

print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(d.isalpha())

fruit_name = 'blueberry'
print(fruit_name[4])
print(fruit_name[:4])

print(fruit_name.find('berry'))
print(fruit_name.find('b'))

fruit_name = fruit_name.replace('blue', 'black')
print(fruit_name)
print(fruit_name.isalpha())

phrase = 'All ships rise with the tide.'
print(phrase[-3])
print(phrase[5:8])
print(phrase.find('hi'))

phrase = phrase.replace(' ', '')
print(phrase)
print(phrase.isalpha())

