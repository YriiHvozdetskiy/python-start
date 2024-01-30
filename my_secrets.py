# генерація паролів
import secrets
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
print('')

all_chars = string.ascii_letters + string.digits + string.punctuation
print(''.join(secrets.choice(all_chars) for i in range(20)))
