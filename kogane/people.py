#!/usr/bin/env python3

import json
import os


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


DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "people.json")


def load_people():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_people(people):
    with open(DATA_FILE, "w") as f:
        json.dump(people, f, indent=4)


def add_person():
    print("\n=== Add Person ===")

    name = input("Name: ")
    age = input("Age: ")
    phone = input("Phone: ")
    address = input("Address: ")
    notes = input("Notes: ")

    people = load_people()

    people.append({
        "name": name,
        "age": age,
        "phone": phone,
        "address": address,
        "notes": notes
    })

    save_people(people)

    print("\nPerson added successfully!")


def list_people():
    people = load_people()

    if len(people) == 0:
        print("\nNo people stored.")
        return

    print("\n=== People ===")

    for i, person in enumerate(people, start=1):
        print("-" * 30)
        print(f"#{i}")
        print(f"Name    : {person['name']}")
        print(f"Age     : {person['age']}")
        print(f"Phone   : {person['phone']}")
        print(f"Address : {person['address']}")
        print(f"Notes   : {person['notes']}")


def search_people():
    people = load_people()

    search = input("\nSearch name: ").lower()

    found = False

    for person in people:
        if search in person["name"].lower():
            found = True
            print("-" * 30)
            print(f"Name    : {person['name']}")
            print(f"Age     : {person['age']}")
            print(f"Phone   : {person['phone']}")
            print(f"Address : {person['address']}")
            print(f"Notes   : {person['notes']}")

    if not found:
        print("No matches found.")


def main():
    while True:
        print("\n====================")
        print("      KOGANE")
        print("====================")
        print("1. Add person")
        print("2. List people")
        print("3. Search")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_person()

        elif choice == "2":
            list_people()

        elif choice == "3":
            search_people()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()