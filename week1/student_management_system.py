from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    
class StudentManager:
    def __init__(self):
        self.students: list[Student] = []
        
    def list_students(self):
        for student in self.students:
            print(student)
    
    def add_student(self, student: Student):
        self.students.append(student)
        
    def remove_student(self, name: str):
        self.students = list(
            filter(lambda student: student.name != name, self.students)
        )
        
    def find_student(self, name: str):
        print(list(
            filter(lambda student: student.name == name, self.students)
        ))
        
manager = StudentManager()

manager.add_student(Student("Ali", 20))
manager.add_student(Student("Ahmed", 22))

manager.list_students()

manager.find_student('Ali')

manager.remove_student('Ali')

manager.list_students()

