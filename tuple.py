users = (
    {
        'user_id': 1,
        'user_name': 'Alice'
    },
    {
        'user_id': 2,
        'user_name': 'Bob'
    }
)

print(f"users {users[1]['user_id']}")  # 2
users[1]['user_id'] = 100
print(f"users {users[1]['user_id']}")  # 100

internal_ids = (123, 123)
external_ids = (12, 421, 41)
all_ids = internal_ids + external_ids
print(f"all_ids {all_ids}")  # (123, 123, 12, 421, 41)

my_nums = (10, 3, 100, 23, 3, 3)
print(f"my_nums {my_nums.count(3)}")  # 3
index_one = my_nums.index(3)
print(f"my_nums {my_nums.index(3, index_one)}")  # 1

my_numbers = (10, 5, 100, 0, 5, 5)
my_list = list(my_numbers)
my_list.append(7)
my_numbers = tuple(my_list)
print(f"my_numbers {my_numbers}")  # (10, 5, 100, 0, 5, 5, 7)

my_touple_str = tuple('abc')
print(f"my_touple_str {my_touple_str}")  # ('a', 'b', 'c')

my_touple_dict = tuple({'first': 1, 'second': True})
print(f"my_touple_dict {my_touple_dict}")  # ('first', 'second')

my_lists_tuple = ([1, 23], [223, 54])
print(f"my_lists_tuple {my_lists_tuple}")  # ([1, 23], [223, 54])
print(f"my_lists_tuple[0] {my_lists_tuple[0]}")  # [1, 23]
my_lists_tuple[0].append(999)
print(f"my_lists_tuple {my_lists_tuple}")  # ([1, 23, 999], [223, 54])
