#!/usr/bin/env python
from time import sleep

# Need a function to compare CPU vs Player1 combat stats


def game_round():
    '''Runs a game round'''
    round = 1
    player_win = True
    print(f"Round {round} begins!")
    combat()
    for round, result in round_result.items():
        last_round_result = result
    round += 1
    print(last_round_result)
    sleep(5)
    buy_period(round, last_round_result)


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
