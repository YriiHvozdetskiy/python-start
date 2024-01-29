from zipfile import ZipFile
from pathlib import Path

# Створення архіву

# folder_name = 'my-zip'
#
# # Створення архіву з розширенням .zip
# with ZipFile('my-files.zip', mode='w') as my_zip_file:
#     # Ітерація по всіх файлах у папці
#     for file in Path(folder_name).iterdir():
#         if file.is_file():
#             # Додавання файлу до архіву
#             my_zip_file.write(file, file.relative_to(folder_name))


# Розпаковування архіву

with ZipFile('my-files.zip') as my_zip_file:
    # my_zip_file.extractall('my-files-unzipped')
    print(f"infolist {my_zip_file.infolist()}")

# [<ZipInfo filename='first.txt' filemode='-rw-r--r--' file_size=18>,
# <ZipInfo filename='second.txt' filemode='-rw-r--r--' file_size=19>]
