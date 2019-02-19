# Python code for the minimum fluidization flow rate of the prototype fluidized bed reactor.

# This code assumes the user knows the porosity of the sand used in the fluidized bed. 

# This code makes use of aide_design, a package provided by AguaClara Cornell

# Assumptions: All input values are real numbers.

import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut
from aide_design.play import*

# The following code, determining the bed's minimum flow for fluidization, adheres to the equation in Source 4 in the Fluidization page of the Literature folder (i.e. Fluidization Source 4). The code requests the reactor's cross sectional area in order to calculate the fluidization flow rate at the end of the script.

area_reactor = float(input("\nWhat is the cross sectional area of the fluidized bed reactor, in units of millimeters squared?\n"))*u.mm**2
porosity = float(input("What is the porosity of the sand bed?\n"))

density_sand = float(input("What is the density of the sand, in units of kilograms per cubic meter?\n"))*u.kg/(u.m**3)
density_water = 997*u.kg/(u.m**3)

diameter = float(input("What is the average diameter of the sand grains, in units of millimeters?\n")) * u.mm


g = 9.8 *u.m/(u.s**2)
kozeny = 5 #This is an approximate value, suggested by Fluidization Source 4.
viscosity = float(input("What is the kinematic viscosity of water, in units of millimeters squared per second?\n"))*u.mm**2/u.s

# The following variable definitions are based off those in the equation in Fluidization Source 4.

fluidization_velocity_FirstTerm = (porosity**3 * g * (diameter)**2)/(36*kozeny*(viscosity)*(1-porosity))

fluidization_velocity_SecondTerm = (density_sand/density_water - 1)

fluidization_velocity = fluidization_velocity_FirstTerm * fluidization_velocity_SecondTerm * (1000*u.mm)/(1*u.m)

fluidization_flow = fluidization_velocity * area_reactor * (0.001*u.mL)/(1*u.mm**3)

print("\nThe reactor's fluidization velocity is "+ str(ut.sig(fluidization_velocity,3))+".")
print("The reactor's fluidization flow is "+ str(ut.sig(fluidization_flow,3))+".")
