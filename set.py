posts_ids = {151, 245, 167, 167, 151}
print(f"posts_ids {posts_ids}")  # {151, 245, 167}

my_fruits = {'apple', 'banana', 'lime'}
other_fruits = {'banana', 'apple', 'lime'}
print(f"comparison {my_fruits == other_fruits}")  # True
print(f"len {len(my_fruits)}")  # 3

# lists_set = {[1, 2], [23, 4]}  # error

# створити пустий набір
my_set = set()
print(f"my_set type {type(my_set)}")  # type <class 'set'>

photo_sizes = {'1920x1080', '800x600'}
photo_sizes.add('1920x1080')
print(f"photo_sizes {photo_sizes}")  # {'1920x1080', '800x600'}

other_sizes = {'800x600', '1024x768'}
all_sizes = photo_sizes.union(other_sizes)
print(f"all_sizes {all_sizes}")  # {'1920x1080', '800x600', '1024x768'}

int_set = {1, 23, 4}
str_set = {'1', 'abc', 'gaga'}
all_set = str_set.union(int_set)
# or
# all_set = str_set | (int_set)
print(f"all_set {all_set}")  # {'gaga', '1', 1, 4, 'abc', 23}

photo_s = {'1920x1028', '800x600'}
other_s = {'800x600', '1024x768'}
common_s = photo_s.intersection(other_s)
# or
# common_s = photo_s & other_s
print(f"common_s {common_s}")  # {'800x600'} - те що є в обох наборах

nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}
res = nums.issubset(other_nums)
print(f"res {res}")  # True - значення nums  є і в other_nums

my_sset = {'abc', 'd', 'f', 'y'}
othet_sset = {'a', 'f', 'd'}
print(f"intersection {my_sset.intersection('abcd')}")  # {'d'}
# my_sset.intersection('abcd') = my_sset.intersection(['a', 'b', 'c', 'd']) # {'d'} - передаєм все що ітерується
# my_sset.intersection('abcd') = my_sset.intersection(('a', 'b', 'c', 'd')) # {'d'} - передаєм все що ітерується

print(f"difference {my_sset.difference(othet_sset)}")  # {'y', 'abc'} - те що неспівпадає
# or
print(f"difference {my_sset - othet_sset}")  # {'y', 'abc'} - те що неспівпадає

copy_my_sset = {'abc', 'd', 'f', 'y'}
copy_othet_sset = {'a', 'f', 'd'}
copy_my_sset.discard('d')
copy_my_sset.discard('dsdfsdf')  # - нічого не буде
# copy_my_sset.remove('dsdfsdf')  # - буде помилка: KeyError: 'dsdfsdf'
print(f"discard {copy_my_sset}")  # {'y', 'abc', 'f'} - без 'd'

copy_copy_my_set = copy_my_sset.copy()
print(f"copy_copy_my_set {copy_copy_my_set}")  # {'y', 'abc', 'f'}
