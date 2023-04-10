#!/usr/bin/env python
'''This module is for the buy phase'''
from time import sleep
import random

def player_wallet(wallet, round, round_result):
    '''Player Wallet Tracker'''
    if round == 12:
        wallet = 800
        print(f"\nYou have {wallet} credits")
        return wallet
    if round_result == "victory":
        wallet += 2000
        if wallet >= 16000:
            wallet = 16000
        print(f"\nYou have {wallet} credits")
        return wallet
    if round_result == "defeat":
        wallet += 1000
        if wallet >= 16000:
            wallet = 16000
        print(f"\nYou have {wallet} credits")
        return wallet
    if round == 1:
        wallet = 800
        print(f"\nYou have {wallet} credits")
        return wallet
    return wallet


def agent_select():
    '''Agent Select'''
    while True:
        print("1─► Jett")
        print("2─► Phoenix")
        print("3─► Sage")
        print("4─► Brimstone")
        print("5─► Sova")
        agent_choice = input("\nSelect your agent: ").lower()
        if agent_choice in ("1", "jett"):
            agent = "Jett"
            break
        if agent_choice in ("2", "phoenix"):
            agent = "Phoenix"
            break
        if agent_choice in ("3", "sage"):
            agent = "Sage"
            break
        if agent_choice in ("4", "brimstone"):
            agent = "Brimstone"
            break
        if agent_choice in ("5", "sova"):
            agent = "Sova"
            break
        else:
            print("\nPlease choose an agent\n")
            continue
    print(f"\n|| You have chosen {agent}. ||\n")
    sleep(1)
    return agent


def player_purchase(wallet):
    '''Runs to let the user buy weapons pre-round'''
    while True:
        print("\n ||| Weapons |||\n")
        print("1─► Ghost ----  500")
        print("2─► Judge ---- 1800")
        print("3─► Phantom -- 2900")
        print("4─► Operator - 5000")
        if hasattr(player_purchase, 'weapon'):
            print("5─► Keep Current --")
        weapon = input("\nSelect your weapon: ").lower()
        if weapon in ('1', 'ghost'):
            if wallet >= 500:
                wallet -= 500
                weapon = "ghost"
                player_purchase.weapon = "ghost"
                print(f"\n|| Purchased the {weapon}. ||".title())
                sleep(1)
                print(f"\nYou have {wallet} credits remaining.")
                sleep(1)
                return wallet
            else:
                print("\nYou don't have enough to purchase the Ghost!")
                continue
        if weapon in ('2', 'judge'):
            if wallet >= 1800:
                wallet -= 1800
                weapon = "judge"
                player_purchase.weapon = "judge"
                print(f"\n|| Purchased the {weapon}. ||".title())
                sleep(1)
                print(f"\nYou have {wallet} credits remaining.")
                sleep(1)
                return wallet
            else:
                print("\nYou don't have enough to purchase the Judge!")
                continue
        if weapon in ('3', 'phantom'):
            if wallet >= 2900:
                wallet -= 2900
                weapon = "phantom"
                player_purchase.weapon = "phantom"
                print(f"\n|| Purchased the {weapon}. ||".title())
                sleep(1)
                print(f"\nYou have {wallet} credits remaining.")
                sleep(1)
                return wallet
            else:
                print("\nYou don't have enough to purchase the Phantom!")
                continue
        if weapon in ('4', 'operator'):
            if wallet >= 5000:
                wallet -= 5000
                weapon = "operator"
                player_purchase.weapon = "operator"
                print(f"\n|| Purchased the {weapon}. ||".title())
                sleep(1)
                print(f"\nYou have {wallet} credits remaining.")
                sleep(1)
                return wallet
            else:
                print("\nYou don't have enough to purchase the Operator!")
                continue
        if weapon in ('5', 'keep', 'current'):
            weapon = player_purchase.weapon
            print("\n|| Keeping current weapon. ||")
            sleep(1)
            print(f"\nYou have {wallet} credits remaining.")
            sleep(1)
            return wallet
        else:
            print("\nYou don't have a weapon to keep!")
            continue


def bot_wallet_func(bot_wallet, round, round_result):
    '''bot Wallet Tracker'''
    if round == 13:
        bot_wallet = 800
        return bot_wallet
    if round_result == "victory":
        bot_wallet += 2000
        if bot_wallet >= 16000:
            bot_wallet = 16000
        return bot_wallet
    if round_result == "defeat":
        bot_wallet += 1000
        if bot_wallet >= 16000:
            bot_wallet = 16000
        return bot_wallet
    if round == 1:
        bot_wallet = 800
        return bot_wallet
    return bot_wallet


def bot_purchase(bot_wallet, round_result):
    '''bot Buy Process'''
    # UPDATED: Add a list of available weapons with costs
    weapons = {
        "ghost": 500,
        "judge": 1800,
        "phantom": 2900,
        "operator": 5000,
    }

    # UPDATED: Randomize the keep_probability value
    keep_probability = random.uniform(0, 1)  # Generates a random float between 0 and 1

    # UPDATED: Check if the bot has a weapon and won the previous round
    if (random.random() < keep_probability and hasattr(bot_purchase, 'bot_weapon') and
            round_result.get(len(round_result), "") == "defeat"):
        # Keep the current weapon
        print("\n|| Bot is keeping its current weapon. ||")
        return bot_wallet
    else:
        # Buy a new weapon
        for weapon, cost in sorted(weapons.items(), key=lambda x: x[1], reverse=True):
            if bot_wallet >= cost:
                bot_wallet -= cost
                bot_purchase.bot_weapon = weapon
                return bot_wallet
    return bot_wallet



# def bot_purchase(bot_wallet):
#     '''bot Buy Process'''
#     if bot_wallet >= 5000:
#         bot_wallet -= 5000
#         bot_purchase.bot_weapon = "operator"
#         return bot_wallet
#     if bot_wallet >= 2900:
#         bot_wallet -= 2900
#         bot_purchase.bot_weapon = "phantom"
#         return bot_wallet
#     if bot_wallet >= 1800:
#         bot_wallet -= 1800
#         bot_purchase.bot_weapon = "judge"
#         return bot_wallet
#     elif bot_wallet >= 500:
#         bot_wallet -= 500
#         bot_purchase.bot_weapon = "ghost"
#         return bot_wallet
#     return bot_wallet

# maybe can check weapon existing i.e. if weapon == ghost; then weapon == ghost
