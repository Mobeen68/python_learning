from utils import student_utils
import requests

print(requests.__version__)

try:
    age = int(input("How old are you? "))
    if(student_utils.is_adult(age)):
        print('Adult')
    else:
        print('Minor')
except ValueError:
    print('Please enter a valid number')
else:
    print('Success')
finally:
    print('Program finished')
    
while True:
    try:
        num = int(input("Enter number: "))
        print(f"You entered {num}")
        break
    except ValueError:
        print("Please enter a valid number")
    
def divide(a, b):
        return a/b

try:
    divide(9,0)
except ZeroDivisionError:
    print('Cannot divide by zero')
    
def student_profile(*grades, **info):
    print(f"Grades: {grades}")
    print(f"Name: {info.get('name')}")
    print(f"Age: {info.get('age')}")
    avg = sum(grades) / len(grades) if grades else 0
    print(f"Average: {avg}")
    
student_profile(80, 90, 85, name="Ali", age=20)

students = [
    {"name": "Ali", "age": 17},
    {"name": "Ahmed", "age": 25},
    {"name": "Mobeen", "age": 27},
]

filtered_students = list(
    filter(lambda student: student.get('age') > 18, students)
)

final_result = list(map(lambda student: student.get('name'), filtered_students))

print(final_result)

## one list comprehension

print([student.get('name') for student in students if student.get('age') > 18])

## iterators and generators
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)
    
## decorators 

def timer(func):
    def wrapper():  
        print('Starting function...')
        func()
        print('Function finished.')
    return wrapper

@timer
def say_hi():
    print('Hi')
    
say_hi()

class Employee:
    def __init__(self,name):
        self.name = name
        
    def work(self):
        print(f'Employee name is {self.name}')
        
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
        
    def work(self):
        print(f'{self.name} manages {self.department} department')
        
manager = Manager("Ali", "Engineering")
manager.work()
    
