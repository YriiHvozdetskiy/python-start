my_set = {1, 3, 234, 0}
my_set.add(777)
other_set = {1, 6756, 56, 3, 666, 777}

common_set = my_set.intersection(other_set)
my_list = list(common_set)
print(f"my_list {my_list}")
#  оригінальні набори не змінилися
