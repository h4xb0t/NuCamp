#!/usr/bin/env python

def login(database, username, password):
    '''Login Function'''
    if username in database:
        if password == database[username]:
            print(f"Welcome back {username}!\n")
            return username
        else:
            print("Incorrect Password")
            return ""
    else:
        print(f"{username} is not registered")
        return ""


def register(database, username):
    '''Registration function'''
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print(f"{username} is now registered.")
        return username
