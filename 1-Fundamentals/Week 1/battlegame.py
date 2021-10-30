#!/usr/bin/env python
import sys
from time import sleep

def main():
    wizard = "wizard"
    elf = "elf"
    human = "human"
    orc = "orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 200
    dragon_hp = 300

    wizard_dmg = 150
    elf_dmg = 100
    human_dmg = 20
    orc_dmg = 75
    dragon_dmg = 50

    while True:
        print("""
        1) Wizard
        2) Elf
        3) Human
        4) Orc
        9) Exit
        """)
        character = input("Choose your character: ").lower()
        if character == "1" or character == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_dmg = wizard_dmg
            break
        elif character == "2" or character == "elf":
            character = elf
            my_hp = elf_hp
            my_dmg = elf_dmg
            break
        elif character == "3" or character == "human":
            character = human
            my_hp = human_hp
            my_dmg = human_dmg
            break
        elif character == "4" or character == "orc":
            character = orc
            my_hp = orc_hp
            my_dmg = orc_dmg
            break
        elif character == "9" or character == "exit":
            print("\nSee you next time!")
            sys.exit()
        else:
            print("\nUnknown character")

    print(f"You have chosen the character: {character}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_dmg}\n")

    while True:
        dragon_hp -= my_dmg
        print(f"The {character} damaged the dragon\n")
        print(f"The dragon's hitpoint are now: {dragon_hp}")
        sleep(1)
        if dragon_hp <= 0:
            print("The dragon has lost the battle")
            break
        my_hp -= dragon_dmg
        print(f"The dragon has damaged the {character}\n")
        print(f"The {character}'s hitpoints are now: {my_hp}")
        sleep(1)
        if my_hp <= 0:
            print(f"The {character} has lost the battle.")
            break

    while True:
        play_again = input("\nDo you want to play again? (y/n)").lower()
        if play_again == "y":
            main()
        else:
            print("See you next time!")
            sys.exit()

main()