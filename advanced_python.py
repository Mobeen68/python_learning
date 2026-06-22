from dataclasses import dataclass

## dataclasses: you don't need to write all the boilerplate.
## important: Dataclasses are for data containers, not business logic-heavy classes.
@dataclass
class User:
    name: str
    age: int = 18 ## default value
    
user = User("Mobeen", 25)
print(user)

@dataclass(frozen= True)
class Product:
    name: str
    price: float
    
product = Product('Laptop', 20)
## it will not work because class is frozen now. It's immutable
# product.price = 30

@dataclass
class Student:
    title: str
    
class Course:
    def __init__(self):
        self.students = []
        
    def add_students(self, student):
        self.students.append(student)
        
    def show_students(self):
        for student in self.students:
            print(student)
            
    
course = Course()

course.add_students(Student("Robert Martin"))
course.add_students(Student("Guido"))

course.show_students()

