#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Apr 29 14:04:50 2019

@author: Bakari Mustafa
"""
print("This is a program to model the population of fish over time, with a growth rate of 0.05.")

# growth value
r = 0.05

# initial number of fish
init = float(input("Input the initial number of fish: "))

# carrying capacity
capacity = float(input("Input the carrying capacity of the fish population: "))

# number of years to project for
years = float(input("Input the number of years to be modelled: "))

print("Year", ' ' , "Number of Fish")

fish = init
i = 1
while i <= years:
    fish = init + r * init * (1 - (init / capacity))
    print(i, "  -  ", round(fish))
    i = i + 1

print("The fish population changed by", round(abs(fish - init)), "fish in", years, "years.")
print("Press the RUN icon to start the program again.")
