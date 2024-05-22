my_motorbike = {
    'brand': 'Ducati',
    ' price': 25_000,
    'engine_vol': 1.2,
}

print(f"my_motorbike {my_motorbike[' price']}")  # 25000
other_motorbike = {
    'brand': 'Ducati',
    'price': 25_000,
    'engine_vol': 1.2,
}
print(f"= {my_motorbike == other_motorbike}")  # False

name = 'Dima'
name_dict = {
    name: 'Sexy',
    'age': 13
}

name_dict_2 = {
    'Dima': 'Sexy',
    'age': 13
}
print(f"name_dict {name_dict[name]}")  # Sexy

name_dict_2['Dima'] = 'super'
print(name_dict_2)  # {'Dima': 'super', 'age': 13}
del name_dict_2['age']
print(name_dict_2)  # {'Dima': 'super'}

poroda = 'British'
my_cat = {
    poroda
}
my_new_cat = {}
print(f"my_cat {my_cat}")
print(f"len {len(my_cat)}")  # 1
print(f"len {len(my_new_cat)}")  # 0
# print(f"my_new_cat {my_new_cat['name']}")  # KeyError: 'name'
print(f"get {my_new_cat.get('name')}")  # None
print(f"get {my_new_cat.get('name', 'Michelb')}")  # Michelb - повертає значення за замовчуванням

my_disk = {'price': 10_000, 'model': 'Galaxy'}
my_disk['brand'] = 'Samsung'
print(f"pop {my_disk.pop('price')}")  # 10000
print(f"my_disk {my_disk}")  # {'model': 'Galaxy', 'brand': 'Samsung'}
print(f"items {my_disk.items()}")  # dict_items([('model', 'Galaxy'), ('brand', 'Samsung')]) - вертає кортеж

print(f"my_disk {my_disk.keys()}")  # dict_keys(['model', 'brand'])
print(f"my_disk list {list(my_disk.keys())}")  # ['model', 'brand']

print(f"copy {my_disk.copy()}")  # {'model': 'Galaxy', 'brand': 'Samsung'}
copy_my_disk = {**my_disk}
print(f"copy_my_disk {copy_my_disk}")  # {'model': 'Galaxy', 'brand': 'Samsung'}

my_list = [['first', 0], ['second', 1]]
my_tuple = [('first', 0), ('second', 1)]
print(f"my_dict {dict(my_list)}")  # {'first': 0, 'second': 1}
print(f"my_tuple {dict(my_tuple)}")  # {'first': 0, 'second': 1}

# ===== task ==========
# Створюємо порожній словник
# user_data = {}
#
# # Виконуємо цикл 6 разів
# for _ in range(6):
#     # Запросити користувача ввести ключ
#     key = input("Будь ласка, введіть ключ: ")
#     # Запросити користувача ввести значення
#     value = input("Будь ласка, введіть значення для цього ключа: ")
#     # Додати або оновити пару ключ-значення у словнику
#     user_data[key] = value
#
# # Виводимо зібрані дані
# print("Зібраний словник даних:", user_data)
# ===== task ==========

button = {
    'width': 200,
    'text': 'Buy'
}

red_button = {
    **button,
    'color': 'red'
}

print(f"red_button {red_button}")  # {'width': 200, 'text': 'Buy', 'color': 'red'}
print(f"button {button}")  # {'width': 200, 'text': 'Buy'}

button_info = {
    'text': 'Buy'
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}

button_all = {
    **button_info,
    **button_style
}
# or
button_all_2 = button_info | button_style

print(f"button_all {button_all}")  # {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}
print(f"button_all_2 {button_all_2}")  # {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}
