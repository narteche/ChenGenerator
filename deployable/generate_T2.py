#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv

###############################################################################
#============================ GENERATOR FOR TYPE 2 ===========================#
###############################################################################

def generate_ChenType2(n):
    """
    Generates a Type 2 Chen Formula for the value n.
    
    NOTE: this is the only function in this module that should be invoked
          outside of it in case somebody chose to import this file as a module.
    
    -Input-: an integer n
    -Precondition-: n ≥ 1
    -Output-: a QBC object
    -Postcondition-: the formula returned is a Chen Formula of Type 2 for size n
    -Cost-: Θ(n)
    """
    
    num_vars = 2*n
    num_gates = 0
    phi = QBC(num_vars, num_gates, name="type2_size{}".format(n))
    
    names_to_ints = [{}, 0]
    
    generate_quantifier_blocks(phi, n, names_to_ints)
    generate_gates(phi, n, names_to_ints)

    return phi

###############################################################################
###############################################################################

# =================== Internal functions for the generator ================== #

def generate_quantifier_blocks(phi, n, names_to_ints):
    """
    Generates the quantifier block on phi.
    
    -Input-: a QBC object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBC object is updated with the prefix quantifier
    vector of a Chen Formula of Type 2 and size n.
    -Cost-: Θ(n)
    """
    
    dic = names_to_ints[0]
    counter = names_to_ints[1]
    
    for i in range(1, n + 1):
        counter += 1
        dic['x' + str(i)] = str(counter)
        phi.add_quantifier_block('e', [str(counter)])
        
        counter += 1
        dic['y' + str(i)] = str(counter)
        phi.add_quantifier_block('a', [str(counter)])
        
    names_to_ints[1] = counter
        
def generate_gates(phi, n, names_to_ints):
    """
    Generates the gates on the circuit.
    
    -Input-: a QBC object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBC object is updated with the appropriate gates
    of a Chen Formula of Type 2 and size n.
    -Cost-: Θ(n)
    """
        
    dic = names_to_ints[0]
    counter = names_to_ints[1]
    
    s_1_0 = 's_{}_{}'.format(1, 0)
    s_1_1 = 's_{}_{}'.format(1, 1)
    s_1_2 = 's_{}_{}'.format(1, 2)
    
    counter += 1
    dic[s_1_0] = str(counter)
    counter += 1
    dic[s_1_1] = str(counter)
    counter += 1
    dic[s_1_2] = str(counter)
    
    xor_1 = 'xor_1'
    xor_2 = 'xor_2'
    
    counter += 1
    dic[xor_1] = str(counter)
    counter += 1
    dic[xor_2] = str(counter)
    
    phi.add_gate(dic[s_1_0], 'and', ['-' + dic['x1'], '-' + dic['y1']], True)
    
    #phi.add_gate(dic[s_1_1], 'xor', [dic['x1'], dic['y1']])
    phi.add_gate(dic[xor_1], 'and', [dic['x1'], '-' + dic['y1']], True)
    phi.add_gate(dic[xor_2], 'and', ['-' + dic['x1'], dic['y1']], True)
    phi.add_gate(dic[s_1_1], 'or', [dic[xor_1], dic[xor_2]], True)
    
    phi.add_gate(dic[s_1_2], 'and', [dic['x1'], dic['y1']], True)

    for k in range(2, n + 1):
        
        adder_k_0 = 'adder_{}_{}'.format(k, 0)
        adder_k_1 = 'adder_{}_{}'.format(k, 1)
        adder_k_2 = 'adder_{}_{}'.format(k, 2)
        
        counter += 1
        dic[adder_k_0] = str(counter)
        counter += 1
        dic[adder_k_1] = str(counter)
        counter += 1
        dic[adder_k_2] = str(counter)
        
        xor_1_k = 'xor_1_{}'.format(k)
        xor_2_k = 'xor_2_{}'.format(k)
    
        counter += 1
        dic[xor_1_k] = str(counter)
        counter += 1
        dic[xor_2_k] = str(counter)
        
        phi.add_gate(dic[xor_1_k], 'and', [dic['x' + str(k)], '-' + dic['y' + str(k)]], True)
        phi.add_gate(dic[xor_2_k], 'and', ['-' + dic['x' + str(k)], dic['y' + str(k)]], True)
        
        phi.add_gate(dic[adder_k_0], 'and', ['-' + dic['x' + str(k)], '-' + dic['y' + str(k)]], True)
        phi.add_gate(dic[adder_k_1], 'or', [dic[xor_1_k], dic[xor_2_k]], True)
        phi.add_gate(dic[adder_k_2], 'and', [dic['x' + str(k)], dic['y' + str(k)]], True)
        
        
#        phi.add_gate(adder_k_0, 'and', ['-x' + str(k), '-y' + str(k)])
#        phi.add_gate(adder_k_1, 'xor', ['x' + str(k), 'y' + str(k)])
#        phi.add_gate(adder_k_2, 'and', ['x' + str(k), 'y' + str(k)])
        
        for m in [0, 1, 2]:
            
            aux_k_0 = 'aux_{}_{}_{}'.format(k, m, 0)
            aux_k_1 = 'aux_{}_{}_{}'.format(k, m, 1)
            aux_k_2 = 'aux_{}_{}_{}'.format(k, m, 2)
            
            counter += 1
            dic[aux_k_0] = str(counter)
            counter += 1
            dic[aux_k_1] = str(counter)
            counter += 1
            dic[aux_k_2] = str(counter)
            
            if m == 0:
                phi.add_gate(dic[aux_k_0], 'and', [dic['s_{}_0'.format(k-1)], dic['adder_{}_0'.format(k)]], True)
                phi.add_gate(dic[aux_k_1], 'and', [dic['s_{}_1'.format(k-1)], dic['adder_{}_2'.format(k)]], True)
                phi.add_gate(dic[aux_k_2], 'and', [dic['s_{}_2'.format(k-1)], dic['adder_{}_1'.format(k)]], True)
            elif m == 1:
                phi.add_gate(dic[aux_k_0], 'and', [dic['s_{}_0'.format(k-1)], dic['adder_{}_1'.format(k)]], True)
                phi.add_gate(dic[aux_k_1], 'and', [dic['s_{}_1'.format(k-1)], dic['adder_{}_0'.format(k)]], True)
                phi.add_gate(dic[aux_k_2], 'and', [dic['s_{}_2'.format(k-1)], dic['adder_{}_2'.format(k)]], True)
            else:
                phi.add_gate(dic[aux_k_0], 'and', [dic['s_{}_0'.format(k-1)], dic['adder_{}_2'.format(k)]], True)
                phi.add_gate(dic[aux_k_1], 'and', [dic['s_{}_1'.format(k-1)], dic['adder_{}_1'.format(k)]], True)
                phi.add_gate(dic[aux_k_2], 'and', [dic['s_{}_2'.format(k-1)], dic['adder_{}_0'.format(k)]], True)
                
            s_k_m = 's_{}_{}'.format(k, m)
            counter += 1
            dic[s_k_m] = str(counter)
            phi.add_gate(dic[s_k_m], 'or', [dic[aux_k_0], dic[aux_k_1], dic[aux_k_2]], True)
    
    
    phi.set_output_gate('-' + dic['s_{}_{}'.format(n, n % 3)], True)
    # phi.set_output_gate('-s_{}_{}'.format(n, n % 3))
    
    

# =================== Internal representation for circuits ================== #
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
        variable to generate new id's
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
    
    def set_output_gate(self, G, isNew=False):
        self.output_gate = G   
        if isNew:
            self.m += 1

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
        self.id_counter += 1
        new_id = 'g' + str(self.id_counter)
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

    def convert_to_QCIR(self):
        """
        Converts the circuit to a string enconding in QCIR."
        
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
    
    def convert_to_QDIMACS(self):
        """
        Converts the circuit to a string enconding in QDIMACS."
        
        """
        
        C = self
        phi = QBF(C.get_n_gates() + C.get_n_vars() - 1, 0, name=C.get_name() + "_CNF")
        
        # add basic quantifier blocks
        dic = {}
        counter = 0
        for B in C.get_prefix():
            Q = C.get_quantifier_from_block(B)
            V = C.get_variables_from_block(B)
            X = []
            for v in V:
                counter += 1
                dic[v] = counter
                X.append(counter)
            phi.add_quantifier_block(Q, X)
            
        aux_vars = list()
        
        for G in C.get_gates():
            gate_id = G[0]
            op = G[1]
            V = G[2]
            
            counter += 1
            dic[gate_id] = counter
            aux_vars.append(counter)
            
            c = counter
            
            x = dic[V[0]] if V[0][0] != '-' else dic[V[0][1:]]
            y = dic[V[1]] if V[1][0] != '-' else dic[V[1][1:]]
            z = 0
            if len(V) == 3:
                z = dic[V[2]] if V[2][0] != '-' else dic[V[2][1:]]
            
            
            
            if op == "or":
                phi.add_clause([x, y, z, -c], True)
                phi.add_clause([-x, c], True)
                phi.add_clause([-y, c], True)
                phi.add_clause([-z, c], True)
                
            elif op == "and":
                phi.add_clause([-x, -y, c], True)
                phi.add_clause([x, -c], True)
                phi.add_clause([y, -c], True)
        
        phi.add_quantifier_block('e', aux_vars)
        
        g = C.get_output_gate()
        op = ''
        if g[0] == '-':
            op = "-"
            g = dic[g[1:]]
        phi.add_clause([int(op + str(g))], True)
        
        return phi.convert()

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
        phi = generate_ChenType2(n)
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
    print("  - n is a positive integer")
    print("  - and filename is the name of the file (std. output otherwise)")

# ================================= SCRIPT ================================== #

run_generator()