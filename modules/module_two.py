# 1 імпорті всього модуля
# import module_one

# 2 переіменували імпортований модуль з module_one на one
# import module_one as one

# 3 імпортуємо з модуля тільки потрібні ф-ції, зміні ітд
# from module_one import print_sum, my_name

# 4 переіменовуєм ф-ції, зміні ітд при імпорті
# from module_one import print_sum as my_sum, my_name as name

# 5 імпорт всіх ф-цій, зміних ітд
from module_one import *

# =========================================================

# 1
# print(dir(module_one))  # 'my_name', 'print_sum'
# module_one.print_sum(5, 2)  # 7

# 2
# print(dir(one))  # 'my_name', 'print_sum'
# one.print_sum(2, 3)  # 5

# 3
# print_sum(8, 4)  # 12
# print(f"my_name {my_name}")  # Bogdan

# 4
# my_sum(12, 1)  # 13
# print(f"name {name}")  # Bogdan

# 5
print_sum(1, 2)  # 3
print(f"my_name {my_name}")  # Bogdan
