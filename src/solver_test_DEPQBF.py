# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:21:06 2019

@author: noela
"""

# -*- coding: utf-8 -*-

from tools.system_tools import run_command
from time import time


print(" === SIMPLE CHECKER ===")
print("This module will check Type 1 formulas in QDIMACS format.")
#n = input("[Enter a value for max. n (≥ 1)] ---> n = ")
#n = int(n)

n = 1000

filename = "./output_files/" + "depqbf_new_times1.txt"
file = open(filename, 'w')
print("Checking on DEPQBF... (n = {})".format(1))
t0 = time()
run_command("depqbf ./output_files/type1/type1_size{}.qdimacs".format(1))
t = time() - t0
print("{} s".format(t)) 
file.write(str(t) + "\n")

i = 100
while i <= n:
    print("Checking on DEPQBF... (n = {})".format(i))
    t0 = time()
    run_command("depqbf ./output_files/type1/type1_size{}.qdimacs".format(i))
    t = time() - t0
    print("{} s".format(t)) 
    file.write(str(t) + "\n")
    i += 100

file.close()