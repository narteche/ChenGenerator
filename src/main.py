#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:22:56 2019

@author: noel
"""
from time import time
import matplotlib.pyplot as plt
from tools.QBF import QBF
from tools.system_tools import run_command, clear
from generators.generator_for_T1 import generate_ChenType1
import sys
import math

def main_for_user():
    print("=== CHEN FORMULA GENERATOR ===")
    while True:
        print("Select an option:")
        print("     1. Generator for Chen Formulas of Type 1.")
        print("     2. Generator for Chen Formulas of Type 2 [NOT YET IMPLEMENTED].")
        print("     3. Run Type 1 tests repeatedly.")
        print("     4. EXIT.")
        s = input("[SELECT] --> ")
        clear()
        if s == '1':
            run_type1_test()
        elif s == '2':
            run_type2_test()
        elif s == '3':
            run_repeated_tests()
        elif s == '4':
            break
        else:
            print("Incorrect selection; try again.")

    print("END")
    clear()

def run_type1_test():
    clear()
    while True:

        print("Enter a natural value for n (an integer greater or equal than 1):")
        n = input("n = ")
        n = int(n)
        if (n >= 1):
            phi = generate_ChenType1(n)
            phi.print_formula()
            print("Result: ")
            phi.check_satisfiability()
            break
        else:
            clear()
            print("Wrong value for n. Try again.")

def run_type2_test():
    print("TO BE IMPLEMENTED. TRY AGAIN")


def run_repeated_tests():
    while True:
        print("Enter a natural value for n (an integer greater or equal than 1):")
        n = input("n = ")
        n = int(n)
        if (n < 1):
            clear()
            print("Wrong value for n. Try again.")
        
        else:
            
            generate = list()
            solve = list()
            for i in range(1, n):
        
                t0 = time()
                phi = generate_ChenType1(i)
                t = time() - t0
                generate.append(t)
                print("Time for generate size n = {}: {} s".format(i, t))
        
                t, res = phi.check_satisfiability()
                solve.append(t)
                print("Time for solving size n = {}: {} s".format(i, t))
                print(res)
            
            r_n1 =list()
            r_n2 = list()
            r_t = list()
            r_m = list()
            for i in range(1, n):
                r_n1.append(9*i + 4)
                r_n2.append(12*i + 6)
                r_t.append(r_n1[i-1] + r_n2[i-1])
                r_m.append(r_n1[i-1] - r_n2[i-1])
                
            plt.plot(range(1, n), r_n1, 'g^')    
            plt.plot(range(1, n), r_n2, 'bs')
            plt.plot(range(1, n), r_t, 'r+')
            plt.plot(range(1, n), r_m, 'r--')
            plt.show()
            print("FIGURE 1:")
            print("In GREEN: 9n + 4 (rate od growth for the vars.)")
            print("In BLUE: 12n + 6 (rate of growth for the clauses)")
            print("In RED +: the sum of both.")
            print("In RED -: the difference of both.")
            
            plt.plot(range(1, n), generate, 'ro')
            plt.show()
            print("FIGURE 2:")
            print("Time needed to generate the formulas.")
            
            plt.plot(range(1, n), solve, 'ro')
            plt.show()
            print("FIGURE 3: performance of the solver")
            
            r_aprox = list()
            for i in range(1, n):
                r_aprox.append(math.pow(1.001682, i))
            plt.plot(range(1, n), solve, 'ro', range(1, n),r_aprox, 'bs')
            plt.show()
            print("FIGURE 4: performance of the solver VS approximation")
            
            break

main_for_user()
