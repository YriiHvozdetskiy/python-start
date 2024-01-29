# lambda parameters: expression

def greeting(greet):
    return lambda name: f"{greet}, {name}!"


result = greeting("Good Morning")
print(f"result {result}")  # <function greeting.<locals>.<lambda> at 0x1045b6f20>

morning_greeting = greeting("Good Morning")
print(morning_greeting('Bogdan'))  # Good Morning, Bogdan!

evening_greeting = greeting("Good Evening")
print(evening_greeting('Bogdan'))  # Good Evening, Bogdan!

nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Виведе [2, 4, 6]

nums = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Виведе [1, 4, 9, 16, 25, 36]
