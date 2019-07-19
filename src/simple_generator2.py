# -*- coding: utf-8 -*-

from generators.generator_for_T2 import generate_ChenType2

from time import time


print(" === SIMPLE GENERATOR 1 ===")
print("This module will generate Type 2 formulas.")
n = input("[Enter a value for max. n (≥ 1)] ---> n = ")
print("Now, we will generate formulas from n = 1 to {}".format(n))
n = int(n)

filename = "./output_files/" + "times_generate_2.txt"
file = open(filename, 'w')
for i in range(n, n + 1):
    print("Generating... (n = {})".format(i))
    file.write("n = {}\n".format(i))
    t0 = time()
    phi = generate_ChenType2(i)
    t = time() - t0
    print("Complete! ({} s)".format(t))
    file.write(str(t) + "\n")
    phi.print_formula('file')
    
    print("")
    
    
file.close()
    