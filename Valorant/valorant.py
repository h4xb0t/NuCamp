#!/usr/bin/env python
'''This is the main Valorant code'''
import random
from time import sleep
import val_pkg.buy
import val_pkg.round

wallet = 0
cpu_wallet = 0
weapon = ""
weapon_dmg = {"Ghost": 36, "Judge": 55, "Phantom": 46, "Operator": "150"}
weapon_range = {"Ghost": .5, "Judge": .25, "Phantom": .9, "Operator": 1}
player_inventory = {}
round = 1
round_result = {2: "defeat", 3: "victory", 4: "defeat"}
post_purchase_wallet = ""
post_purchase_cpu_wallet = ""

# GAME BEGINS
print('''
───────────────────────────────────────────────────
            │  Welcome to Valorant  │
───────────────────────────────────────────────────''')

# BUY PERIOD
# player wallet is loaded with proper starting amount
wallet = val_pkg.buy.player_wallet(wallet, round, round_result)
# cpu_wallet = val_pkg.buy.cpu_wallet_track(cpu_wallet, round, round_result)
while True:
    print('''
            ┌───────────────────────┐
            │       Buy Phase       │
            └───────────────────────┘
''')
    post_purchase_wallet = val_pkg.buy.player_purchase(wallet)
    wallet = post_purchase_wallet
    # post_purchase_cpu_wallet = val_pkg.buy.cpu_wallet_track(
    #     cpu_wallet, round, round_result[round])
    # cpu_wallet = post_purchase_cpu_wallet
    # val_pkg.buy.cpu_purchase(cpu_wallet)
    sleep(1)
    print(f"Round {round} begins!\n")
    # COMBAT PHASE BEGINS
    sleep(1)
    print('''
            ┌───────────────────────┐
            │     Combat Phase      │
            └───────────────────────┘
''')
    sleep(1)
    # COMBAT PHASE ENDS
    round_result[1] = "victory"
    print(f"\nRound {round} ends in {round_result[round]}!")
    sleep(1)
    wallet = val_pkg.buy.player_wallet(wallet, round, round_result[round])
    round += 1
