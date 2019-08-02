#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv

###############################################################################
#============================ GENERATOR FOR TYPE 1 ===========================#
###############################################################################

def generate_ChenType1(n):
    """
    Generates a Type 1 Chen Formula for the value n.
    
    NOTE: this is the only function in this module that should be invoked
          outside of it in case somebody chose to import this file as a module.
    
    -Input-: an integer n
    -Precondition-: n ≥ 1
    -Output-: a QBF object
    -Postcondition-: the formula returned is a Chen Formula of Type 1 for size n
    -Cost-: Θ(n)
    """
    
    num_vars = 9*n + 4
    num_clauses = 12*n + 6
    
    # create the QBF object:
    phi = QBF(num_vars, num_clauses, "type1_size{}".format(n))

    # generate the formula on the object:
    generate_quantifier_blocks(phi, n)
    generate_B_clauses(phi, n)
    generate_H_clauses(phi, n)
    generate_T_clauses(phi, n)

    return phi

###############################################################################
###############################################################################

# =================== Internal functions for the generator ================== #

def encoding_to_index(var_id):
    """
    Converts variables to natural numbers according
    to the bijection defined in the documentation.
    
    -Input-: a tuple of the form (i, jk, 'y' | 'np' | 'p')
    -Precondition-: -
    -Output-: a natural number
    -Postcondition-: the output is a positive natural number that is obtained
    following the mapping defined in the documentation.
    -Cost-: Θ(1)
    """
    
    if var_id[0] == 0: # variables x_0
        return int(var_id[1], 2) + 1
    elif var_id[2] == 'y': # variables y_i
        return (var_id[0]) * 9 + 4
    elif var_id[2] == 'np': # variables x_i
        return (var_id[0] - 1) * 9 + (int(var_id[1], 2) + 1) + 4
    elif var_id[2] == 'p': #variables x'_i
        return (var_id[0] - 1) * 9 + (int(var_id[1], 2) + 1) + 8
    

def generate_quantifier_blocks(phi, n):
    """
    Generates the quantifier block on phi.
    
    -Input-: a QBF object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBF object is updated with the prefix quantifier
    vector of a Chen Formula of Type 1 and size n.
    -Cost-: Θ(n)
    """
    
    # quantifier block for X_0 
    phi.add_quantifier_block('e', [1, 2, 3, 4])

    # rest of quantifier blocks
    for i in range(1, n + 1):
        y_i = (i, None, 'y')
        X_i = list()
        X_i_prime = list()
        for str_j in ['0', '1']:
            for str_k in ['0', '1']:
                x_ijk = (i, str_j + str_k, 'np')
                x_ijk_prime = (i, str_j + str_k, 'p')
                X_i.append(encoding_to_index(x_ijk))
                X_i_prime.append(encoding_to_index(x_ijk_prime))

        Y_i = [encoding_to_index(y_i)]

        phi.add_quantifier_block('e', X_i_prime) # exits X'_i
        phi.add_quantifier_block('a', Y_i) # forall y_i
        phi.add_quantifier_block('e', X_i) # exists X_i


def generate_B_clauses(phi, n):
    """
    Generates the B-clauses on the formula.
    
    -Input-: a QBF object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBF object is updated with the conjunction of the
    appropriate B-clauses or a Chen Formula of Type 1 and size n.
    -Cost-: Θ(1)
    """
    
    B = list()

    for str_j in ['0', '1']:
        for str_k in ['0', '1']:
            new_clause = [-encoding_to_index((0, str_j + str_k, 'np'))]
            B.append(new_clause)

    for str_j in ['0', '1']:
        new_clause = list()
        new_clause.append(encoding_to_index((n, str_j + '0', 'np')))
        new_clause.append(encoding_to_index((n, str_j + '1', 'np')))
        B.append(new_clause)

    for C in B:
        phi.add_clause(C)

def generate_H_clauses(phi, n):
    """
    Generates the H-clauses on the formula.
    
    -Input-: a QBF object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBF object is updated with the conjunction of the
    appropriate H-clauses or a Chen Formula of Type 1 and size n.
    -Cost-: Θ(n)
    """
    
    for i in range(1, n + 1):
        for str_j in ['0', '1']:
            
            H_ij = list()
            
            for str_k in ['0', '1']:
                for str_l in ['0', '1']:
                    
                    new_clause = list()
                    new_clause.append(-encoding_to_index((i, '0' + str_k, 'p')))
                    new_clause.append(-encoding_to_index((i, '1' + str_l, 'p')))
                    new_clause.append(encoding_to_index((i-1, str_j + '0', 'np')))
                    new_clause.append(encoding_to_index((i-1, str_j + '1', 'np')))
                    H_ij.append(new_clause)
                    
            for C in H_ij:
                phi.add_clause(C)

def generate_T_clauses(phi, n):
    """
    Generates the T-clauses on the formula.
    
    -Input-: a QBF object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBF object is updated with the conjunction of the
    appropriate T-clauses or a Chen Formula of Type 1 and size n.
    -Cost-: Θ(n)
    """
    
    for i in range(1, n + 1):
        
        T_i = list()

        for str_k in ['0', '1']:
            new_clause = list()
            new_clause.append(-encoding_to_index((i, '0' + str_k, 'np')))
            new_clause.append(encoding_to_index((i, None, 'y')))
            new_clause.append(encoding_to_index((i, '0' + str_k, 'p')))
            T_i.append(new_clause)

        for str_k in ['0', '1']:
            new_clause = list()
            new_clause.append(-encoding_to_index((i, '1' + str_k, 'np')))
            new_clause.append(-encoding_to_index((i, None, 'y')))
            new_clause.append(encoding_to_index((i, '1' + str_k, 'p')))
            T_i.append(new_clause)

        for C in T_i:
            phi.add_clause(C)
            
# =================== Internal representation for formulas ================== #
###############################################################################
#================================= QBF Class =================================#
###############################################################################

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
        Adds a clause C to the list of clauses. If isNew is True, then the
        variable counter is incremented.
    
    add_quantifier_block(Q, X)
        Adds a quantifier block with quantifier Q and variables X.
    
    get_quantifier_from_block(B)
        Returns the quantifier from a quantifier block B.
    
    get_variables_from_block(B)
        Returns the variables from a quantifier block B.
    
    convert()
        Converts the formula to a string in the QDIMACS format.
        
    print_formula(mode='default', output='stdIO', filename=None)
        Prints the formula in the specified mode (normal for 'default' or QDIMACS
        or QCIR otherwise), either in the standard output or onto a text file.
        
    """

    def __init__(self, n, m, name=""):
        self.n = n # number of variables
        self.m = m # number of clauses
        self.prefix = list() # quantifier vector
        self.clauses = list() # formula matrix
        self.name = name # name

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

    def convert(self):
        """
        Converts the formula to a string enconding in the QDIMACS format.
        """
        
        phi = self
        converted = ""
        
        converted += "c " + phi.get_name() + "\n" #identifier
        converted += "c num. vars.: {}".format(self.get_n_vars()) + "\n"
        converted += "c num. clauses.: {}".format(self.get_n_clauses()) + "\n"
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
        """
        Prints the formula in the desired format.
        
        -Parameters-:
            - mode: -- 'default' for human readability
                    -- 'QDIMACS' for QDIMACS
            - output: -- 'stdIO' for std. output; formulas with more than 100
                      variables and/or clauses will not be printed.
                      -- 'file' for a text file
            - filename: used for the name of the file to be written on; it must
                        include the desired extension. If a name is not
                        specified, the name will be formed using the name of the
                        formula.
        """
        
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

        else:
            print("ERROR: Mode not recognised.")
            return

        # Output the formula:
        if output == "stdIO":
            if self.n > 100:
                print("MESSAGE: Cannot print on std. output a formula with more than 100 variables.")
                return
            elif self.m > 100:
                print("MESSAGE: Cannot print on std. output a formula with more than 100 clauses.")
                return
            else:
                print(result)
                
        elif output == "file":
            if filename == None: # default filename
                ext = ""
                if mode == 'default':
                    ext = ".out"
                elif mode == 'QDIMACS':
                    ext = ".qdimacs"
                    
                filename = self.name + ext
                
            #filename = "./output_files/" + filename
            file = open(filename, 'w')
            file.write(result)
            file.close()
            
        else:
            print("ERROR: Incorrect output selection.")
            return

# ================== Script functions for running generator ================= #
        
def run_generator():
    if len(argv) <= 1:
        return
    elif len(argv) == 2 and argv[1] in ["-help", "--help", "-h", "--h"]:
        print_help()
        return

    args = read_arguments()
    if args == None:
        return
    else:
        n, form, out, filename = args[0], args[1], args[2], args[3]
        phi = generate_ChenType1(n)
        phi.print_formula(form, out, filename)
    
def read_arguments():
    
    if len(argv) not in [2, 3]:
        print_help()
        return None
    
    # Read value for n:
    n = 0
    try:
        n = int(argv[1])
        if (n <= 0):
            raise
    except:
        print("ERROR: First argument must be positive natural value for n.")
        return None
    
   
    # Read output option:
    out = ""
    filename = ""
    if len(argv) == 2:
        out = "stdIO"
    else:
        out = "file"
        try:
            filename = argv[2]
        except:
            print("ERROR: wrong filename.")
            return None
    
    return n, "QDIMACS", out, filename

def print_help():
    print("=== Formula generator for Type 1 Chen Formulas ===")
    print("")
    print("Input should be of the form:")
    print("")
    print("  python3 generateChenType1 n [filename]  ")
    print("")
    print("    n is a positive integer")
    print("    and filename is the name of the file (std. output otherwise)")

# ================================= SCRIPT ================================== #

run_generator()