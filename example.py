my_cat = 'Michelb'
int_number = 12
my_comment = 'this is my short comment'

hello = 'Hello'
world = 'World'
greeting = hello + ' ' + world
print(greeting)  # Hello World


def say_vode(voice):
    print(f"voice {voice}")


copy_my_cat = my_cat

print(f"id {id(my_cat)}")  # 4311079728
print(f"id copy {id(copy_my_cat)}")  # 4311079728

print(f"type {type(my_cat)}")
print(f"type {type(say_vode)}")
print(f"type {type(id)}")
print(f"type {type(type)}")

"""
this is
    a vary long string
"""
# ======== str ==========
print(f"len {len(my_cat)}")  # lenght - 7
print(f" {my_cat[3:5]}")  # he - діапазон в рядку
print(f" {my_cat[3:]}")  # hehelb - від 3 індексу до кінця
print(f"[:2] {my_cat[:2]}")  # виведе перших два символи рядку - Mi
print(f"[:] {my_cat[:]}")  # виведе всесь рядок

print(f" {my_comment.replace('short', 'long')}")  # повертає нову змінесу строку
print(f"my_comment {my_comment}")  # не міняє оригінального строку
print(f"count {my_comment.count('is')}")  # 2 - вертає скільки раз повторяється 'is'

is_str = '10'
any_value = int(is_str)
print(f"any {type(any_value)}")

one_million = 1_000_000
print(f"one_illion {one_million} ")  # 1000000

avarage_price = 17.32
price = int(avarage_price)  # 17

str_tempr = 13
print(f" {float(str_tempr)}")  # 13.0

avarage_price = 17.55
print(f"round {round(avarage_price)}")  # 18

complex_a = 10 + 7j
complex_b = 3 + 3j
print(f"compex + {complex_a + complex_b}")  # 13+10j
print(f"compex * {complex_a * complex_b}")  # 9+51j = (10+7j)(3+3j) = 30 + 30j + 21j + 21j^2

print(f"bool[] {[1, 2, 3] == [1, 2, 3]}")  # True
print(f"bool[]=[] {[] == []}")  # True
print(f"bool {bool({})}")  # False

print(f"list {list()}")  # []
print(f"set {set()}")  # set()
# print(f" {5 + '10'}")  # unsupported operand type(s) for +: 'int' and 'str'

print(f" {5 + int('101')}")  # 106
print(f"fload+ {5 + 4.5}")  # 9.5
print(f"boole+ {True + 7}")  # 8
print(f"boole- {7 - True}")  # 6

int_num = 5
float_num = 4.5
str_val = 'abc'
print(f" {int_num + float_num}")  # 9.5
print(f" {int_num.__add__(float_num)}")  # NotImplemented
print(f" {int_num.__mul__(int_num)}")  # 25
print(f"* {int_num * str_val}")  # abcabcabcabcabc
print(f"/ {float_num / 5}")  # 0.9

user_inputs = ['vova', True, 10]
del user_inputs[0]
print(f"userinputs {user_inputs}")  # [True, 10]

users = [
    {
        'user_id': 12,
        'user_name': 'Alice'
    },
    {
        'user_id': 13,
        'user_name': 'Bob'
    }
]
print(f"users {users[1]['user_name']}")  # Bob

happy_names = ['Igor']
happy_names.append('Dima')  # append = push: ['Igor', 'Dima']

return_delete_element = happy_names.pop()  # delete last elemet
print(f"return {return_delete_element}")  # Dima

print(f" {happy_names}")  # ['Igor']

posts_ids = [245, 152, 762, 167]
posts_ids.sort()
print(f"sort() {posts_ids}")  # [152, 167, 245, 762]

posts_ids.sort(reverse=True)
print(f"sort(revers) {posts_ids}")  # [762, 245, 167, 152]

greeting = 'Hello from Python'
greeting_letters = list(greeting)
print(f"greeting_letters {greeting_letters}")
'''
['H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm', ' ', 'P', 'y', 't', 'h', 'o', 'n']
'''

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)
print(f"my_dict_keys {my_dict_keys}")  # ['a', 'b']

ratings = [2.5, 5.0, 4.4, 3.7, -1]

print(f"min {min(ratings)}")  # -1
print(f"max {max(ratings)}")  # 5.0
print(f"sum {sum(ratings)}")  # 14.600000000000001
print(f"{sum(ratings) / len(ratings)}")  # 2.9200000000000004

my_ratings = [2.5, 4, 5]
my_names = ['Vika', 'Dima', 'Shasa']
all_values = my_names + my_ratings  # під капотом використовується __add__
print(f"all_values {all_values}")  # новий список ['Vika', 'Dima', 'Shasa', 2.5, 4, 5]

first_two_ratings = ratings[:2]
print(f"first_two_ratings {first_two_ratings}")  # 2.5, 5.0

last_two_ratings = ratings[-2:]
print(f"last_two_ratings {last_two_ratings}")  # [3.7, -1]

copy_ratings = ratings[:]  # ratings - [2.5, 5.0, 4.4, 3.7, -1]
print(f"copy_ratings {copy_ratings}")  # [2.5, 5.0, 4.4, 3.7, -1]

my_cars = ['BMW', 'Audi']
copy_cars_1 = my_cars[:]  # 1
copy_cars_2 = my_cars.copy()  # 2
copy_cars_3 = list(my_cars)  # 3
print(f"copy_cars {copy_cars_3}")  # ['BMW', 'Audi']
my_cars.insert(1, 'Toyota')
print(f"my_cars {my_cars}")  # перед __index вставиться значення ['BMW', 'Toyota', 'Audi']

sort_copy_rating = ratings.copy().sort()
print(f"sort_copy_rating {sort_copy_rating}")  # None
print(f"sorted(ratings.copy()) {sorted(ratings.copy())}")  # [-1, 2.5, 3.7, 4.4, 5.0]

my_nums = [10, 23, 42, 42, 4]
my_nums.clear()
print(f"my_nums {my_nums}")  # [] - користо коли використовуєм список як чергу
my_nums.extend('a')
print(f"my_nums {my_nums}")  # [10, 23, 42, 42, 4, 'a']

# Припустимо, є два словники
dict1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
dict2 = {'c': 3, 'd': 4, 'b': {'z': 30}}

# Розпакування та об'єднання словників
combined_dict = {**dict1, **dict2}
print(combined_dict)  # {'a': 1, 'b': {'z': 30}, 'c': 3, 'd': 4}

# Об'єднання вкладених словників
combined_dict_2 = {**dict1, **dict2, 'b': {**dict1['b'], **dict2['b']}}
print(f"combined_dict_2 {combined_dict_2}")  # {'a': 1, 'b': {'x': 10, 'y': 20, 'z': 30}, 'c': 3, 'd': 4}

my_dict_del = {'age': 32, 'name': 'Dima'}
my_list = [1, 2]

del my_list[0]
# or
# my_list.__delitem__(0)
my_dict_del.__delitem__('age')
print(f"my_list del {my_list}")  # [2]
print(f"my_dict_del {my_dict_del}")  # {'name': 'Dima'}

#  розпаковування деструктивізація: списків, кортежів

my_fruits = ['apple', 'banana', 'lime']

my_apple, my_banana, my_lime = my_fruits
print(f"my_apple {my_apple}")  # apple
print(f"my_banana {my_banana}")  # banana
print(f"my_lime {my_lime}")  # lime

my_apple_new, *remaining_fruits = my_fruits
print(f"my_apple_new {my_apple_new}")  # apple
print(f"remaining_fruits {remaining_fruits}")  # ['banana', 'lime']

#  розпаковування словаря в аргументи
user_profile = {
    'name': 'Bogdan',
    'comments_qty': 23
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"


# буде помилка якщо в словнику user_info буде ще якісь властивості
print(f"user_info {user_info(**user_profile)}")

# розпаковування списка list, tuple в позиційні аргументи

user_data = ('Bogdan', 23)


# user_data = ['Bogdan', 23]


# можна зібрати лишні аргументи в *args
def user_info(name, comments_qty):
    if not comments_qty:
        return f"'{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(f"user_info/data {user_info(*user_data)}")  # Bogdan has 23 comments

#  ========== if ==========
num_one = 10
num_two = 5.3
'''
Вираз isinstance(num_one, int) у Python використовується для перевірки,
чи змінна num_one є екземпляром (тобто, чи належить до типу) int,
що означає ціле число.
'''

if (num_one > 0 and
        num_two > 0 and
        isinstance(num_one, int) and
        isinstance(num_two, int)):
    print('Both numbers are ints and positive')

my_number = 21.5
if type(my_number) is int:
    print(my_number, "is integer")
else:
    print(my_number, "is not an integer")  # 21.5 is not an integer

my_number = -10

if my_number > 0:
    print(my_number, "is positive number")
elif my_number < 0:
    print(my_number, "is negative number")  # -10 is negative number
else:
    print(my_number, "is zero")


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "Один из аргументов не целое число"

    if a >= b:
        return f"{a} больше или равно {b}"
    return f"{a} меньше {b}"


print(nums_info(True, 10))  # Один из аргументов не целое число
print(nums_info(10, 2))  # 10 больше или равно 2
print(nums_info(4, 15))  # 4 меньше 15

# ternarnik
product_qty = 10
print('in stok' if product_qty > 0 else 'out of stock')  # in stok

temp = +24
weather = 'hot' if temp > 18 else 'cold'
print(f"weather {weather}")  # hot

my_img = ('1920', '1080')
print(f"my_img {my_img[0]}x{my_img[1]}") if len(my_img) == 2 else print('Incorect img')  # 1920x1080

# or


info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else 'Incorect img'  # 1920x1080
print(f"info {info}")  # 1920x1080

# if else

if len(my_img) == 2:
    print(f"my_img if {my_img[0]}x{my_img[1]}")  # 1920x1080
else:
    print('Incorect img')

# task
my_str = 'xaxaxa what is going now?'

print('String is long') if len(my_str) > 79 else print('String is short')  # String is short


# task

def rute_info(route):
    speed = route.get('speed')
    time = route.get('time')
    distance = route.get('distance')

    if distance and (not speed and not time):
        if isinstance(distance, int):
            return f"Distance to your destinations is {distance}"

    if speed and time:
        int_speed = int(speed)
        int_time = int(time)
        return f"Distance to your destinations is {int_speed * int_time}"

    return 'No disatance info is available'


print(f"rute_info {rute_info({'distance': 10.0})}")  # No disatance infi as available
print(f"rute_info {rute_info({'distance': 10, 'speed': 100, 'time': 25})}")  # Distance to your destinations is 2500
print(f"rute_info {rute_info({'distance': 24})}")  # Distance to your destinations is 24


# or


def route_info_v2(route):
    if ('distance' in route) and (isinstance(route['distance'], int)):
        return f"Distance to your destintion is {route['distance']}"

    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"

    return 'No distance info is available'


print(route_info_v2({'distance': 15}))  # Distance to your destintion is 15
print(route_info_v2({'speed': 20, 'time': 3}))  # Distance to your destination is 60
print(route_info_v2({'my_speed': 13}))  # No distance info is available
