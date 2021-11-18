#!/usr/bin/env python

def fizzbuzz(num):
    for n in range(1, num):
        if n % 3 == 0 and n % 5 == 0:
            print("Fizzbuzz")
            continue
        if n % 3 == 0:
            print("Fizz")
            continue
        if n % 5 == 0:
            print("Buzz")
            continue
        else:
            print(n)


fizzbuzz(51)
