
contacts = {}

while True:
    print('\n Contact Book App') 
    print('1. Create Contact') 
    print('2. View Contact') 
    print('3. Update  Contact') 
    print('4. Delete Contact') 
    print('5. Seach Contact') 
    print('6. Count Contact') 
    print('7. Exit') 

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input("Enter age: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contacts[name] = {'age': int(age), 'email':email, 'phone':phone}
            print(f'Contact name {name} has been CREATED succesfully!')

    elif choice == '2':
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts [name]
            print(f'Name: {name}, Age = {age}, Phone Number:{phone}')           
        else:
            print("Contact not found!")

    elif choice == '3':
        name = input("Enter contact to update: ")
        if name in contacts:
            age = input("Enter updated age: ")
            phone = input("Enter updated phone: ")
            email = input("Enter updated email: ")
            contacts[name] = {'age': int(age), 'email':email, 'phone':phone}
        else:
            print('Contact not found!')

    elif choice == '4':
        name = input("Enter contact to delete: ")
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been DELETED succesfully!')
        else:
            print('Contact not found!')

    elif choice == '5':
        search_name = input("Enter contact to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found = Name {name}, Age:{age}, Mobile Number:(mobile), Email:{email}')
                found =True

        if not found:
            print("No contacts FOUND!")

    elif choice == '6':
        print(f'Total contacts in your book : {len(contacts)}')

    elif choice == '7':
        print('...Exit...')
        break
    else:
        print('Invalid Input')



        