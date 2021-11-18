#!/usr/bin/env python

def linear_search_dictionary(my_dict, target):
    for key, value in my_dict.items():
        if value == target:
            print(f"Found {target} at {key}.")
            return key
    print(f"{target} is not in the dictionary")


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
