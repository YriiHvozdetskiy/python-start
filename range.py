my_range = range(10, 20, 3)
print(f"my_range {my_range}")  # range(10, 20, 3)
print(f"list {list(my_range)}")  # [10, 13, 16, 19]
print(my_range[3])  # 19

my_range_new = range(5)
print(f"my_range_new {my_range_new}")  # range(0, 5)

for n in my_range_new:
    print(n)
    '''
   0
   1
   2
   3
   4
   '''

for n in range(2, 7):
    print(n)
    '''
    2
    3
    4
    5
    6
    '''

for n in range(12, 25, 5):
    print(n)
    '''
    12
    17
    22
    '''

my_range_new_new = range(10, 30, 3)
print(f"my_range_new_new {my_range_new_new.start}")  # 10- старт діапазона
print(f"my_range_new_new {my_range_new_new.stop}")  # 30 - стоп діапазона
print(f"my_range_new_new {my_range_new_new.step}")  # 3 - крок(за замовч 1) діапазона

print(f"index {my_range_new_new.index(19)}")  # 3
print(f"count {my_range_new_new.count(11)}")  # 1 - є такий елемент, 0 - нема
