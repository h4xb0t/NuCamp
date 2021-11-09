#!/usr/bin/env python
from time import sleep
'''This module is to simulate a game round'''
# Need a function to compare CPU vs Player1 combat stats


def combat():
    '''Combat phase within a game round'''
    player_dmg = "20"
    cpu_dmg = "10"
    player = "Riot Kon"
    cpu = "Phoenix"
    print(f"{player} attacks with {player_dmg} damage!")
    print(f"{cpu} attacks with {cpu_dmg} damage!")

    # random distance of fight generated e.g. randint(1, 90)
    # user weapons get a rand multiplier for damage based effective range
    # user weapons get a rand hit % based on range
    # values are compared in fight vs CPU(who also gets random values)
    # winning the fight gives the winner more cash for next round
    # losing the fight gives less cash for next round
