#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:22:56 2019

@author: noel
"""
from tools.QBF import QBF
from tools.system_tools import run_command, clear
from generators.generator_for_T1 import generate_ChenType1
import sys

def main_for_user():
    print("=== CHEN FORMULA GENERATOR ===")
    while True:
        print("Select an option:")
        print("     1. Generator for Chen Formulas of Type 1.")
        print("     2. Generator for Chen Formulas of Type 2 [NOT YET IMPLEMENTED].")
        print("     3. EXIT.")
        s = input("[SELECT] --> ")
        clear()
        if s == '1':
            run_type1_test()
        elif s == '2':
            run_type2_test()
        elif s == '3':
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

main_for_user()
