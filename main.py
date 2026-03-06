import json
import os

FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print("Contact added.")

def show_contacts():
    contacts = load_contacts()
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

def delete_contact():
    contacts = load_contacts()
    show_contacts()
    index = int(input("Enter contact number to delete: ")) - 1
    contacts.pop(index)
    save_contacts(contacts)
    print("Contact deleted.")

while True:
    print("\n1.Add Contact")
    print("2.Show Contacts")
    print("3.Delete Contact")
    print("4.Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
