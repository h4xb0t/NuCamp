#!/usr/bin/env python

import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    card_pick = input(
        "Press enter to pick a card, or type Q then hit enter to quit: ").lower()
    if card_pick == "q":
        break
    else:
        rand_card = random.choice(diamonds)
        diamonds.remove(rand_card)
        hand.append(rand_card)
        print(f"Your hand: {hand}")
        print(f"Remaining cards: {diamonds}")
if not diamonds:
    print("There are no more cards to pick.")
