import pytest
from ..student_management_system import StudentManager, Student

@pytest.fixture
def manager() -> StudentManager:
    return StudentManager()

def test_add_student(manager:StudentManager):
    manager.add_student(Student("Ali", 20))

    assert len(manager.students) == 1
    
def test_remove_student(manager:StudentManager):
    manager.add_student(Student("Ali", 20))

    manager.remove_student("Ali")

    assert len(manager.students) == 0
    
def test_find_student(manager:StudentManager):
    manager.add_student(Student("Ali", 20))

    result = manager.find_student("Ali")

    assert result[0].name == "Ali"