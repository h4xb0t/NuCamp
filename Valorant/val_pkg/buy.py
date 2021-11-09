#!/usr/bin/env python
from time import sleep


def player_wallet(wallet, round, round_result):
    '''Player1 Wallet Tracker'''
    if round == 13:
        wallet = 800
        print(f"You have {wallet} credits")
        return wallet
    if round_result == "victory":
        wallet += 2000
        print(f"You have {wallet} credits")
        return wallet
    if round_result == "defeat":
        wallet += 1000
        print(f"You have {wallet} credits")
        return wallet
    if round == 1:
        wallet = 800
        print(f"You have {wallet} credits")
        return wallet
    return wallet


def player_purchase(wallet):
    '''Runs to let the user buy weapons pre-round'''
    while True:
        print("\n ||| Weapons |||\n")
        print("1─►Ghost ----  500")
        print("2─►Judge ---- 1800")
        print("3─►Phantom -- 2900")
        print("4─►Operator - 5000")
        # print(f"You have {wallet} credits")
        weapon = input("\nChoose your weapon: ").lower()
        if weapon in ('1', 'ghost'):
            if wallet >= 500:
                wallet -= 500
                weapon = "ghost"
                print(f"|| Purchased the {weapon}. ||".title())
                sleep(1)
                print(f"{wallet} credits remaining.")
                sleep(1)
                return wallet
            else:
                print("You don't have enough to purchase the Ghost!")
                continue
        if weapon in ('2', 'judge'):
            if wallet >= 1800:
                wallet -= 1800
                weapon = "judge"
                print(f"|| Purchased the {weapon}. ||".title())
                sleep(1)
                print(f"{wallet} credits remaining.")
                sleep(1)
                return wallet
            else:
                print("You don't have enough to purchase the Judge!")
                continue
        if weapon in ('3', 'phantom'):
            if wallet >= 2900:
                wallet -= 2900
                weapon = "phantom"
                print(f"|| Purchased the {weapon}. ||".title())
                sleep(1)
                print(f"{wallet} credits remaining.")
                sleep(1)
                return wallet
            else:
                print("You don't have enough to purchase the Phantom!")
                continue
        if weapon in ('4', 'operator'):
            if wallet >= 5000:
                wallet -= 5000
                weapon = "operator"
                print(f"|| Purchased the {weapon}. ||".title())
                sleep(1)
                print(f"{wallet} credits remaining.")
                sleep(1)
                return wallet
            else:
                print("You don't have enough to purchase the Operator!")
                continue


def cpu_wallet(cpu_wallet, round, last_round_result):
    '''CPU Wallet Tracker'''
    # wallet = 0
    if round == 13:
        cpu_wallet = 800
        return cpu_wallet
    if last_round_result == "victory":
        cpu_wallet += 2000
        return cpu_wallet
    if last_round_result == "defeat":
        cpu_wallet += 800
        return cpu_wallet
    if round == 1:
        cpu_wallet = 800
        return cpu_wallet
    return cpu_wallet


def cpu_purchase(cpu_wallet):
    '''CPU Buy Process'''
    if cpu_wallet >= 5000:
        cpu_weapon = "operator"
    if cpu_wallet >= 2900:
        cpu_weapon = "phantom"
    if cpu_wallet >= 1800:
        cpu_weapon = "judge"
    elif cpu_wallet >= 500:
        cpu_weapon = "ghost"
