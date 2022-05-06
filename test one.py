#!/usr/bin/env python3

# display a title
print("The miles per gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("enter gallons of gas used:\t\t"))

# calculate and round mpg
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

# display the results
print()
print(f"miles per gallon:\t\t{mpg}")
print()
print("bye!")