# Класс Студент
'''
 class Student:
     def __init__(self, name, age, average_score):
         self.name = name
         self.age = age
         self.average_score = average_score

     def get_name(self):
         return self.name

     def set_name(self, name):
         self.name = name

     def get_age(self):
         return self.age

     def set_age(self, age):
         self.age = age

     def get_average_score(self):
         return self.average_score

     def set_average_score(self, average_score):
         self.average_score = average_score


 student = Student("Консантин Костяков", 16, 4.85)

 print(student.get_name())
 print(student.get_age())
 print(student.get_average_score())
'''

# ----------------------------------------------------------------------------------------------------------------------

'''
# Класс прямоугольник
 class Rectangle:
     def __init__(self, length, width):
         self.length = length
         self.width = width

     def test_area(self):
         return self.length * self.width

     def test_perimeter(self):
         return 2 * (self.length + self.width)

 rectangle = Rectangle(10, 15)
 print(rectangle.test_area())
 print(rectangle.test_perimeter())
'''

#----------------------------------------------------------------------------------------------------------------------
# Класс Автомобиль
# class Car:
#     def __init__(self, brand, model, year, mileage):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#     def set_info(self, new_brand, new_model, of_year, new_mileage):
#         self.brand = new_brand
#         self.model = new_model
#         self.year = of_year
#         self.mileage = new_mileage
#
#     def get_info(self):
#         return f"{self.year} {self.brand} {self.model}, Mileage: {self.mileage} miles"
#
#
# car1 = Car("Toyota", "Camry", 2022, 15000)
# print(car1.get_info())
# car1.set_info("Lada", "Granta". 2015, 25000)

'''
# Класс Банковский счёт
class BankAccount:
    def __init__(self, client_name, balance):
        self.client_name = client_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Снятие денежных средств: -{amount}")
        else:
            return "Недостаточно средств на счете"

    def info_transactions(self):
        list_tr = []
        for i in range(0, len(self.transactions)):
            list_tr.append(f'- {self.transactions[i]}')
        return list_tr


account1 = BankAccount("Иванов", 1000)
account1.deposit(500)
account1.withdraw(200)

print('История:')
print(account1.info_transactions())
'''


'''
# Класс Треугольник
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный"
        else:
            return "Разносторонний"

    def get_area(self):
        perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = (perimeter * (perimeter - self.side1) * (perimeter - self.side2) *
                (perimeter - self.side3)) ** 0.5
        return area


triangle1 = Triangle(3, 4, 5)
print(f"Тип треугольника: {triangle1.get_type()}")
print(f"Площадь треугольника: {triangle1.get_area()}")
'''
