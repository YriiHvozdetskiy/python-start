my_list = [1, 3, 'abc', True, 5]

del my_list[2]
# or
# my_list.pop(2)

print(f"my_list {len(my_list)}")

my_list.sort()
print(f"sort_my_list {my_list}")

new_list = [2, 'fff']
# my_list.append(10)

my_list.extend(new_list)
# my_list.extend('new_list')
# my_list += new_list
# my_list.insert(2, "new_item")

print(f"my_list {my_list}")
