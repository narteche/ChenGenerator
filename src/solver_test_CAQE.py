# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 01:35:54 2019

@author: noela
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:21:06 2019

@author: noela
"""

# -*- coding: utf-8 -*-

from tools.system_tools import run_command
from time import time


print(" === SIMPLE CHECKER ===")
print("This module will check Type 2 formulas in QDIMACS format.")
#n = input("[Enter a value for max. n (≥ 1)] ---> n = ")
#n = int(n)

n = 15

filename = "./output_files/" + "caqe_t2_times1.txt"
file = open(filename, 'w')

for i in range(1, n + 1):
    print("Checking on CAQE... (n = {})".format(i))
    t0 = time()
    run_command("./solvers/caqe ./output_files/type2/QDIMACS/type2_size{}_cnf.qdimacs".format(i))
    t = time() - t0
    print("{} s".format(t)) 
    file.write(str(t) + "\n")


file.close()