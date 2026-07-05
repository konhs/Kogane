#!/usr/bin/env python3

import json
import os

# ==========================
# KOGANE
# ==========================

banner = r"""
 _  __                           
| |/ /___   __ _  __ _ _ __   ___
| ' // _ \ / _` |/ _` | '_ \ / _ \
| . \ (_) | (_| | (_| | | | |  __/
|_|\_\___/ \__, |\__,_|_| |_|\___|
            |___/

A liaison between players and You! XD
"""

print(banner)

DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "people.json")


# ==========================
# FILE FUNCTIONS
# ==========================

def load_people():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_people(people):
    with open(DATA_FILE, "w") as f:
        json.dump(people, f, indent=4)


# ==========================
# ADD
# ==========================

def add_person():
    print("\n=== ADD PERSON ===")

    person = {
        "name": input("Name: "),
        "age": input("Age: "),
        "phone": input("Phone: "),
        "notes": input("Notes: ")
    }

    people = load_people()
    people.append(person)
    save_people(people)

    print("\nPerson saved!")


# ==========================
# LIST
# ==========================

def list_people():
    people = load_people()

    print("\n=== PEOPLE ===")

    if not people:
        print("No people stored.")
        return

    for i, person in enumerate(people, start=1):
        print("-" * 30)
        print(f"#{i}")
        print("Name :", person["name"])
        print("Age  :", person["age"])
        print("Phone:", person["phone"])
        print("Notes:", person["notes"])


# ==========================
# SEARCH
# ==========================

def search_people():
    people = load_people()

    search = input("\nSearch name: ").lower()

    found = False

    for person in people:
        if search in person["name"].lower():
            print("-" * 30)
            print("Name :", person["name"])
            print("Age  :", person["age"])
            print("Phone:", person["phone"])
            print("Notes:", person["notes"])
            found = True

    if not found:
        print("No matches found.")


# ==========================
# EDIT
# ==========================

def edit_person():
    people = load_people()

    if not people:
        print("\nNo people to edit.")
        return

    print("\n=== EDIT PERSON ===")

    for i, person in enumerate(people, start=1):
        print(f"{i}. {person['name']}")

    try:
        index = int(input("\nPerson number: ")) - 1

        if index < 0 or index >= len(people):
            print("Invalid selection.")
            return

        person = people[index]

        print("\nLeave blank to keep the current value.\n")

        new_name = input(f"Name ({person['name']}): ")
        new_age = input(f"Age ({person['age']}): ")
        new_phone = input(f"Phone ({person['phone']}): ")
        new_notes = input(f"Notes ({person['notes']}): ")

        if new_name:
            person["name"] = new_name

        if new_age:
            person["age"] = new_age

        if new_phone:
            person["phone"] = new_phone

        if new_notes:
            person["notes"] = new_notes

        save_people(people)

        print("\nPerson updated!")

    except ValueError:
        print("Please enter a valid number.")


# ==========================
# DELETE
# ==========================

def delete_person():
    people = load_people()

    if not people:
        print("\nNo people to delete.")
        return

    print("\n=== DELETE PERSON ===")

    for i, person in enumerate(people, start=1):
        print(f"{i}. {person['name']}")

    try:
        index = int(input("\nPerson number: ")) - 1

        if index < 0 or index >= len(people):
            print("Invalid selection.")
            return

        removed = people.pop(index)

        save_people(people)

        print(f"\nDeleted {removed['name']}")

    except ValueError:
        print("Please enter a valid number.")


# ==========================
# MENU
# ==========================

def main():

    while True:

        print("\n========== KOGANE ==========")
        print("1. Add person")
        print("2. List people")
        print("3. Search")
        print("4. Edit person")
        print("5. Delete person")
        print("6. Exit")

        choice = input("\nSelect: ")

        if choice == "1":
            add_person()

        elif choice == "2":
            list_people()

        elif choice == "3":
            search_people()

        elif choice == "4":
            edit_person()

        elif choice == "5":
            delete_person()

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()