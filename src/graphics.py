from tools.plot import plot

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import sympy as sym
from numpy import polyfit


###############################################################################
###############################################################################
########################## Functions for PLOTS ################################
###############################################################################
###############################################################################

def linear(x, a, b):
    return a*x + b

def cuadratic(x, a, b, c):
    return a*np.power(x, 2) + b*x + c

def cubic(x, a, b, c, d):
    return a*np.power(x, 3) + b*np.power(x, 2) + c*x + d

def cuart(x, a, b, c, d, e):
    return a*np.power(x, 4) + b*np.power(x, 3) + c*np.power(x, 2) + d*x + e

def five(x, o, a, b, c, d, e):
    return o * np.power(x, 5) + a*np.power(x, 4) + b*np.power(x, 3) + c*np.power(x, 2) + d*x + e

def expo(x, a, b):
    #return a * (np.exp(b*x))
    return a * (np.exp2(b*x))

###############################################################################
###############################################################################
    
# Chargin data:
    
filename = "./output_files/times/type2/" + "cqesto_times.txt"
file = open(filename, 'r')

y = list()
for line in file:
    t = float(line)
    #t = t * 100.0
    y.append(t)
    
print("DATA:")
print(y)
x = list()
i = 0
while i<= 600:
    x.append(i)
    i += 100
x[0] = 1
print(x)


filename = "./output_files/times/type2/" + "quabs_times.txt"
file = open(filename, 'r')

yd = list()
for line in file:
    t = float(line)
    #t = t * 100.0
    yd.append(t)
    
yd = yd[:7]
print("DATA:")
print(yd)
xd = list()
i = 0
while i<= 600:
    xd.append(i)
    i += 100
xd[0] = 1
print(x)

# Original data
beingsaved = plt.figure()
plt.plot(x, y, 'ro', label="CQESTO")
plt.plot(x, y, 'b')
plt.plot(xd, yd, 'rx', label="QUABS")
plt.plot(xd, yd, 'b')


plt.xlabel('Size (n)', fontsize=10)
plt.ylabel('Time (s)', fontsize='medium') 
plt.show()
beingsaved.savefig('quabs.svg', format='svg', dpi=1200)

# Polynomials
p1 = polyfit(np.asarray(x[:5]), np.asarray(y[:5]), 1)
p2 = polyfit(np.asarray(x[:5]), np.asarray(y[:5]), 2)
p3 = polyfit(np.asarray(x[:5]), np.asarray(y[:5]), 3)
p4 = polyfit(np.asarray(x[:5]), np.asarray(y[:5]), 4)
p5 = polyfit(np.asarray(x[:4]), np.asarray(y[:4]), 5)
#exp, g = curve_fit(expo, np.asarray(x[:6]), np.asarray(y[:6]))

# Coefficients:
print(p1)
print(p2)
print(p3)
print(p4)
print(exp)

beingsaved = plt.figure()
plt.plot(x, y, 'ro',label="Original Data")
#plt.plot(np.asarray(x), linear(np.asarray(x), *p1), label="Linear")
plt.plot(np.asarray(x), cuadratic(np.asarray(x), *p2), label="Cuadratic")
plt.plot(np.asarray(x), cubic(np.asarray(x), *p3), label="Cubic")
plt.plot(np.asarray(x), cuart(np.asarray(x), *p4), label="Fourth")
plt.plot(np.asarray(x), five(np.asarray(x), *p5), label="Fifth")
#plt.plot(np.asarray(x), expo(np.asarray(x), *exp), label="Exp")
plt.xlabel('Size (n)', fontsize=10)
plt.ylabel('Time (s)', fontsize='medium') 
plt.legend(loc='upper left')
plt.show()
beingsaved.savefig('compare.svg', format='svg', dpi=1200)



#filename2 = "./output_files/times/type1/" + "depqbf_new_times2.txt"
#filename3 = "./output_files/times/type1/" + "depqbf_new_times3.txt"
#file1 = open(filename1, 'r')
#file2 = open(filename2, 'r')
#file3 = open(filename3, 'r')
#
#file = open("./output_files/" + "latest_depqbf_times.txt", 'w')
#
#for line1 in file1:
#    
#    line2 = file2.readline()
#    line3 = file3.readline()
#    
#    t = float(line1) + float(line2) + float(line3)
#    t = t / 3
#    
#    file.write(str(t) + '\n')
#    
#file.close()
#file1.close()
#file2.close()
#file3.close()