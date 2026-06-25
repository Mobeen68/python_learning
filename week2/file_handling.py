import json

file = open('hello.txt')
content = file.read()
print(content)
## this required to close the file. If not closed, then it will remain open in the memory and too much file will create a problem
file.close()

## more pythonic way is 'with'. It automatically handles the close
with open("hello.txt") as file:
    content = file.read()

print(content)

## reading line by line. this is good as it will not load the whole file
with open("hello.txt") as file:
    for line in file:
        print(line)
        
## read the whole file
with open("hello.txt") as file:
    lines = file.readlines()

print(lines)

## writing a file
## w means to override the data
with open("hello.txt", "w") as file:
    file.write("Hello Python")
    
## a means append at the end of the file. Add the data without changing the previous data.
with open("hello.txt", "a") as file:
    file.write("\nAnother line")
    
## for json
user = {
    "name": "Mobeen",
    "age": 27
}

with open("user.json", "w") as file:
    json.dump(user, file)
    
with open("user.json") as file:
    user = json.load(file)

print(user)
