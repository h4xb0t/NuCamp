#!/usr/bin/env python


def linear_search(the_list, target):
    for x in range(len(the_list)):  # this statement holds index value as x
        if the_list[x] == target:
            print(f"Found at index {x}")
            return x
    print(f"The target is not in the list")
    return -1

# def linear_search(the_list, target):
#     for x in range(len(the_list)):
#         if the_list[x] == target:
#             print("Found at index", x)
#             return x
#     print("Target is not in the list")
#     return -1


my_list = [1, 3, 4, 2, 5, 7]
print(f"{my_list}")
linear_search(my_list, 1)
linear_search(my_list, 3)
linear_search(my_list, 8)
