# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import sympy as sym

def plot(func, x, y):
    
    """
    brutal force to avoid errors
    """    
    x = np.array(x, dtype=float) #transform your data in a numpy array of floats 
    y = np.array(y, dtype=float) #so the curve_fit can work
    """
    Plot your data
    """
    #plt.plot(x, y, 'ro',label="Original Data")
    #plt.show()
    
    #"""
    #Generate some data, let's imagine that you already have this. 
    #"""
    #
    #x = np.linspace(0, 3, 50)
    #y = np.exp(x)
    
    """
    Plot your data
    """
    plt.plot(x, y, 'ro',label="Original Data")
    

    
    """
    create a function to fit with your data. a, b, c and d are the coefficients
    that curve_fit will calculate for you. 
    In this part you need to guess and/or use mathematical knowledge to find
    a function that resembles your data
    """
    #def func(x, a, b, c, d):
    #    return a*(b**(c*x)) + d

    """
    make the curve_fit
    """
    popt, pcov = curve_fit(func, x, y)
    print(popt)
    print(*popt)
    
    """
    The result is:
    popt[0] = a , popt[1] = b, popt[2] = c and popt[3] = d of the function,
    so f(x) = popt[0]*x**3 + popt[1]*x**2 + popt[2]*x + popt[3].
    """
    
    
    """
    Use sympy to generate the latex sintax of the function
    """
    xs = sym.Symbol('n')    
    tex = sym.latex(func(xs,*popt)).replace('$', '')
    plt.title(r'$f(n)= %s$' %(tex),fontsize=16)
    
    """
    Print the coefficients and plot the funcion.
    """
    
    plt.plot(x, func(x, *popt), label="Fitted Curve") #same as line above \/
    #plt.plot(x, popt[0]*x**3 + popt[1]*x**2 + popt[2]*x + popt[3], label="Fitted Curve") 
    
    plt.legend(loc='upper left')
    
    plt.show()
    
    
    return popt
