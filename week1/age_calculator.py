name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello {name}!")
print(f'You are currently {age} years old.')
print(f'Next year you will be {age +1} years old.')

if age >= 18:
    print('Adult')
else:
    print('Minor')