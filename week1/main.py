## variables
firstName = 'Mobeen'
lastName = 'Khan'
age = 30
is_employed = True
salary = 50000.0

print(f"Name: {firstName} {lastName}")
print(f"Age: {age}")
print(f"Employed: {is_employed}")
print(f"Salary: ${salary:.2f}")

print(type(firstName))
print(type(age))
print(type(is_employed))
print(type(salary))

print(firstName[:])

## if statemeents
age = 16

if age >= 18:
    print('Adult')
else:
    print('Minor')


## loops
for i in range(1,6):
    print(i)
    
name = 'Python'
for char in name:
    print(char)
    
## functions

def greeting(name):
    return f'Hello {name}'

print(greeting('Mobeen'))

def sqaure(number):
    return number ** 2

print(sqaure(2))

def is_even(number):
    return number % 2 == 0

print(is_even(3))

## arrays

fruits = ["Apple", "Banana"]
fruits.append('Orange')
print(fruits)

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
    
students = [
    "Ali",
    "Ahmed",
    "Mobeen"
]
for student in students:
    print(f'Student: {student}')
    
## dictionary(which is called object in JS)
user = {
    "name": "Mobeen",
    "age": 27
}

for key, value in user.items():
    print(f'{key}: {value}')

user['city'] = 'Lahore'
print(user)

## tuples(immutable list)
names = ("Ali", "Ahmed", "Mobeen")

print(names)

## set(like JS set, duplicate gets removed)
skills = {'React', 'Python', 'React'}
skills.add('Flutter')
print(skills)
print("Python" in skills)

## lambda functions(single line functions)
square = lambda x: x * x
print(square(5))

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)

numbers = [1, 2, 3, 4, 5, 6]

evens = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(evens)

## list comprehensions
## instead of list(map(lambda x: x * 2, numbers))
print([x * 2 for x in numbers])
## instead of list( filter(lambda x: x % 2 == 0, numbers))
print([x for x in numbers if x % 2 == 0])

users = [
    {
        "name": "Ali",
        "age": 17
    },
    {
        "name": "Ahmed",
        "age": 25
    },
    {
        "name": "Mobeen",
        "age": 27
    }
]

print([user['name'] for user in users if user['age'] >= 18])