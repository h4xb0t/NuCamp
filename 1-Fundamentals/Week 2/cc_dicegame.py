#!/usr/bin/env python
import random


def dice_game():
    high_score = 0
    while True:
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        roll_total = roll_1 + roll_2
        print(f"Current High Score: {high_score}\n")
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"\nYou roll a... {roll_1}")
            print(f"You roll a... {roll_2}")
        if choice == "2":
            print("See you next time!")
            exit()
        if roll_total > high_score:
            high_score = roll_total
            print(f"\nNew High Score of: {high_score}\n")


dice_game()
