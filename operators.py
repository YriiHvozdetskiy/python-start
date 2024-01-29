my_car = {
    'brand': 'BMW',
    'price': 100_000
}

print('brand' in my_car)  # True
print('year' in my_car)  # False
print('year' not in my_car)  # True

'''
Пріоритет оператора is є вищим,
ніж пріоритет логічних операторів (як and, or, not), 
але нижчим, ніж пріоритет операторів порівняння (як ==, !=, <, >, <=, >=).
Таким чином, is стоїть на одному рівні з операторами in, not in, <, <=, >, >=, !=, == в порядку пріоритету.
'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, оскільки b є тим же самим об'єктом, що й a
print(a is c)  # False, оскільки c є копією a, але не тим самим об'єктом

f = 2
j = 2
print(f"f is j {f is j}")  # True

k = 4
y = '4'
print(f"k is y {k is y}")  # False

# task

set_one = {10, 'abc', 50, True}
set_two = {'abc', 10, 50, True}
print(set_one == set_two)  # True
# or
print(f"__eq__ {set_one.__eq__(set_two)}")  # True
print(set_one is set_two)  # False
print('abc' in set_two)  # True - 'abc' є в наборі
print(5 not in set_two)  # True - 5 немає в наборі

d = '3'
c = '3'
print(d in c)  # True

# ======= not, and, or =======

not 10  # False
not 0  # True
not 'abc'  # False
not ''  # True
not True  # False
not None  # True

my_list = [1, 2]
my_list and print('list in not empty')

my_dict_1 = {'name': 'Vasa', 'age': 23}
my_dict_2 = {'name': 'Vasa', 'age': 23}
my_dict_2 == my_dict_1 and print('dict is ecval')
