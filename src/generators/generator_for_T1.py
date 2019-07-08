#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports:
from tools.QBF import QBF

###############################################################################
#============================ GENERATOR FOR TYPE 1 ===========================#
###############################################################################

def generate_ChenType1(n):
    """
    Generates a Type 1 Chen Formula for the value n.
    
    NOTE: this is the only function in this module that should be invoked
          outside of it.
    
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