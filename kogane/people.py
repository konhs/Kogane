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


DATA_FILE = os.path.join("data", "people.json")

def load_people():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_people(people):
    with open(DATA_FILE, "w") as f:
        json.dump(people, f, indent=4)

def add_person():
    print("\nADD PERSON")

    name = input("Name: ")
    age = input("Age: ")
    phone = input("Phone: ")
    notes = input("Notes: ")

    people = load_people()

    people.append({
        "name": name,
        "age": age,
        "phone": phone,
        "notes": notes
    })

    save_people(people)
    print("Saved!")

def list_people():
    people = load_people()

    print("\nALL PEOPLE")

    if not people:
        print("No people found.")
        return

    for p in people:
        print("-----------------")
        print("Name:", p["name"])
        print("Age:", p["age"])
        print("Phone:", p["phone"])
        print("Notes:", p["notes"])

def search_people():
    people = load_people()

    query = input("Search name: ").lower()

    found = False

    for p in people:
        if query in p["name"].lower():
            print("\nMATCH FOUND")
            print("Name:", p["name"])
            print("Age:", p["age"])
            print("Phone:", p["phone"])
            print("Notes:", p["notes"])
            found = True

    if not found:
        print("No results found.")

def main():
    while True:
        print("\n==== KOGANE ====")
        print("1. Add person")
        print("2. List people")
        print("3. Search")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            add_person()
        elif choice == "2":
            list_people()
        elif choice == "3":
            search_people()
        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()