import json

# JSON рядок
json_string = '{"id": "235", "brand": "Nike", "qty": 84, "status": {"isForSale": true}, "type": null}'

# Конвертація JSON рядка в словник
dictionary = json.loads(json_string)

print(dictionary)  # {'id': '235', 'brand': 'Nike', 'qty': 84, 'status': {'isForSale': True}}
print(dictionary['brand'])  # Nike
print(dictionary['status']['isForSale'])  # True
print(dictionary['type'])  # None - був null в json
print(type(dictionary))  # <class 'dict'>

json_array = '[1,true, ["abc",234], {"name":"Vasa"}]'

python_list = json.loads(json_array)
print(f"python_list {python_list}")  # [1, True, ['abc', 234], {'name': 'Vasa'}]

# ====================================================

my_dict = {
    'id': 235,
    'brand': 'Nike',
    'qty': 86,
    'status': {
        'isForSale': True
    },
    'typle': (2, 3, 4)
}

my_json = json.dumps(my_dict)
# indent=1 - к-сть пробілів
my_json_2 = json.dumps(my_dict, indent=1)  # форматує json в словник

print(f"my_json {my_json}")  # {"id": 235, "brand": "Nike", "qty": 86, "status": {"isForSale": true}}
print(type(my_json))  # <class 'str'>

# json.dumps(my_dict, indent=1)
print(f"my_json_2 {my_json_2}")
# такий json зручно записувати в файл
"""
my_json_2 {
 "id": 235,
 "brand": "Nike",
 "qty": 86,
 "status": {
  "isForSale": true
 },
 "typle": [
  2,
  3,
  4
 ]
}
"""
