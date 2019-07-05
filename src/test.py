# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:25:30 2019

@author: noela
"""
from generators.generator_for_T2 import generate_ChenType2
f = generate_ChenType2(5)
#f.print_formula(mode='QDIMACS', output='file', filename='hey')
f.print_formula()