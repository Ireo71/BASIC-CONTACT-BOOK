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

while True:
    choice = input("Menu Type:\n1 - Add contact\n2 - View contact\n3 - Search contact\n4 - Delete\n5 - Exit\n  :")

    if choice == "1":
        print("Add Menu Choice")
    elif choice == "2":
        print("View Menu Choice")
    elif choice == "3":
        print("Search Menu Choice")
    elif choice == "4":
        print("Delete Menu Choice")
    elif choice == "5":
        break       
    else:
        print("Invalid Menu Choice! Please select a valid menu!")    
