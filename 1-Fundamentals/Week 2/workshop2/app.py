#!/usr/bin/env python
from banking_pkg import account
from time import sleep


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
while True:
    name = input("Enter name to register: ").title()
    if len(name) < 1 or len(name) > 10:
        print("The maximum name length is 10 characters, please try again.")
    else:
        break
while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4:
        print("PIN must contain 4 numbers, please try again.")
    else:
        break

balance = 0

print(f"\n{name} has been registered with a starting balance of ${balance}")

while True:
    print("\n\t\tATM LOGIN")
    name_to_validate = input("Enter name: ").title()
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials!")


while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
        sleep(1)
        continue
    elif option == "2":
        balance = account.deposit(balance)
        print(f"Current Balance: ${balance}")
        sleep(1)
        continue
    elif option == "3":
        balance = account.withdraw(balance)
        print(f"Current Balance: ${balance}")
        sleep(1)
        continue
    elif option == "4":
        account.logout(name)
        break
