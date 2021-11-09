#!/usr/bin/env python
from getpass import getpass
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin": "password123"}

donations = []

authorized_user = ""


# show_homepage()
while True:
    if authorized_user == "":
        print("\nYou must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")
    show_homepage()
    menu_choice = input("Please select a choice from the menu: ")
    if menu_choice == "1":
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")
        authorized_user = login(database, username, password)
    elif menu_choice == "2":
        username = input("Enter your username to register: ")
        password = getpass("Enter your password to register: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[authorized_user] = password
    elif menu_choice == "3":
        if authorized_user != "":
            donation = donate(authorized_user)
            donations.append(donation)
    elif menu_choice == "4":
        show_donations(donations)
    elif menu_choice == "5":
        print("Goodbye!")
        break
