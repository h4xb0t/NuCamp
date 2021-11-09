#!/usr/bin/env python

my_string = "Valorant"

# Reverses a string
print(my_string[::-1])

# Prints nothing
print(my_string[-1:-5])

# Displays a string in the same format, but starts from the end
print(my_string[-1::])
print(my_string[-2::])
print(my_string[-3::])
print(my_string[-4::])
print(my_string[-8::])

# Really confusing reverse string pieces lol
print(my_string[::-1])


my_string = "butters"

my_list = ["dog", "butters", "terrier"]

# This prints the thrid to last character in my_string
print(my_string[-3])

# This prints my_string backwards
print(my_string[::-1])

# This prints the second item in my_list
print(my_list[1:2])

# THis prints the last character in each entry of my_list
for i in my_list:
    print(i[-1])

# This will print my_list backwards starting from the last entry (-1)
print(my_list[::-1])

# This will print the last two entries in my_list backwards
print(my_list[::-2])

# This prints the last entry in my_list
print(my_list[-1::])

# This prints the last two entries in my_list in list order
print(my_list[-2::])

# This appends my_string to my_list, but spelled backwards
my_list.append(my_string[::-1])
print(my_list)
