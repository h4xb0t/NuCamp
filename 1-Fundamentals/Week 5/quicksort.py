#!/usr/bin/env python

my_list = [5, 4, 1, 2, 3]


def sort_part(the_list, lowest_idx, pivot_idx):
    pivot_val = the_list[pivot_idx]

    while pivot_idx != lowest_idx:
        lowest_val = the_list[lowest_idx]

        print(the_list, lowest_val, pivot_val)
        if lowest_val <= pivot_val:
            lowest_idx += 1
        else:
            the_list[lowest_idx] = the_list[pivot_idx-1]
            the_list[pivot_idx] = lowest_val
            the_list[pivot_idx-1] = pivot_val
            pivot_idx -= 1

    return pivot_idx


def quicksort(the_list, lowest_idx, high_idx):
    if lowest_idx > high_idx:
        return

    pivot_idx = sort_part(the_list, lowest_idx, high_idx)
    quicksort(the_list, lowest_idx, pivot_idx-1)
    quicksort(the_list, pivot_idx+1, high_idx)


print(f"My Unsorted List {my_list}")
quicksort(my_list, 0, len(my_list)-1)
print("My Sorted List:", my_list)
