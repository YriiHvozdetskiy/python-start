def my_fn():
    pass


print('other.py', __name__)  # __main__
print('other.py', __name__ == '__main__')  # True
