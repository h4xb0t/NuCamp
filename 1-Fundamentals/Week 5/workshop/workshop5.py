#!/usr/bin/env python
import random


def guess_random_num(tries, start, stop):
    number = random.randint(start, stop)
    print(number)
    while tries != 0:
        print(f"Tries remaining: {tries}")
        tries -= 1
        guess = int(input("Guess a number: "))
        if guess == number:
            print(f"Wow, you correctly guessed {number}!")
            return
        if guess < number:
            print("Too low, guess higher!")
        if guess > number:
            print("Too high, guess lower!")
        # if tries == 0:
        #     print("Sorry you are out of tries!")
    print("Sorry you are out of tries!")
    print(f"The number was {number}")


def guess_random_num_linear(tries, start, stop):
    number = random.randint(start, stop)
    print(number)
    for i in range(start, stop):
        print(f"Number of tries left: {tries}")
        print(i, number)
        if i == number:
            print(f"The machine guessed {number} correctly!")
            return
        tries -= 1
        if tries == 0:
            print("Sorry you are out of tries!")
            print(f"The number was {number}")
            return


def guess_random_num_binary(tries, start, stop):
    number = random.randint(start, stop)
    num_list = [*range(start, stop + 1)]
    binary_search(num_list, number, tries)


def binary_search(the_list, target, tries):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        print(f"{tries} tries remaining")
        if pivot_value == target:
            print(f"The value {pivot_value} was found by the computer")
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1
        tries -= 1
        if tries == 0:
            print(f"Unable to guess {target}")
            return


# guess_random_num_linear(5, 0, 50)
guess_random_num_binary(5, 0, 50)
