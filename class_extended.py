# ExtendedList буде підкласом класа list
# люнцюжок класів: custom_list => ExtendedList => list => object
class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([3, 5, 2])
# custom_list має всі методи класу list, ExtendedList
custom_list.print_list_info()


class Vehicle:
    def general_usage(self):
        return "General use: transportation"


class Car(Vehicle):
    def specific_usage(self):
        return "Specific use: Commute to work"


car = Car()
print(car.general_usage())  # Наслідування з класу Vehicle
print(car.specific_usage())  # Метод визначений в Car


class Engine:
    def power(self):
        return "Engine: Combustion power"


class ElectricBattery:
    def type(self):
        return "Battery: Lithium-Ion"


class ElectricCar(Engine, ElectricBattery):
    def specific_usage(self):
        return "Specific use: Environment-friendly transportation"


electric_car = ElectricCar()
print(electric_car.power())  # Наслідування з класу Engine
print(electric_car.type())  # Наслідування з класу ElectricBattery
print(electric_car.specific_usage())  # Метод визначений в ElectricCar
