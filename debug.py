try:
    print('10' / 0)
except ZeroDivisionError:  # тут обробляється ТІЛЬКИ цей вид помилок
    print('Error - Division by zero')

except TypeError as e:
    print(f"TypeError {e}")

print('next...')

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Виникла помилка в: {e}")  # e - виводить повідомлення помилки

'''
В блоку else код виконується, якщо в блоку try не виникає винятків.
Блок finally виконується завжди, незалежно від того,чи виник виняток.
'''
try:
    number = int(input("Введіть число: "))
except ValueError:
    print("Це не число!")
else:  # виконається якщо не було помилок
    print("Ви ввели число:", number)
finally:  # виконується завжди
    print("Блок 'finally' завжди виконується.")

try:
    # Деякий код, який може викликати помилку
    result = 1 / 0
except Exception as e:  # Exception - універсальний тип помилок
    print(f"Виникла помилка: {e}")


# ======= generate errors ============

def divede_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b


try:
    divede_nums(10, 0)
except ValueError as e:
    print(f"ValueError {e}")

# task

my_dict = {
    # 'image_id': '5136',
    'image_title': 'MiIIIeLb',
    'age': 3,
}


def image_info(passed_dict):
    # перевірка чи є ключі image_id, image_title в словнику
    if ('image_id' not in passed_dict) or ('image_title' not in passed_dict):
        raise TypeError('No have key')

    image_id = passed_dict['image_id']
    image_title = passed_dict['image_title']

    return f"Image {image_title} has id {image_id}"


try:
    print(f"image_info {image_info(my_dict)}")
except TypeError as e:
    print(f"TypeError {e}")
