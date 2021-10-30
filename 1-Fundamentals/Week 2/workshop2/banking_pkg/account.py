#!/usr/bin/env python

def show_balance(balance):
    print(f"\nCurrent Balance: ${balance}")


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print(f"\nInsufficient funds - unable to withdraw ${amount}")
        return balance
    else:
        balance -= amount
        return balance


def logout(name):
    print(f"\nGoodbye {name}")
