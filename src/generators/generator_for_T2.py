# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:52:24 2019

@author: noela
"""
from tools.QBF import QBF
from itertools import combinations

def is_congruent(a, b, n):
    return (a % n) == (b % n)

def generate_ChenType2(n):

    num_vars = 2*n
    num_clauses = 0
    phi = QBF(num_vars, num_clauses, "type2_size{}".format(n))

    generate_quantifier_blocks(phi, n)
    generate_clauses(phi, n)

    return phi

def generate_quantifier_blocks(phi, n):
    
    i = 1
    while i in range(1, 2*n + 1):
        phi.add_quantifier_block('e', [i])
        phi.add_quantifier_block('a', [i + 1])
        i += 2
        
def generate_clauses(phi, n):
    
    for i in range(1, 2*n + 1):
        
        if is_congruent(i, n, 3):
            C = combinations(range(1, 2*n + 1), i)
            
            for comb in C:
                new_clause = list()
                comb_index = 0
                for next_var in range(1, 2*n + 1):
                    if (comb_index in range(len(comb))) and (comb[comb_index] == next_var):
                        new_clause.append(-comb[comb_index])
                        comb_index += 1
                    else:
                        new_clause.append(next_var)
                
                phi.add_clause(new_clause, isNew=True)
                
f = generate_ChenType2(9)
f.print_formula(mode='QDIMACS', output='file', filename='hey')