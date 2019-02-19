# Python code for standard deviation of a list of length 100 or less
# Assumption: All entries are real numbers

# This code makes use of aide_design, a package provided by AguaClara Cornell.

import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut
from aide_design.play import*

print("\n"+"Please input only real numbers; make sure the list is at least two items long! If you're done inputting your list, just type 'done'."+"\n")
values = []
item = "blank"
for n in range(100):
    item = input("What number would you like to add to the list?" +"\n")
    if item == "done":
        break
    else:
        try:
            values.append(float(item))
        except:
            print("It seems like you didn't input a number. Please try again!")

total=0
for n in range(len(values)):
    total += values[n]

average= total / len(values)

numerator = 0
for n in range(len(values)):
    numerator += (values[n]-average)**2

standard_deviation = math.sqrt(numerator / (len(values)-1))

print("The list you've entered has an average value of " + str(ut.sig(average, 4)) +", with a standard deviation of "+ str(ut.sig(standard_deviation, 4))+'.')
