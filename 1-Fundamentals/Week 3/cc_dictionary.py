#!/usr/bin/env python

inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    '''Prints the total inches of snow throughout the week, by day'''
    total_inches = 0
    for days, inches in inches_snow.items():
        total_inches += inches
        print(f"Total snowfall through {days} is inches: {total_inches}")


print_total_snowfall(inches_snow)

inches_snow["Thursday"] = int(input("How much snow fell on Thursday?: "))

print_total_snowfall(inches_snow)
