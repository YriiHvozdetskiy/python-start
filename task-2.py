my_list_1 = [1, 34, 53]
my_list_2 = ['d', 'g' 'g', 'fff']

marged_list = my_list_1 + my_list_2

my_list_1 += my_list_2
print(f"my_list_1 {my_list_1}")  # [1, 34, 53, 'd', 'gg', 'fff']

print(f"marged_list {marged_list}")  # [1, 34, 53, 'd', 'gg', 'fff']
print(f"__add__ {my_list_1.__add__(my_list_2)}")  # [1, 34, 53, 'd', 'gg', 'fff']
