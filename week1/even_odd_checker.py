num = int(input('Enter number to check: '))

def isEven(number: int) -> bool:
    return number % 2 == 0

if num % 2:
    # because in python 0 is a falsey value, so when a number is fully divisible by 2, it returns 0 which in turn will send our compiler to the else section
    print(f'{num} is odd')
else:
    print(f'{num} is even')