import random

print(random.random())
print(random.randint(1, 10))
print(random.choice('abcd'))
print(random.choice([1, 10, 5]))
print(random.choices([1, 23, 45, 123, 7], k=2))

my_list = [1, 23, 45, 123, 7]
random.shuffle(my_list)
print(my_list)

# генерація рандомного пароля(не використовувати)
print(''.join(random.choices('ASDASDASD012334234234', k=8)))
