#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports: 
from tools.system_tools import clear
import tests

def main_menu():
    
    print("========= CHEN FORMULA GENERATOR =========")
    
    while True:
        print("Select an option:")
        print("")
        print("     1. Generator for Chen Formulas of Type 1.")
        print("     2. Generator for Chen Formulas of Type 2.")
        print("     3. Run Type 1 tests repeatedly.")
        print("     4. Run Type 2 tests repeatedly.")
        print("")
        print("     E. EXIT.")
        
        s = input("[SELECT] --> ")
        clear()
        
        if s == '1':
            mode_1()
        elif s == '2':
            mode_2()
        elif s == '3':
            mode_3()
        elif s == '4':
            mode_4()
            
        elif s == 'e' or s == 'E':
            break
        else:
            print("Incorrect selection; try again.")

    clear()
    print("===================== END ======================")
    print("=========== Noel Arteche - July 2019 ===========")


def mode_1():
    clear()
    print(" ----------------- MODE 1 -----------------")
    print("")
    print("This mode will generate and print a Type 1 formula.")
    n = input("[Enter a value for n (≥ 1)] ---> n = ")
    output = input("[Enter 'stdIO' for printing in standard output or a filename for a file] ---> ")
    mode = input("[Enter a format - 'QDIMACS', 'QCIR', 'default'] ---> ")
    checkSat = ("[Select wheter you want to check satisfiability: 'no' or a solver's name] ---> ")
    tests.T1_simple_test(n, output, mode, checkSat)

def mode_2():
    print(" ----------------- MODE 2 -----------------")
    print("")
    print("This mode will generate and print a Type 2 formula.")
    n = input("[Enter a value for n (≥ 1)] ---> n = ")
    output = input("[Enter 'stdIO' for printing in standard output or a filename for a file] ---> ")
    tests.T2_simple_test(n, output)
    
def mode_3():
    clear()
    print(" ----------------- MODE 3 -----------------")
    print("")
    print("This mode will generate and print a large number of formulas and check running times.")
    print("Tests will be performed from n = 1 to any specified value:")
    n = input("[Enter a value for n (≥ 1)] ---> n = ")
    displayData = input("[Do you want data to be displayed? Y / N] ---> ")
    displayData = True if displayData == 'Y' else False
    tests.T1_repeated_tests(n, displayData)

def mode_4():
    print("--- --- --- [TO BE IMPLEMENTED] --- --- ---")

main_menu()
