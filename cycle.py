my_list = [True, 10, 'abc', {}]
for elem in my_list:
    print(f"my_list {elem}")

my_tuple = ('1920x1080', True, 27)
for elem in my_tuple:
    print(f"my_tuple {elem}")

# dict
my_dict = {
    'x': 10,
    'y': True,
    'z': 'abc'
}
for key in my_dict:
    print(f"my_dict {my_dict[key]}")

# or 1

# item - буде tuple, так як items() вертає tuple
for item in my_dict.items():
    key, value = item  # розпаковка tuple
    print(f"key, value {key, value}")

# or 2

for key, value in my_dict.items():
    print(f"key,value {key, value}")

#  el - буде в глобальній зоні видимості й там буде остання зная з циклу
for el in [1, 'abc', True]:
    print(f"el {el}")

print(f"el {el}")  # True

# range

# можна використовуватися для підключення до сервера (є 5 спроб)
for num in range(5):
    print(num)


# task 1

def dict_to_list(obj):
    result = []
    for key_, value_ in obj.items():
        # Перевірка, чи значення є цілим числом
        if isinstance(value_, int):
            value_ *= 2
        result.append((key_, value_))
    return result


# [('status', 'evaible'), ('name', 'Bober'), ('age', 36), ('weight', 187.8)]
print(f"dict_to_list {dict_to_list({'status': 'evaible', 'name': 'Bober', 'age': 18, 'weight': 187.8})}")


# task 2

def filter_list(_list, _type):
    retult = []
    for li in _list:
        # True конвертується в 1, тому дод ще перевірку
        if isinstance(li, _type) and not isinstance(li, bool):
            retult.append(li)
    return retult


print(f"filter_list {filter_list(['a', 'b', 1, True, [], {}], int)}")  # [1]
print(f"filter_list {filter_list([35, True, 'abc', 10], str)}")  # ['abc']


# filter

def _filter_list(list_to_filter, value_type):
    # def check_element_type(element):
    #     return isinstance(element, value_type)
    #
    # return list(filter(check_element_type, list_to_filter))

    # or

    # return list(filter(lambda element: isinstance(element, value_type), list_to_filter))

    # or

    return list(
        filter(lambda element: isinstance(element, value_type) and not isinstance(element, bool), list_to_filter))


print(f"_filter_list {_filter_list([1, 10, 'abc', 5.51], int)}")  # [1, 10]
print(f"_filter_list {_filter_list([1, 10, 'abc', 5.51, False], int)}")  # [1, 10, False]

i = 10
while i < 50:
    print(i)
    i += 10

import random

random_num = random.randint(1, 5)

# while True:
#     num = int(input("Guess the number from 1 to 5:"))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congratulations!", random_num)
#     break

# task

while False:  # True
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    print(f"/ {num_1 / num_2}")

    continue_message = input('Continue?: (yes/no)')

    if continue_message != 'no':
        print("lets gooo")
        continue
    print('Stop')
    break

# or

while False:  # True
    try:
        num_one = float(input("Please enter number one: "))
        num_two = float(input("Please enter number two: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    print(num_one / num_two)

    answer = input("Do you want to continue? (yes/no): ")
    if answer == 'no':
        break

#  short for in

all_nums = [-3, 1, 0, 10 - 20, 5]

absolute_nums = [abs(num) for num in all_nums]
print(f"absolute_nums {absolute_nums}")  # [3, 1, 0, 10, 5]
print(f"all_nums {all_nums}")  # [-3, 1, 0, -10, 5]

positive_nums = [num for num in all_nums if num > 0]
print(f"positive_nums {positive_nums}")  # [1, 5]

my_set = {1, 10, 15}
new_set = {val * val for val in my_set}
print(f"new_set {new_set}")  # {1, 100, 225}

scores = {
    'a': 10,
    'b': 7,
    'm': 14,
}
new_scores_dict = {key: value * 10 for key, value in scores.items()}  # made dict
print(f"new_scores_dict {new_scores_dict}")  # {'a': 100, 'b': 70, 'm': 140}

new_scores_set = {value * 10 for key, value in scores.items()}  # made set
print(f"new_scores_set {new_scores_set}")  # {140, 100, 70}

# made dict for list

scores_list = [10, 7, 14]
scores_dict = {index: value for index, value in enumerate(scores_list)}
print(f"scores_dict {scores_dict}")  # 0: 10, 1: 7, 2: 14}

# task 1

my_str = {
    'name': 'Vasa',
    'last_name': 'Pupkin'
}

upper_dict = {key: value.upper() for key, value in my_str.items()}
print(f"upper_dict {upper_dict}")  # {'name': 'VASA', 'last_name': 'PUPKIN'}

# task 2

my_list_str = ['vognuk', 'MiIIIelb', 'abc', 'a', 'op']

len_str_3 = [elem for elem in my_list_str if elem.__len__() >= 3]
print(f"len_str_3 {len_str_3}")  # ['vognuk', 'MiIIIelb', 'abc']

# геніратори

nums = [3, 4, 10]

a = ()
# <class 'tuple'>
print(f"a {type(a)}")

generator = (num * num for num in nums)

# <class 'generator'>
print(f"generator {type(generator)}")

squares = tuple(generator)
# <class 'tuple'>
print(f"squares {type(squares)}")
