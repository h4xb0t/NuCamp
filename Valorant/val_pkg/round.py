#!/usr/bin/env python
from time import sleep
'''This module is to simulate a game round'''
# Need a function to compare bot vs Player1 combat stats


def combat(weapon_dmg, weapon_range, weapon_accuracy, bot_dmg, bot_range, bot_accuracy):
    '''Combat phase within a game round'''
    bot_dmg_total = bot_dmg * bot_range * bot_accuracy
    player_dmg_total = weapon_dmg * weapon_range * weapon_accuracy
    if player_dmg_total >= bot_dmg_total:
        round_result = "victory"
        sleep(2)
        print("|| Round Won! ||")
        return round_result
    elif bot_dmg_total > player_dmg_total:
        round_result = "defeat"
        sleep(2)
        print("|| Round Lost! ||")
        return round_result

    # player1_dmg = weapon_dmg[player1_weapon]
    # bot_dmg = weapon_dmg[bot_weapon]
    # print(f"{player1} attacks with {player1_dmg} damage!")
    # print(f"{bot} attacks with {bot_dmg} damage!")

    # random distance of fight generated e.g. randint(1, 90)
    # user weapons get a rand multiplier for damage based effective range
    # user weapons get a rand hit % based on range
    # values are compared in fight vs bot(who also gets random values)
    # winning the fight gives the winner more cash for next round
    # losing the fight gives less cash for next round
