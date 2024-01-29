from os import path  # об'єкт
from pathlib import Path  # класс (надає більше можливостей)

#  абсолютний шлях до поточної папки
print(f"path {path.abspath('.')}")  # path /Users/rasty/Python/python-examples/pythonPyCharm
print(f"Path {Path('.').absolute()}")  # path /Users/rasty/Python/python-examples/pythonPyCharm

# ====================================================

el_path = Path('test.txt')  # рахується відносний шлях, пайтон буде шукати файл в даній папці

# фільтруємо, залишаючи тільки звичайні атрибути
print([m for m in dir(el_path)
       if not m.startswith('_')])
"""
['absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 
'exists', 'expanduser', 'glob', 'group', 'hardlink_to', 'home', 'is_absolute',
'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', 'is_el', 'is_mount',
'is_relative_to', 'is_reserved', 'is_socket', 'is_symlink', 'iterdir', 'joinpath', 
'lchmod', 'link_to', 'lstat', 'match', 'mkdir', 'name', 'open', 'owner', 'parent',
'parents', 'parts', 'read_bytes', 'read_text', 'readlink', 'relative_to', 'rename',
'replace', 'resolve', 'rglob', 'rmdir', 'root', 'sameel', 'stat', 'stem', 'suffix', 
'suffixes', 'symlink_to', 'touch', 'unlink', 'with_name', 'with_stem', 'with_suffix', 
'write_bytes', 'write_text']
"""

print(' ')

# шлях до даної деректорії
print(f"cwd {Path.cwd()}")  # /Users/rasty/Python/python-examples/pythonPyCharm

#  перевірка чи існує папка чи файл
print(f"exists {Path('main.py').exists()}")  # True
print(f"exists {Path('/Users/rasty/Python/python-examples/pythonPyCharm').exists()}")  # True
print(f"exists {Path('json.py').exists()}")  # False

#  перевірка чи є це: папка, файл
print(f"is_file {Path('main.py').is_file()}")  # True
print(f"is_file {Path('pythonPyCharm').is_file()}")  # False
print(f"is_dir {Path('/Users/rasty/Python/python-examples/pythonPyCharm').is_dir()}")  # True
print(f"is_dir {Path('../pythonPyCharm').is_dir()}")  # True

print(' ')

# список файлів і папок
for el in Path('.').iterdir():
    print(f"el {el}")

"""
el cycle.py
el tuple.py
el class_2.py
el lambda.py
el range.py
el __pycache__
el task-1.py
el task_set.py
el zip.py
el el.py
el this_son.py
el task-2.py
el example.py
el class_extended.py
el debug.py
el class.py
el .venv
el dict.py
el operators.py
el main.py
el set.py
el modules
el func.py
el .idea
el decorators.py
"""

# читання і запис файлів
"""
    with - це ключове слово, що використовується для створення менеджера контексту в Python.
    Воно допомагає в автоматизації управління ресурсами, такими як файли. 
    Використання with забезпечує, що ресурси будуть належно відпущені після завершення блоку коду.
    
    Коли виконується блок коду всередині with, ви можете читати з файлу, 
    писати в нього або виконувати інші операції. Після виходу з блоку with, 
    файл автоматично закривається, навіть якщо виникає помилка або виключення.
    Це забезпечує краще управління ресурсами та допомагає уникнути помилок,
    пов'язаних із файлами, які залишилися відкритими.
"""
# ====================================================
# test_file_1 = open('test_1.txt', 'w')
# test_file_1.write('vognuk')
# test_file_1.close()

# or

# with open('test_1.txt') as test_file_2:
#     test_file_2.write('vognuk')
# ====================================================

with open('test.txt') as test_file:
    print(f"read {test_file.read()}")  # це дані з text файлу другий рядок

#  формуємо список з даних файлу по рядках
with open('test.txt') as test_file:
    # readline - працює з курсором (без "s" вкінці)
    print(f"readlines {test_file.readlines()}")  # ['це дані з text файлу\n', 'другий рядок']

print(' ')
# запис в файл
'''
    w - відкрити файл для запису(вміст фалу перезапишеться)
    'w' означає "write mode" (режим запису).
'''
with open('new.txt', 'w') as new_file:
    new_file.write('Перший рядок в новому файлі\n')

with open('new.txt') as new_file:
    print(f"new_file read {new_file.read()}")

'''
    a - дозапис в файл(вміст додасться вкінці)
'''

with open('new.txt', 'a') as new_file:
    new_file.write('Другий рядок в файлі')

with open('new.txt') as new_file:
    print(f"new_file read {new_file.read()}")

print(' ')

# task

# Ім'я папки
folder_name = 'files'

# Створення об'єкта Path для папки
folder_path = Path(folder_name)

# Створення папки, якщо вона не існує
if not folder_path.exists():
    # Створення v1
    folder_path.mkdir()
    print(f"Папка '{folder_name}' була успішно створена.")

    # Створення v2 (якщо папка існує, вона не буде створена знову і не буде помилки)
    folder_path.mkdir(exist_ok=True)
else:
    print(f"Папка '{folder_name}' вже існує.")

# Дані для запису в файли
data_to_write = {
    'file1.txt': ['Вміст першого файл', 'другий рядок першого файлу'],
    'file2.txt': ['Вміст другого файл', 'другий рядок друго файлу', 'третій рядок друго файл']
}

# Перевірка наявності папки та створення файлів
if folder_path.exists():
    for filename, lines in data_to_write.items():
        # Створення файлів
        file_path = folder_path / filename
        with file_path.open(mode='w') as file:
            # Запис даних з списку
            for line in lines:
                file.write(line + '\n')  # переходем на новий рядок
else:
    print(f"Папка '{folder_name}' не існує.")

print(' ')

# Перевірка наявності папки та читання файлів
if folder_path.exists():
    # Отримання списку всіх файлів та підкаталогів у папці
    entries = folder_path.iterdir()

    # Виведення списку файлів та підкаталогів
    for entry in entries:
        if entry.is_file():
            print(f"Файл: {entry.name}")
            with entry.open('r') as file:
                content = file.read()
                print(f"content: {content}")

        elif entry.is_dir():
            print(f"Каталог: {entry.name}")
else:
    print(f"Папка '{folder_name}' не існує.")

print(' ')

# видалення файлів з папки folder_name

# Ітерація по всіх файлах та підкаталогах у папці
for entry in folder_path.iterdir():
    if entry.is_file():
        entry.unlink()  # Видалення файлу
    elif entry.is_dir():
        for subentry in entry.iterdir():
            subentry.unlink()  # Видалення файлів у підкаталозі
        entry.rmdir()  # Видалення підкаталогу
folder_path.rmdir()  # Видалення самої папки
print(f"Папка '{folder_name}' та її вміст були видалені.")
