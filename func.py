from datetime import datetime


def my_fn():
    pass  # коли ще незнаєм що буде в функції


print(my_fn())


def my_fn_2(a, b):
    print(f"id(a) {id(a)}")  # id(a) 4359433872


one = 10
print(f"one {id(one)}")  # one 4359433872
two = 5

my_fn_2(one, two)


#  task
def merge_lists_to_dict(keys, values):
    merged_dict = dict(zip(keys, values))
    return merged_dict


print(f"merge_lists_to_dict {merge_lists_to_dict(['a', 'b', 'c'], [10, 23, 45])}")
# {'a': 10, 'b': 23, 'c': 45}

print(f"merge_lists_to_dict {merge_lists_to_dict(['abc'], [{}, True, 100])}")
# {'abc': {}}

print(f"merge_lists_to_dict {merge_lists_to_dict([12], [True, 100])}")
# {12: True}

res = merge_lists_to_dict([True], [True, 100])
print(f"res {res}")  # {True: True}
print(res[True])  # True


#  tuple argum
def sum_nums(*args):
    print(args)  # (2,3,7)
    print(type(args))  # class 'tuple

    print(args[0])  # 2
    return sum(args)


print(sum_nums(2, 3, 7))  # 12


# var #1
def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info(posts_qty=25, name='Bogdan')
print(f"info {info}")  # Bogdan wrote 25 posts


# var #2 dict argum
def get_posts_info(**person):
    print(f"**person {person}")  # {'posts_qty': 25, 'name': 'Bogdan', 'id': 1234}
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info


info = get_posts_info(posts_qty=25, name='Bogdan', id=1234)
print(f"info {info}")  # Bogdan wrote 25 posts


# task 2
def update_car_info(**car):
    car['is_available'] = True
    return car


fn_car = update_car_info(brand='Audi', price=10_000)
print(f"fn_car {fn_car}")


def mult_by_factor(value, multiplier=1):
    return value * multiplier


print(mult_by_factor(10, 2))  # 20
print(mult_by_factor(5))  # 5

'''
%Y: Рік із чотирма цифрами (наприклад, 2023).
%y: Рік з двома цифрами (наприклад, 23 для 2023 року).
%m: Місяць як число з двома цифрами (01-12).
%B: Повне ім'я місяця (наприклад, January).
%b: Скорочене ім'я місяця (наприклад, Jan).
%d: День місяця як число з двома цифрами (01-31).
%A: Повне ім'я дня тижня (наприклад, Monday).
%a: Скорочене ім'я дня тижня (наприклад, Mon).
%H: Година (24-годинний формат) як число з двома цифрами (00-23).
%I: Година (12-годинний формат) як число з двома цифрами (01-12).
%p: AM або PM.
%M: Мінути як число з двома цифрами (00-59).
%S: Секунди як число з двома цифрами (00-59).
%f: Мікросекунди як число з шістьма цифрами (000000-999999).
%Z: Ім'я часової зони (наприклад, UTC, GMT).
%j: День року як число з трьома цифрами (001-366).
'''


def get_weekday():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['creared_on_weekday'] = weekday

    return post_copy


initial_post = {
    'id': 234,
    'author': 'Bogdan'
}

post_with_weekday = create_new_post(initial_post)
# {'id': 234, 'author': 'Bogdan', 'creared_on_weekday': '2024-01-20 20:10:47'}
print(f"post_with_weekday {post_with_weekday}")


def print_number_info(num):
    """
    Print whether bumber is even or add

    Args: num(int):Number to be evaluated
    :param num:
    :return:same number
    """
    if (num % 2) == 0:
        print('num is even')
    else:
        print('num is add')

    return num


print_number_info(20)


def mult(a, b): return a * b


print(mult(2, 4))  # 8


def func_with_kwargs(*args, **kwargs):
    print(f"kwargs {kwargs}")  # {'name': 'John', 'age': 30}
    print(f"args {args}")  # ('John', 30)

    # Ітерація через kwargs для отримання ключів та значень
    for key, value in kwargs.items():
        # Ключ: name, Значення: John
        # Ключ: age, Значення: 30
        print(f"Ключ: {key}, Значення: {value}")

    # Ітерація args
    for elem in args:
        # elem John
        # elem 30
        print(f"elem {elem}")


# Виклик функції з декількома іменованими аргументами
func_with_kwargs(name="John", age=30)
func_with_kwargs("John", 30)
