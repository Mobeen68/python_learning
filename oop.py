from abc import ABC, classmethod

class Student:
    ## whenever you create an object, python automatically runs init, Its job is to prepare the object.
    ## self like this in JS
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print(f'My name is {self.name}')
        
student = Student('Mobeen')
student.introduce()

class Dog:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print(f'{self.name} says woof!')
        
dog = Dog("Buddy")
dog.bark()

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def describe(self):
        print(f'{self.name} is {self.color} cat')

cat = Cat("Milo", "black")

cat.describe()

## encapsulation
class User1:
    def __init__(self, name):
        ## single underscore means Please treat this as internal. Python does NOT enforce it. You can still do: user._name But other developers know they shouldn't.
        self._name = name
        
## name mangling
class User:
    def __init__(self, name):
        self.__name = name
        ## Now: user = User("Ali") print(user.__name) Error: AttributeError
        ## Python secretly changes: __name into something like: _User__name This is called name mangling. It's Python's way of saying: "This is private."
    ## to get the data
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
    
user = User("Ali")

print(user.get_name())

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())

class Product:
    def __init__(self, price):
        self.__price = price
        
    def get_price(self):
        return self.__price
    def set_price(self, price):
        if price > 0:
            self.__price = price

product = Product(100)

product.set_price(200)

print(product.get_price())

## inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")
        
class Dog(Animal):
    pass

## children can override parent. classes in this way
class Animal1:
    def speak(self):
        print("Some sound")
        
class Dog1(Animal1):
    def speak(self):
        print("Woof!")

dog = Dog('Buddy')

dog.introduce()

dog1 = Dog1()

dog1.speak()

## if we want to pass something to the parent class
class Animal2:
    def __init__(self, name):
        self.name = name
        
class Dog2(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
dog = Dog2("Buddy", "Labrador")

class Vehicle:
    def start(self):
        print('Vehicle Started')
    
class Car(Vehicle):
    pass

car = Car()
car.start()

## polymorphism: Different objects can respond to the same method call differently.

class Dog6():
    def speak(self):
        print("Woof!")
        
class Cat:
    def speak(self):
        print("Meow")
        
animals = [Dog6(), Cat()]

for animal in animals:
    animal.speak()
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        print(self.width * self.height)
        
class Square:
    def __init__(self, side):
        self.side = side
        
    def area(self):
        print(self.side * self.side)
        
rectangle = Rectangle(3,5)
rectangle.area()

square = Square(4)
square.area()
        
shapes = [Rectangle(2,3), Square(2)]

for shape in shapes:
    shape.area()
    
## composition
class Engine:
    def start(self):
        print("Engine started")
        
class Car:
    def __init__(self):
        self.engine = Engine()
        
    def start_car(self):
        return self.engine.start()
        
car = Car()

car.start_car()

class Battery:
    def charge(self):
        print("Charging battery")
        
class Phone:
    def __init__(self):
        self.battery = Battery()
        
    def charge_phone(self):
        return self.battery.charge()
    
battery = Phone()
battery.charge_phone()

## abstraction: hides implementation details. Fot example, you only care about the car start, you don't care how it starts

class Shape(ABC):
    
    @classmethod
    def area(self):
        return self.width * self.height
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.height = height
        self.width = width
    
    def area(self):
        return super().area(self)
    
rectangle = Rectangle(3,6)
rectangle.area()
