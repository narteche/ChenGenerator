#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports:
from instance_encodings.QBC import QBC
from itertools import combinations

###############################################################################
#========================== SLOW GENERATOR FOR TYPE 2 ========================#
###############################################################################

def generate_ChenType2(n):
    """
    Generates a Type 2 Chen Formula for the value n.
    
    NOTE: this is the only function in this module that should be invoked
          outside of it.
    
    -Input-: an integer n
    -Precondition-: n ≥ 1
    -Output-: a QBC object
    -Postcondition-: the formula returned is a Chen Formula of Type 2 for size n
    -Cost-: Θ(n)
    """
    
    num_vars = 2*n
    num_gates = 15*n - 11
    phi = QBC(num_vars, num_gates, name="type2_size{}".format(n))

    generate_quantifier_blocks(phi, n)
    generate_gates(phi, n)

    return phi

###############################################################################
###############################################################################

# =================== Internal functions for the generator ================== #

def generate_quantifier_blocks(phi, n):
    """
    Generates the quantifier block on phi.
    
    -Input-: a QBC object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBC object is updated with the prefix quantifier
    vector of a Chen Formula of Type 2 and size n.
    -Cost-: Θ(n)
    """
    
    for i in range(1, n + 1):
        phi.add_quantifier_block('e', ['x' + str(i)])
        phi.add_quantifier_block('a', ['y' + str(i)])
        
def generate_gates(phi, n):
    """
    Generates the gates on the circuit.
    
    -Input-: a QBC object phi and an integer n
    -Precondition-: n ≥ 1
    -Output-: -
    -Postcondition-: the phi QBC object is updated with the appropriate gates
    of a Chen Formula of Type 2 and size n.
    -Cost-: Θ(n)
    """
    
    s_1_0 = 's_{}_{}'.format(1, 0)
    s_1_1 = 's_{}_{}'.format(1, 1)
    s_1_2 = 's_{}_{}'.format(1, 2)
    phi.add_gate(s_1_0, 'and', ['-x' + str(1), '-y' + str(1)])
    phi.add_gate(s_1_1, 'xor', ['x' + str(1), 'y' + str(1)])
    phi.add_gate(s_1_2, 'and', ['x' + str(1), 'y' + str(1)])

    for k in range(2, n + 1):
        
        adder_k_0 = 'adder_{}_{}'.format(k, 0)
        adder_k_1 = 'adder_{}_{}'.format(k, 1)
        adder_k_2 = 'adder_{}_{}'.format(k, 2)
        phi.add_gate(adder_k_0, 'and', ['-x' + str(k), '-y' + str(k)])
        phi.add_gate(adder_k_1, 'xor', ['x' + str(k), 'y' + str(k)])
        phi.add_gate(adder_k_2, 'and', ['x' + str(k), 'y' + str(k)])
        
        for m in [0, 1, 2]:
            
            aux_k_0 = 'aux_{}_{}_{}'.format(k, m, 0)
            aux_k_1 = 'aux_{}_{}_{}'.format(k, m, 1)
            aux_k_2 = 'aux_{}_{}_{}'.format(k, m, 2)
            
            if m == 0:
                phi.add_gate(aux_k_0, 'and', ['s_{}_0'.format(k-1), 'adder_{}_0'.format(k)])
                phi.add_gate(aux_k_1, 'and', ['s_{}_1'.format(k-1), 'adder_{}_2'.format(k)])
                phi.add_gate(aux_k_2, 'and', ['s_{}_2'.format(k-1), 'adder_{}_1'.format(k)])
            elif m == 1:
                phi.add_gate(aux_k_0, 'and', ['s_{}_0'.format(k-1), 'adder_{}_1'.format(k)])
                phi.add_gate(aux_k_1, 'and', ['s_{}_1'.format(k-1), 'adder_{}_0'.format(k)])
                phi.add_gate(aux_k_2, 'and', ['s_{}_2'.format(k-1), 'adder_{}_2'.format(k)])
            else:
                phi.add_gate(aux_k_0, 'and', ['s_{}_0'.format(k-1), 'adder_{}_2'.format(k)])
                phi.add_gate(aux_k_1, 'and', ['s_{}_1'.format(k-1), 'adder_{}_1'.format(k)])
                phi.add_gate(aux_k_2, 'and', ['s_{}_2'.format(k-1), 'adder_{}_0'.format(k)])
                
            s_k_m = 's_{}_{}'.format(k, m)
            phi.add_gate(s_k_m, 'or', [aux_k_0, aux_k_1, aux_k_2])
        
    phi.set_output_gate('-s_{}_{}'.format(n, n % 3))
                