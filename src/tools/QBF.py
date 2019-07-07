#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .system_tools import run_command
from time import time
import os

class QBF:
    """
    A class used to represent a QBF formula in prenex CNF.


    Attributes
    ----------
    n : int
        number of variables
    m : int
        number of clauses
    prefix : list
        list of tuples representing the quantifier blocks; for instance, the
        quantifier block ƎxƎy is represented with ('e', [1, 2]) provided that
        1 and 2 are the integers representing x and y
    clauses : list
        list of lists containing the clauses; a clause like [1, 2, 4] represents
        the disjunction of those three variables
    name : string
        name of the formula for identification purposes

    Methods
    -------
    get_n_vars()
        Returns the number of variables.
        
    get_n_clauses()
        Returns the number of clauses.
    
    get_name()
        Returns the name of the object.
    
    set_name(name)
        Sets the name of the formula to 'name'.
    
    get_prefix()
        Returns the prefix of the formula.
        
    get_clauses()
        Returns the list of clauses of the formula.
        
    set_prefix(P)
        Sets a new prefix P for the formula.
        
    set_clauses(phi)
        Sets a new list of clauses for the formula.
    
    add_clause(C, isNew=False)
        Adds a clause C to the list of clauses. If isNew=True, then the variable
        counter is incremented.
    
    add_quantifier_block(Q, X)
        Adds a quantifier block with quantifier Q and variables X.
    
    get_quantifier_from_block(B)
        Returns the quantifier from a quantifier block B.
    
    get_variables_from_block(B)
        Returns the variables from a quantifier block B.
    
    convert(to='QDIMACS')
        Converts the formula to a string in some standard format, such as
        QDIMACS or QCIR.
        
    print_formula(mode='default', output='stdIO', filename=None)
        Prints the formula in the specified mode (normal for 'default' or QDIMACS
        or QCIR otherwise), either in the standard output or onto a text file.
        
    check_satisfiability(self, solver='depqbf')
        Checks the satisfiability of the formula on a specified QBF solver
        (depqbf if not specified otherwise). Returns on a string the output
        of the solver and the time required to check the satisfiability in seconds.
        This function does not yet run on Windows.
        
    """

    def __init__(self, n, m, name=""):
        self.n = n
        self.m = m
        self.prefix = list()
        self.clauses = list()
        self.name = name

    def get_n_vars(self):
        return self.n

    def get_n_clauses(self):
        return self.m

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_prefix(self):
        return self.prefix

    def get_clauses(self):
        return self.clauses

    def set_prefix(self, P):
        self.prefix = P

    def set_clauses(self, phi):
        self.clauses = phi

    def add_clause(self, C, isNew=False):
        self.clauses.append(C)
        if isNew:
            self.m += 1

    def add_quantifier_block(self, Q, X):
        self.prefix.append([Q, X])

    def get_quantifier_from_block(self, B):
        return B[0]

    def get_variables_from_block(self, B):
        return B[1]

    def convert(self, to='QDIMACS'):
        phi = self
        converted = ""
        
        if to == 'QDIMACS':
            converted += "p cnf {} {}\n".format(phi.get_n_vars(), phi.get_n_clauses())

            for Q_block in phi.get_prefix():
                block = phi.get_quantifier_from_block(Q_block)
                for var in phi.get_variables_from_block(Q_block):
                    block += " " + str(var)
                block += " 0"
                converted += block + "\n"
    
            for C in phi.get_clauses():
                clause = ""
                for lit in C:
                    clause += str(lit) + " "
                clause += "0"
                converted += clause + "\n"
        
        elif to == 'QCIR':
            print("QCIR conversion not yet implemented.")
        
        else:
            print("ERROR: unknown conversion format.")

        return converted

    def print_formula(self, mode='default', output='stdIO', filename=None):
        result = ""
        
        # Convert the formula to a string.
        if mode == 'default':
            result += self.name + '\n'
            result += "Variables: {}\n".format(self.n)
            result += "Clauses: {}\n".format(self.m)

            for Q in self.prefix:
                block = "Ǝ" if Q[0] == 'e' else "∀"
                for var in Q[1]:
                    block += " " + str(var) + ","
                result += block[:len(block)-1] + "\n"

            count = 0
            for C in self.clauses:
                count += 1
                line = "("
                for lit in C:
                    neg = "¬" if lit < 0 else ""
                    line += neg + str(abs(lit)) + " ∨ "
                line = line[:len(line) - 3]
                line += ") ∧"
                if count == self.m:
                    line = line[:len(line) - 2]
                result += line + "\n"

        elif mode == 'QDIMACS':
            result = self.convert()
        
        elif mode == 'QCIR':
            result= self.convert(to='QCIR')

        else:
            print("ERROR: Method not recognised.")
            return

        # Output the formula:
        if output == "stdIO":
            if self.n > 100:
                print("MESSAGE: Cannot print on StdO a formula with that many variables.")
                return
            else:
                print(result)
                
        elif output == "file":
            if filename == None:
                filename = self.name + ".txt" # should change this to .qdimacs or .qcir

            filename = "./output_files/" + filename
            file = open(filename, 'w')
            file.write(result)
            file.close()
        else:
            print("ERROR: Incorrect output selection.")
            return

    def check_satisfiability(self, solver='depqbf'):
        name = 'forTesting_' + self.name + '.txt'
        name = self.print_formula(mode='QDIMACS', output='file', filename=name)
        if os.name == 'nt':
            print("Running on Windows: cannot check satifiability.")
            return
        t0 = time()
        res = run_command(solver + " " + name)
        t = time() - t0
        return t, res



