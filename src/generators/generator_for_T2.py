#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports:
from tools.QBF import QBF
from itertools import combinations

###############################################################################
#========================== SLOW GENERATOR FOR TYPE 2 ========================#
###############################################################################

def generate_ChenType2(n):

    num_vars = 2*n
    num_clauses = 0 # to be updated later
    phi = QBF(num_vars, num_clauses, "type2_size{}".format(n))

    generate_quantifier_blocks(phi, n)
    generate_clauses(phi, n)

    return phi

###############################################################################
###############################################################################

# =================== Internal functions for the generator ================== #
    
def is_congruent(a, b, n):
    """
    Checks whether a is congruent with b mod n.
    
    -Input-: integers a, b and n
    -Precondition-: a, b ≥ 0, n ≥ 1
    -Output-: Boolean value
    -Postcondition-: returns True iff a ≡ b (mod n)
    -Cost-: Θ(1)
    """
    
    return (a % n) == (b % n)

def generate_quantifier_blocks(phi, n):
    """
    Generates the quantifier block on phi.
    
    -Input-: a QBF object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBF object is updated with the prefix quantifier
    vector of a Chen Formula of Type 2 and size n.
    -Cost-: Θ(n)
    """
    
    i = 1
    while i in range(1, 2*n + 1):
        phi.add_quantifier_block('e', [i])
        phi.add_quantifier_block('a', [i + 1])
        i += 2
        
def generate_clauses(phi, n):
    """
    Generates the clauses on the formula.
    
    -Input-: a QBF object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBF object is updated with the conjunction of the
    appropriate clauses of a Chen Formula of Type 2 and size n.
    -Cost-: Θ(4^n)
    """
    
    for i in range(0, 2*n + 1):
        if is_congruent(i, n, 3):
            for comb in combinations(range(1, 2*n + 1), i):
                new_clause = list(range(1, 2*n + 1))
                for var in comb:
                    new_clause[var - 1] = -var
                phi.add_clause(new_clause, isNew=True)
                