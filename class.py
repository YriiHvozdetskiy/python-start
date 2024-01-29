class Car:
    """
        self - значення в середині методів move, stop буде обєкт my_car,
        ітд(якщо будуть нові обєкти)
    """

    def move(self):
        print('Car moving')

    def stop(self):
        print('Car stoping')


my_car = Car()
my_second_car = Car()

my_car.move()  # Car moving

print(Car.move(my_car))  # Car moving

print(f"== {my_car == my_second_car}")  # False
# перевірка чи належе екзимпляр класу
print(f"isinstance {isinstance(my_car, Car)}")  # True
print(f"isinstance {isinstance(my_car, object)}")  # True

# {} - вказує що my_car немає власних методів, всі методи наслідувані з класу
print(my_car.__dict__)

#  __init__
"""
    Власні атрибути екзимплярів визначаються ф-цією __init__
"""


class Comment:
    """
    __init__ - ф-кція конструктор для цього класу вона створює всі нові екзимпляри цього класу,
               викликається автоматично під капотом
    """

    # якщо викликати метод з 1 аргументом то буде:
    # Comment.__init__() missing 1 required positional argument: 'initial_votes_qty'
    # фікс- потрібно задати значення за замовчуванням
    def __init__(self, text='', initial_votes_qty=0):
        self.text = text
        self.votes_qty = initial_votes_qty

    def upvote(self, qty):
        self.votes_qty += qty

    def reset_votes_qty(self):
        self.votes_qty = 0


first_comment = Comment('helloow')  # тут викликається під капотом __init__
second_comment = Comment()
# показує власні атрибути об'єкта
print(f"__dict__ {first_comment.__dict__}")  # {'text': 'helloow', 'votes_qty': 0}

print(first_comment.text)  # helloow
print(first_comment.votes_qty)  # 0
first_comment.upvote(10)
print(first_comment.votes_qty)  # 10
first_comment.upvote(1)
print(first_comment.votes_qty)  # 11
# first_comment.reset_votes_qty()
# print(first_comment.votes_qty)  # 0
print(f"second_comment {second_comment.votes_qty}")  # 0


# task 1

class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, value):
        self.resolution = value


my_img = Image(resolution=480, title='nanture', extension='png')
my_img.resize(1080)

print(f"my_img {my_img.resolution}")


class CommentTwo:
    def __init__(self, text):
        self.text = text

    # вказує що метод можна викликати як на рівні класу так й на екзимплярі
    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"


my_comment = CommentTwo('My comment')

m_1 = CommentTwo.merge_comments('Thanks', 'Excellent')
print(f"m_1 {m_1}")  # Thanks Excellent
m_2 = my_comment.merge_comments('Great', 'ok')
print(f"m_2 {m_2}")  # Great ok


# atribute class

class CommentThree:
    # total_comments - атрибут класа,
    # наслідується екзимплярами класа (comment_three_1, comment_three_2)
    total_comments = 0

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        CommentThree.total_comments += 1


comment_three_1 = CommentThree('comment 1')
# збільшується при створенні екзимлярів з цього класу
print(f"total_comments {CommentThree.total_comments}")  # 1

comment_three_2 = CommentThree('comment 2')
# збільшується при створенні екзимлярів з цього класу
print(f"total_comments {CommentThree.total_comments}")  # 2

print(f"comment_three_1.total_comments {comment_three_1.total_comments}")  # 2

# з екзимпляра НЕ можем зміниит атрибут самого класу
comment_three_1.total_comments = 10
print(CommentThree.total_comments)  # 2

CommentThree.total_comments = 777

print(CommentThree.total_comments)  # 777
print(comment_three_2.total_comments)  # 777
print(comment_three_1.total_comments)  # 10 див. 131 рядок
