import json
name = str(input("What is your name? "))

with open('name.txt', 'w') as file:
    file.write(f'Hello {name}')
    
with open('name.txt') as file:
    content = file.read()
    
print(content)

new_user ={
  "name": "Ali",
  "age": 20
}

with open('new_user.json','w') as file:
    json.dump(new_user, file)
    
with open('new_user.json') as file:
    user = json.load(file)
    
print(f'{user["name"]} is {user["age"]} years old')