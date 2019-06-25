#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .system_tools import run_command
import os
from time import time

class QBF:

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

    def set_name(self):
        return self.name

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

    def convert(self):
        phi = self
        converted = ""
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

        return converted

    def print_formula(self, mode='default', output='stdIO', filename=None):
        result = ""
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

        else:
            print("ERROR: Method not recognised.")
            return

        if output == "stdIO":
            if self.n > 100:
                print("MESSAGE: Cannot print a formula with more than 100 variables.")
                return
            else:
                print(result)
        elif output == "file":
            if filename == None:
                filename = self.name + ".txt"

            filename = os.path.join('./output_files', filename)
            file = open(filename, 'w')
            file.write(result)
            file.close()
            return filename
        else:
            print("ERROR: Incorrect output selection.")
            return

    def check_satisfiability(self, solver='depqbf'):
        name = 'forTesting_' + self.name + '.txt'
        name = self.print_formula(mode='QDIMACS', output='file', filename=name)
        t0 = time()
        res = run_command(solver + " " + name)
        t = time() - t0
        return t, res



