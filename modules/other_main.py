from other import my_fn

# ['__annotations__', '__builtins__','__cached__',
# '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__']
# print(dir())
print('other_main.py', __name__)  # __main__
print('other_main.py', __name__ == '__main__')  # True

help('modules')
help('time')
