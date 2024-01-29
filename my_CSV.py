import csv

# Для exel таблиць

# Створюєм файл
# with open('test.csv', mode='w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([5235, 'Vasa', 1234])
#     writer.writerow([5236, 'Dima', 34])
#     writer.writerow([5237, 'Moly', 23])

"""
    user_id,user_name,comments_qty
    5235,Vasa,1234
    5236,Dima,34
    5237,Moly,23
"""

# with open('test.csv') as csv_file:
#     reader = csv.reader(csv_file)  # можна ітерувати тільки 1 раз
#     for line in reader:
#         print(f"line {line}")
#
#     print(f"line_num {reader.line_num}")  # 4 - де знаходиться курсор в файлі(4- останій рядок)

"""
    line ['user_id', 'user_name', 'comments_qty']
    line ['5235', 'Vasa', '1234']
    line ['5236', 'Dima', '34']
    line ['5237', 'Moly', '23']
"""

"""
    csv_list = list(reader)
    print(f"csv_list {csv_list}")
    
    [['user_id', 'user_name', 'comments_qty'],
    ['5235', 'Vasa', '1234'], 
    ['5236', 'Dima', '34'],
    ['5237', 'Moly', '23']]
"""

# Створюєм файл з іншим розділювачем ';'
# with open('test.csv', mode='w') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';')
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([5235, 'Vasa', 1234])
#     writer.writerow([5236, 'Dima', 34])
#     writer.writerow([5237, 'Moly', 23])
