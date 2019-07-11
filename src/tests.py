#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports:
#from instance_encodings.QBF import QBF
from generators.generator_for_T1 import generate_ChenType1
from generators.generator_for_T2 import generate_ChenType2 
from time import time
import matplotlib.pyplot as plt

def T1_simple_test(n, output, mode, checkSat):
    phi = generate_ChenType1(int(n))
    filename = None
    if output != "stdIO":
        filename = output
        output = 'file'
    phi.print_formula(mode, output, filename)
    if checkSat == "no":
        return
    r, t = phi.check_satisfiability(solver=checkSat)
    print("Satisfiability results: {}, in {} seconds.".format(r, t))
    
def T2_simple_test(n, output):
    phi = generate_ChenType2(int(n))
    filename = None
    if output != "stdIO":
        filename = output
        output = 'file'
    phi.print_formula(output, filename)
    #if checkSat == "no":
    #    return
    #r, t = phi.check_satisfiability(solver=checkSat)
    #print("Satisfiability results: {}, in {} seconds.".format(r, t))
    
def T1_repeated_tests(n, displayData=True):
    n = int(n)
    generate = list()
    solve = list()
    for i in range(1, n + 1):

        print("")
        t0 = time()
        phi = generate_ChenType1(i)
        t = time() - t0
        generate.append(t)
        print("Time for GENERATING with size n = {}: {} s".format(i, t))

        res, t = phi.check_satisfiability()
        solve.append(t)
        print("Time for SOLVING size n = {}: {} s".format(i, t))
        print(res)
    
    if not displayData:
        return
    
    r_n = list()
    r_m = list()
    for i in range(1, n + 1):
        r_n.append(9*i + 4)
        r_m.append(12*i + 6)
        
    plt.plot(range(1, n + 1), r_n, 'g^')    
    plt.plot(range(1, n + 1), r_m, 'bs')
    plt.show()
    print("FIGURE 1:")
    print("In GREEN: 9n + 4 (rate od growth for the vars.)")
    print("In BLUE: 12n + 6 (rate of growth for the clauses)")
    
    plt.plot(range(1, n + 1), generate, 'ro')
    plt.show()
    print("FIGURE 2:")
    print("Time needed to generate the formulas.")
    
    plt.plot(range(1, n + 1), solve, 'ro')
    plt.show()
    print("FIGURE 3: performance of the solver")