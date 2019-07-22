# -*- coding: utf-8 -*-

from generators.generator_for_T1 import generate_ChenType1

from time import time


print(" === SIMPLE GENERATOR 1 ===")
print("This module will generate Type 1 formulas.")
n = input("[Enter a value for max. n (≥ 1)] ---> n = ")
print("Now, we will generate formulas from n = 1 to {}".format(n))
n = int(n)

filename = "./output_files/" + "times_generate_1.txt"
file = open(filename, 'w')
for i in range(1, n + 1):
    print("Generating... (n = {})".format(i))
    file.write("n = {}\n".format(i))
    t0 = time()
    phi = generate_ChenType1(i)
    t = time() - t0
    print("Complete! ({} s)".format(t))
    file.write(str(t) + "\n")
    phi.print_formula('QDIMACS', 'file')
    
    print("")
    
    
file.close()
    
    


