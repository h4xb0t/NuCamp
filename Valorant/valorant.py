#!/usr/bin/env python
'''This is the main (not)Valorant code'''
from time import sleep
from val_pkg.buy import bot_purchase
from val_pkg.buy import bot_wallet_func
from val_pkg.buy import agent_select
from val_pkg.buy import player_wallet
from val_pkg.buy import player_purchase
from val_pkg.round import combat
from collections import Counter

# player values
agent = ""
wallet = 0
weapon_dmg = {"ghost": 36, "judge": 65, "phantom": 46, "operator": 150}
weapon_range = {"ghost": .5, "judge": .25, "phantom": .9, "operator": 1}
weapon_accuracy = {"ghost": .7, "judge": .5, "phantom": .7, "operator": .7}

# bot values
bot_wallet = 0
bot_dmg = {"ghost": 36, "judge": 55, "phantom": 46, "operator": 150}
bot_range = {"ghost": .5, "judge": .25, "phantom": .9, "operator": 1}
bot_accuracy = {"ghost": .7, "judge": .5, "phantom": .7, "operator": .7}

# general values
round = 1
round_result = {}
win_count = {"victory": 0, "defeat": 0}

# GAME BEGINS

print('''
───────────────────────────────────────────────────
            │  Welcome to Valorant  │
───────────────────────────────────────────────────''')
print('''
            ┌───────────────────────┐
            │      Agent Select     │
            └───────────────────────┘
''')

# AGENT SELECT
agent = agent_select()

# BUY PERIOD

# player wallet is loaded with proper starting amount
wallet = player_wallet(wallet, round, round_result)
bot_wallet = bot_wallet_func(bot_wallet, round, round_result)

while win_count["victory"] <= 12:
    win_count = Counter(round_result.values())
    if win_count["victory"] == 13:
        print("\n||||||||||||||||||||||||||||| ")
        print("|| You have won the match! || ")
        print("|||||||||||||||||||||||||||||\n")
        break
    print('''
            ┌───────────────────────┐
            │       Buy Phase       │
            └───────────────────────┘
''')
    wallet = player_purchase(wallet)
    weapon = player_purchase.weapon
    bot_wallet = bot_purchase(bot_wallet)
    bot_weapon = bot_purchase.bot_weapon
    sleep(1)
    print(f"\n|| Round {round} begins! ||\n")
    # COMBAT PHASE BEGINS
    sleep(1)
    print('''
            ┌───────────────────────┐
            │     Combat Phase      │
            └───────────────────────┘
\n''')
    round_result[round] = combat(weapon_dmg[weapon], weapon_range[weapon], weapon_accuracy[weapon],
                                 bot_dmg[bot_weapon], bot_range[bot_weapon], bot_accuracy[bot_weapon])
    sleep(1)

    # COMBAT PHASE ENDS - ROUND CLEANUP
    sleep(1)
    wallet = player_wallet(wallet, round, round_result[round])
    bot_wallet = bot_wallet_func(bot_wallet, round, round_result[round])
    round += 1

# Things to fix
# player and bot can keep weapon if they win the round
# print to switch sides for round 13
# print rounds win/loss totals before buy phase of each round
