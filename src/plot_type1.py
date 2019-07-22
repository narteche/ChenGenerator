from tools.plot import plot

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import sympy as sym


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

def expo(x, a, b):
    return np.power(a,x) + b

###############################################################################
###############################################################################

#### GENERATION TIMES ####
    
times = []

filename1 = "./output_files/times/" + "type2_generate1.txt"
filename2 = "./output_files/times/" + "type2_generate2.txt"
filename3 = "./output_files/times/" + "type2_generate3.txt"
file1 = open(filename1, 'r')
file2 = open(filename2, 'r')
file3 = open(filename3, 'r')

for line1 in file1:

    t1 = float(file1.readline())
    file2.readline()
    t2 = float(file2.readline())
    file3.readline()
    t3 = float(file3.readline())
    
    t = (t1 + t2 + t3) / 3
    times.append(t)

file1.close()
file2.close()
file3.close()

gen_times = times

beingsaved = plt.figure()
plot(linear, range(1, len(gen_times) + 1), gen_times)
beingsaved.savefig('gen2.svg', format='svg', dpi=1200)
#### DEPQBF ####

# Firstly, we plot the 500 first values on DEPQBF:

filename1 = "./output_files/times/" + "type1_depqbf1.txt"
filename2 = "./output_files/times/" + "type1_depqbf2.txt"
filename3 = "./output_files/times/" + "type1_depqbf3.txt"
file1 = open(filename1, 'r')
file2 = open(filename2, 'r')
file3 = open(filename3, 'r')

n = 1
x = list()
y = list()
for line1 in file1:
    if n > 500:
        break
    line2 = file2.readline()
    line3 = file3.readline()
        
    if line1 == "NOT CHECKED\n":
        n += 1
        continue
   
    t1 = float(line1)
    t2 = float(line2)
    t3 = float(line3)
    
    t = (t1 + t2 + t3) / 3
    x.append(n)
    y.append(t)
    
    n += 1
    
file1.close()
file2.close()
file3.close()

# We plot them with corresponding approximations:
pexp = plot(expo, x, y)
p2 = plot(cuadratic, x, y)
p3 = plot(cubic, x, y)
p4 = plot(cuart, x, y)

# We plot again but from 1 to 1000:
filename1 = "./output_files/times/" + "type1_depqbf1.txt"
filename2 = "./output_files/times/" + "type1_depqbf2.txt"
filename3 = "./output_files/times/" + "type1_depqbf3.txt"
file1 = open(filename1, 'r')
file2 = open(filename2, 'r')
file3 = open(filename3, 'r')

n = 1
x = list()
y = list()
for line1 in file1:
    line2 = file2.readline()
    line3 = file3.readline()
        
    if line1 == "NOT CHECKED\n":
        n += 1
        continue
   
    t1 = float(line1)
    t2 = float(line2)
    t3 = float(line3)
    
    t = (t1 + t2 + t3) / 3
    x.append(n)
    y.append(t)
    
    n += 1
    
file1.close()
file2.close()
file3.close()



# Now, these are comparison graphs: we plot the 1000 data with previous approx.
plt.plot(x, y, 'ro',label="Original Data")
plt.plot(np.asarray(x), cuadratic(np.asarray(x), *p2), label="Cuadratic")
plt.plot(np.asarray(x), cubic(np.asarray(x), *p3), label="Cubic")
plt.plot(np.asarray(x), cuart(np.asarray(x), *p4), label="Fourth")
plt.plot(np.asarray(x), expo(np.asarray(x), *pexp), label="Exp")
plt.legend(loc='upper left')

plt.show()




# And additional complete approximations:
pexp = plot(expo, x, y)
p2 = plot(cuadratic, x, y)
p3 = plot(cubic, x, y)
p4 = plot(cuart, x, y)

# Now, we plot for 5000 values and compare against the best approx. we have:
filename = "./output_files/times/" + "type1_depqbf5000.txt"
file = open(filename, 'r')

n = 1
x = list()
y = list()
for line in file:
        
    if line == "NOT CHECKED\n":
        n += 1
        continue
   
    t = float(line)

    x.append(n)
    y.append(t)
    
    n += 1
    
file.close()

plt.plot(x, y, 'ro',label="Original Data")
plt.plot(np.asarray(x), cuadratic(np.asarray(x), *p2), label="Cuadratic")
plt.plot(np.asarray(x), cubic(np.asarray(x), *p3), label="Cubic")
plt.plot(np.asarray(x), cuart(np.asarray(x), *p4), label="Fourth")
#plt.plot(np.asarray(x), expo(np.asarray(x), *pexp), label="Exp")
plt.legend(loc='upper left')


plt.show()



pexp = plot(expo, x, y)
beingsaved = plt.figure()
p2 = plot(cuadratic, x, y)
beingsaved.savefig('cuadratic1.svg', format='svg', dpi=1200)

beingsaved = plt.figure()
p3 = plot(cubic, x, y)
beingsaved.savefig('cubic1.svg', format='svg', dpi=1200)
beingsaved = plt.figure()

p4 = plot(cuart, x, y)
beingsaved.savefig('fourth1.svg', format='svg', dpi=1200)

###############################################################################

#### CAQE ####


filename1 = "./output_files/times/" + "type1_caqe1.txt"
filename2 = "./output_files/times/" + "type1_caqe2.txt"
filename3 = "./output_files/times/" + "type1_caqe3.txt"
file1 = open(filename1, 'r')
file2 = open(filename2, 'r')
file3 = open(filename3, 'r')

n = 1
x = list()
y = list()
for line1 in file1:
    line2 = file2.readline()
    line3 = file3.readline()
        
    if line1 == "NOT CHECKED\n":
        n += 1
        continue
   
    t1 = float(line1)
    t2 = float(line2)
    t3 = float(line3)
    
    t = (t1 + t2 + t3) / 3
    x.append(n)
    y.append(t)
    
    n += 1
    
file1.close()
file2.close()
file3.close()

beingsaved = plt.figure()
plot(expo, x, y)
beingsaved.savefig('expo2.svg', format='svg', dpi=1200)
beingsaved = plt.figure()
plot(cuadratic, x, y)
beingsaved.savefig('cuadratic2.svg', format='svg', dpi=1200)
beingsaved = plt.figure()
plot(cubic, x, y)
beingsaved.savefig('cubic2.svg', format='svg', dpi=1200)
beingsaved = plt.figure()
plot(cuart, x, y)
beingsaved.savefig('cuart2.svg', format='svg', dpi=1200)