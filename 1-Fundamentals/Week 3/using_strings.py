#!/usr/bin/env python

my_string = "alpha"

multiline_string = """
this
is
multi
line
"""
# Single index
print(my_string[0])
print(my_string[3])

# Index range in capitals
print(my_string[0:5].upper())


# Print each char
for char in my_string:
    print(char)

# Testing string for conditions
print("pha" in my_string)
print("z" not in my_string)
