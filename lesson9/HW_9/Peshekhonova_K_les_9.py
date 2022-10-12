""" Katherine Peshekhonova, lesson 9 """

from dataclasses import dataclass
from datetime import date

""" Task 1 """

""" Class """


class CarOne:
    def __init__(self, make, model, price):
        super().__init__()
        self.make = make
        self.model = model
        self.price = price


car_1 = CarOne('BMW', 'X5', 30000)
print(car_1.make)
print(car_1.model)
print(car_1.price)


""" A class using the @dataclass decorator """


@dataclass
class CarTwo:
    make: str
    model: str
    price: float


car_2 = CarTwo('BMW', 'i8', 25000)
print(car_2)


""" Task 2 """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """This method calculates age using the year of birth"""
    @classmethod
    def years_of_age(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def result(self):
        print(self.name + "'s age is: " + str(self.age))


human_1 = Person('Adam', 27)
human_1.result()

human_2 = Person.years_of_age('Daniel', 1999)
human_2.result()


""" Task 3 """


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def info(self):
        print(f'{self.name} - {self.email}')

    @staticmethod
    def age_info(age):
        if age > 18:
            return True
        else:
            return False


user_1 = User("Kris", "kris@gmail.com")
user_1.info()

user_2 = User.age_info(21)
print(user_2)

