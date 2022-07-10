import random

print('Welcome to Password Generator')
print('==============================')


chars = '!"#$%&\'()*+,-./0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopq'
number = input('Amount of passwords to generate: ')
number = int(number)
print(number)

lenght = input('Your password length:')
lenght = int(lenght)

print('Here are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
print(passwords)
