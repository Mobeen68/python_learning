contacts = [
    {
        "name": "Ali",
        "phone": "123"
    },
    {
        "name": "Ahmed",
        "phone": "456"
    }
]

for contact in contacts:
    print(f'Name: {contact.get('name')}, '
          f'Phone: {contact.get('phone')}')