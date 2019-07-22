#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports:
from tools.system_tools import run_command
from time import time
import os

###############################################################################
#================================= QBC Class =================================#
###############################################################################

class QBC:
    """
    A class used to represent a QBC cirtuit.


    Attributes
    ----------
    n : int
        number of variables
    m : int
        number of intermidiate gates
    output_gate :
        name of the output gate
    prefix : list
        list of tuples containing the prefix
    gates : list
        list of tuples containing the gates
    name : string
        name of the formula for identification purposes
    id_counter : int
        variable to gneerate new id's
    id_to_indext : dict
        dictionary to map identifiers to indices
        
    Methods (WRONG COMMENTS - TO BE CHANGED)
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
        Adds a clause C to the list of clauses. If isNew is True, then the
        variable counter is incremented.
    
    add_quantifier_block(Q, X)
        Adds a quantifier block with quantifier Q and variables X.
    
    get_quantifier_from_block(B)
        Returns the quantifier from a quantifier block B.
    
    get_variables_from_block(B)
        Returns the variables from a quantifier block B.
    
    convert(to='QDIMACS')
        Converts the formula to a string in some standard format, such as
        QDIMACS or QCIR (only QDIMACS supported at the moment).
        
    print_formula(mode='default', output='stdIO', filename=None)
        Prints the formula in the specified mode (normal for 'default' or QDIMACS
        or QCIR otherwise), either in the standard output or onto a text file.
        
    check_satisfiability(self, solver='depqbf', time=True)
        Checks the satisfiability of the formula on a specified QBF solver
        (depqbf if not specified otherwise). Returns on a string the output
        of the solver and the time required to check the satisfiability in seconds.
        This function does not yet run on Windows.
        
    """

    def __init__(self, n, m, output_gate=None, name=""):
        self.n = n # number of variables
        self.m = m # number of gates
        self.output_gate = output_gate
        self.prefix = list() # quantifier vector
        self.gates = list() # gates
        self.name = name # name
        self.id_counter = 0
        self.id_to_index = {}

    def get_n_vars(self):
        return self.n

    def get_n_gates(self):
        return self.m

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_prefix(self):
        return self.prefix

    def get_gates(self):
        return self.gates

    def set_prefix(self, P):
        self.prefix = P

    def set_gates(self, G):
        self.gates = G
        
    def get_output_gate(self):
        return self.output_gate
    
    def set_output_gate(self, G):
        self.output_gate = G   

    def add_gate(self, identifier, op, X, isNew=False):
        if identifier == None:
            identifier = self.obtain_new_id()
        elif identifier in self.id_to_index:
            print("CAUTION: trying to add gate with used name")                                
            
        new_gate = (identifier, op, X)
        self.gates.append(new_gate)
        self.id_to_index[identifier] = len(self.gates) - 1
        
        if isNew:
            self.m += 1
            
    def obtain_new_id(self):
        id_counter += 1
        new_id = 'g' + str(id_counter)
        if new_id not in self.id_to_index:
            return new_id
        else:
            return self.obtain_new_id()

    def add_quantifier_block(self, Q, X):
        self.prefix.append([Q, X])

    def get_quantifier_from_block(self, B):
        return B[0]

    def get_variables_from_block(self, B):
        return B[1]

    def convert(self):
        """
        Converts the circuit to a string enconding in QCIR.
        
        """
        
        phi = self
        converted = ""
        
        # preamble
        converted += "#QCIR-G14\n"
        converted += "# Circuit name: {}\n".format(phi.get_name())
        converted += "# Num. vars.: {}\n".format(phi.get_n_vars())
        converted += "# Num. gates: {}\n".format(phi.get_n_gates())
        
        # quantifiers
        for Q_block in phi.get_prefix():
            block = ""
            Q = phi.get_quantifier_from_block(Q_block)
            if Q == 'e':
                block += "exists("
            else:
                block += "forall("
            
            first = True
            for var in phi.get_variables_from_block(Q_block):
                if first:
                    block += var
                    first = False
                else:
                    block += ", " + var
            block += ")"
            converted += block + "\n"
                    
        # output
        converted += "output(" + phi.get_output_gate() + ")\n"
        
        # gates
        for G in phi.get_gates():
            gate = ""
            gate += G[0] + " = " + G[1]
            gate += "("
            
            first = True
            for sub_gate in G[2]:
                if first:
                    gate += sub_gate
                    first = False
                else:
                    gate += ", " + sub_gate
        
            gate += ")"
            converted += gate + "\n"
        return converted

    def print_formula(self, output='stdIO', filename=None):
        
        result = ""
        result = self.convert()
        
        # Output the formula:
        if output == "stdIO":
            if self.n > 500:
                print("MESSAGE: Cannot print on std. output a formula with more than 500 variables.")
                return
            elif self.m > 500:
                print("MESSAGE: Cannot print on std. output a formula with more than 500 clauses.")
                return
            else:
                print(result)
                
        elif output == "file":
            if filename == None: # default filename
                ext = ".qcir"
                filename = self.name + ext
                
            filename = "./output_files/" + filename
            file = open(filename, 'w')
            file.write(result)
            file.close()
            
        else:
            print("ERROR: Incorrect output selection.")
            return

    def check_satisfiability(self, solver='depqbf', checkTime=True):
        """
        Checks the satisfiability of the formula on a given solver.
        
        NOTE: this method does not yet work on Windows.
        
        -Parameters-:
            - solver: -- 'depqbf' for DepQBF
                      -- [other solvers are not yet supported]
            - checkTime: if True, it will return both the time consumed by the
                        solver as well as the output of the solver.
                        If False, it will just output the result of the
                        solver (times in seconds).
        
        """
        
        if os.name == 'nt':
            print("Running on Windows: cannot check satifiability.")
            return "", 0.0
        
        name = 'checking' + self.name + '.qdimacs'
        name = self.print_formula(mode='QDIMACS', output='file', filename=name)
        
        if checkTime == True:
            t0 = time()
            res = run_command(solver + " " + name)
            t = time() - t0
            return res, t
        else:
            res = run_command(solver + " " + name)
            return res