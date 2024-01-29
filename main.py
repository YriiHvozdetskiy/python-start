# This is a sample Python script.
from example import my_cat, say_vode, my_dict

list = ['Hello', 'World', True, {'my_name': 'John', 'age': 30}, [1, 2, 3]]

print(f"list {list[3]['my_name']}")

print(f"list {list[4][0]}")

my_name = 'John'

# dir start

# вивід всіх доступних методів визначеного об'єкта (рядок, число)
print(f"methods in object {dir(my_name)}")

if my_name.count('J'):
    print(f"true")
else:
    print(f"false")

# dir вивід всіх доступних методів
print(f"methods global {dir(__builtins__)}")


def print_hi(name):
    print(f'Hi, {name}')


print(f"my_cat {my_cat}")

say_vode('meawwww')

print(f"my_dict in main {my_dict}")


# =============================================================================
def hello(name: str) -> None:
    print(f"name {name}")


print(f"hello function {hello('2')}")  # return None

print(f"bool {bool.__doc__}")
'''
bool.__doc__: 
Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.
'''

if __name__ == '__main__':
    print_hi('PyCharm')
