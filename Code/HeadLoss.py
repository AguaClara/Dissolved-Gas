##This code follows the formula provided by Ambient Pressure & Gas Solubility Source 5.

import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut
from aide_design.play import*

viscosity = float(input("What is the dynamic (i.e. absolute) viscosity of water, in units of millipascal seconds?\n"))*(1/1000) * u.kg/u.m/u.s
effluent_tubing_length = float(input("What is the length of the effluent tubing, in units of meters?\n"))*u.m
velocity = float(input("What is the velocity of water in the effluent piping, in units of meters per second?\n"))*u.m/u.s

density_water = 997*u.kg/(u.m**3)
g = 9.8 *u.m/(u.s**2)
pipe_diameter = float(input("What is the diameter of the effluent piping, in units of meters?\n"))*u.m

Head_Loss = (32 * viscosity * effluent_tubing_length * velocity)/(density_water * g * pipe_diameter**2)

print("The Head Loss due to the effluent tubing is "+ str(ut.sig(Head_Loss,3))+".")
