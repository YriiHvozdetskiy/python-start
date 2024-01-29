fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

fruits_quntities_zip = zip(fruits, quantities)
print(f"fruits_quntities_zip {fruits_quntities_zip}")  # <zip object at 0x104b3a080>

fruits_quntities_list = list(fruits_quntities_zip)
print(f"fruits_quntities_list {fruits_quntities_list}")  # [('apple', 100), ('banana', 70), ('lime', 50)]

availability = [True, False, False, True]
fruits_quntities_availability_zip = zip(fruits, quantities, availability)
print(
    f"fruits_quntities_availability_list"
    f" {list(fruits_quntities_availability_zip)}")  # [('apple', 100, True), ('banana', 70, False), ('lime', 50, False)]

fruits_b = ['apple', 'banana', 'lime']
quantities_b = [100, 70, 50]
fruits_quntities_zip_b = zip(fruits_b, quantities_b)
print(f"dict_zip {dict(fruits_quntities_zip_b)}")  # {'apple': 100, 'banana': 70, 'lime': 50}
