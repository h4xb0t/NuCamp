#!/usr/bin/env python
from time import sleep
unsorted_list = [101, 202, 316, 3, 56, 18, 21, 46, 126, 912]


def bubblesort(the_list):
    last_idx = len(the_list) - 1

    for i in range(last_idx):
        list_changed = False
        for j in range(last_idx):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True
                sleep(.5)
            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break


bubblesort(unsorted_list)
