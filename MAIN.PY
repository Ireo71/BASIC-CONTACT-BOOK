"""
Loop: while loop 
cotacts = {
"Adam": {"Phone Number": 08012345678, "Email": "adam7@gmail.com},
"Eve": {"Phone Number": 08012373679, "Email": "eve2@gmail.com}
}

contacts = {}

Menus:
1 Add Contact
2 View Contact

"""


contact_book = {}


def addContact():
    contact_name = input("Enter contact name: ")


    if contact_name not in contact_book:
        contact_phone = input("Enter contact phone number: ")
        contact_email = input("Enter contact email: ")
        contact_details = dict(phone_number=contact_phone, email=contact_email)
        contact_book[contact_name] = contact_details
        print(contact_book)
    else:
        print("Name already exist, kindly choose another name.")


def viewContact():
    for key, value in contact_book.items():
        print(f"{key}:")
        for key, value in value.items():
            print(f"{key} : {value}")
    print("=============================================")

def searchContact():
    search_name = input("Enter the contact name to search: ")
    if search_name in contact_book:
        # Filter:
        filtered = {k: v for k, v in contact_book.items() if k == search_name}
        for key, value in filtered.items():
            print(f"{key}:")
        for key, value in value.items():
            print(f"{key} : {value}")

        print(filtered)   


def deleteContact():
    delete_name = input("Enter contact name to be deleted: ")
    delete_name1 = delete_name

    if delete_name in contact_book:
        del delete_name
        print(f"{delete_name1} is successfully deleted from your contact book!")
    else:
        print(f"{delete_name} does not exist in the contact book!")


while True:
    choice = input("Menu Type:\n1 - Add contact\n2 - View contact\n3 - Search contact\n4 - Delete\n5 - Exit\n  :")

    if choice == "1":
        addContact()
    elif choice == "2":
        viewContact()
    elif choice == "3":
        searchContact()
    elif choice == "4":
        deleteContact()
    elif choice == "5":
        break       
    else:
        print("Invalid Menu Choice! Please select a valid menu!")    
