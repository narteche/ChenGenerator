#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools.QBF import QBF

def encoding_to_index(var_id):
    if var_id[0] == 0:
        return int(var_id[1], 2) + 1
    elif var_id[2] == 'y':
        return (var_id[0]) * 9 + 4
    elif var_id[2] == 'np':
        return (var_id[0] - 1) * 9 + (int(var_id[1], 2) + 1) + 4
    elif var_id[2] == 'p':
        return (var_id[0] - 1) * 9 + (int(var_id[1], 2) + 1) + 8


# To be implemented.
def number_to_encoding(var_n):
    return True

def generate_ChenType1(n):

    num_vars = 9*n + 4
    num_clauses = 12*n + 6
    phi = QBF(num_vars, num_clauses, "Type1_size{}".format(n))

    generate_quantifier_blocks(phi, n)
    generate_B_clauses(phi, n)
    generate_H_clauses(phi, n)
    generate_T_clauses(phi, n)

    return phi

def generate_quantifier_blocks(phi, n):

    phi.add_quantifier_block('e', [1, 2, 3, 4])

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

        phi.add_quantifier_block('e', X_i_prime)
        phi.add_quantifier_block('a', Y_i)
        phi.add_quantifier_block('e', X_i)


def generate_B_clauses(phi, n):
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
