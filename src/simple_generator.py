# -*- coding: utf-8 -*-


from tools.system_tools import run_command
from time import time


print(" === SIMPLE GENERATOR ===")
print("This module will generate Type 2 formulas in QDIMACS.")
#n = input("[Enter a value for max. n (≥ 1)] ---> n = ")
#print("Now, we will generate formulas from n = 1 to {}".format(n))
#n = int(n)

n = 5000
#filename = "./output_files/to_cnf_times.txt"
#file = open(filename, 'w')

for i in range(1, n + 1):

    print("Generating n = {}...".format(i))    
    run_command("python3 generate_T1.py {} ./final_formulas/type1/type1_size{}.qdimacs".format(i, i))
    run_command("python3 generate_T2.py {} -QCIR ./final_formulas/type2/QCIR/type2_size{}_circuit.qcir".format(i, i))
    run_command("python3 generate_T2.py {} -QDIMACS ./final_formulas/type2/QDIMACS/type2_size{}_cnf.qdimacs".format(i, i))
    print("Complete!")
    
#file.close()