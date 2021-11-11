#!/usr/bin/env python


# class Player:
#     max_hp = 150
#     weapon = "classic"


# player1 = Player()

# print(player1.max_hp)
# print(player1.weapon)


# class Bot:
#     max_hp = 150
#     weapon = "classic"


# bot = Bot()

# print(bot.max_hp)
# print(bot.weapon)


# class Weapon:
#     classic_dmg = 26
#     ghost_dmg = 36
#     judge_dmg = 45
#     phantom_dmg = 49
#     operator_dmg = 150


# weapon = Weapon()

# print(f"Classic damage is {weapon.classic_dmg}")

# Player.max_hp = 200


# print(player1.max_hp)


# constructor method
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player("Andy", 150)
player2 = Player("Natalee", 125)

print(f"P1: {player1.name} -- HP: {player1.hp} -- SCORE: {player1.score}")
print(f"P2: {player2.name} -- HP: {player2.hp} -- SCORE: {player2.score}")

player2.hp += 25

print(f"P1: {player1.name} -- HP: {player1.hp} -- SCORE: {player1.score}")
print(f"P2: {player2.name} -- HP: {player2.hp} -- SCORE: {player2.score}")
