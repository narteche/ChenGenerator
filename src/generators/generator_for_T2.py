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
    
    phi.add_gate(dic[s_1_0], 'and', ['-' + dic['x1'], '-' + dic['y1']])
    
    #phi.add_gate(dic[s_1_1], 'xor', [dic['x1'], dic['y1']])
    phi.add_gate(dic[xor_1], 'and', [dic['x1'], '-' + dic['y1']])
    phi.add_gate(dic[xor_2], 'and', ['-' + dic['x1'], dic['y1']])
    phi.add_gate(dic[s_1_1], 'or', [dic[xor_1], dic[xor_2]])
    
    phi.add_gate(dic[s_1_2], 'and', [dic['x1'], dic['y1']])

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
        
        phi.add_gate(dic[xor_1_k], 'and', [dic['x' + str(k)], '-' + dic['y' + str(k)]])
        phi.add_gate(dic[xor_2_k], 'and', ['-' + dic['x' + str(k)], dic['y' + str(k)]])
        
        phi.add_gate(dic[adder_k_0], 'and', ['-' + dic['x' + str(k)], '-' + dic['y' + str(k)]])
        phi.add_gate(dic[adder_k_1], 'or', [dic[xor_1_k], dic[xor_2_k]])
        phi.add_gate(dic[adder_k_2], 'and', [dic['x' + str(k)], dic['y' + str(k)]])
        
        
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
                phi.add_gate(dic[aux_k_0], 'and', [dic['s_{}_0'.format(k-1)], dic['adder_{}_0'.format(k)]])
                phi.add_gate(dic[aux_k_1], 'and', [dic['s_{}_1'.format(k-1)], dic['adder_{}_2'.format(k)]])
                phi.add_gate(dic[aux_k_2], 'and', [dic['s_{}_2'.format(k-1)], dic['adder_{}_1'.format(k)]])
            elif m == 1:
                phi.add_gate(dic[aux_k_0], 'and', [dic['s_{}_0'.format(k-1)], dic['adder_{}_1'.format(k)]])
                phi.add_gate(dic[aux_k_1], 'and', [dic['s_{}_1'.format(k-1)], dic['adder_{}_0'.format(k)]])
                phi.add_gate(dic[aux_k_2], 'and', [dic['s_{}_2'.format(k-1)], dic['adder_{}_2'.format(k)]])
            else:
                phi.add_gate(dic[aux_k_0], 'and', [dic['s_{}_0'.format(k-1)], dic['adder_{}_2'.format(k)]])
                phi.add_gate(dic[aux_k_1], 'and', [dic['s_{}_1'.format(k-1)], dic['adder_{}_1'.format(k)]])
                phi.add_gate(dic[aux_k_2], 'and', [dic['s_{}_2'.format(k-1)], dic['adder_{}_0'.format(k)]])
                
            s_k_m = 's_{}_{}'.format(k, m)
            counter += 1
            dic[s_k_m] = str(counter)
            phi.add_gate(dic[s_k_m], 'or', [dic[aux_k_0], dic[aux_k_1], dic[aux_k_2]])
    
    
    phi.set_output_gate('-' + dic['s_{}_{}'.format(n, n % 3)])
    # phi.set_output_gate('-s_{}_{}'.format(n, n % 3))
                