#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 09:33:52 2021

@author: i_atkin
"""

from pylab import *
from scipy.optimize import fsolve
from scipy.constants import *
import math 
import numpy as np 

# Constants
V = 1.6022e-16
a = 0.529e-10

# The function 

K = np.sqrt((2*m_e*(a**2)*V)/(hbar**2))

#print(x)

def left(s):
    return s*((np.cos(s))/np.sin(s))

def right(s):
    return -np.sqrt((K**2)-(s**2))

def tot(s):
    return left(s) - right(s)

# preparing to plot the functions, for which values of s are they equal 
# values from -K to 0 are called "degenerative states"
    
s = linspace(0, K, 1000)

side1 = left(s)
side2 = right(s)

# Plot the result 
# define the figure window to use
figure(1)
# clear the current figure window 
clf()

plot(s, side1, "-r")
plot(s, side2)
xlabel("s")
ylabel("functions")

x = fsolve(tot, 3.5)
y = fsolve(tot, 5.5)
z = fsolve(tot, 8)

print(x, y, z)


E1 = V*(((x**2)/(K**2)) - 1) / e 
E2 = V*(((y**2)/(K**2)) - 1) / e
E3 = V*(((z**2)/(K**2)) - 1) / e

print(E1, E2, E3)

#Energies are -892, -596, -92 eV
