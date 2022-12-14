#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy

def tri_cdf(x):
    if (x < 0): return 0
    elif (x < 1): return (x**2)/2
    elif (x < 2): return -(x**2)/2 + 2*x - 1
    else: return 1

arr_func = scipy.vectorize(tri_cdf, otypes=['double'])

maxrange=80
x = np.linspace(-4,4,maxrange)#points on the x axis
#points for analytical cdf
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('tri.dat',dtype='double')
for i in range(maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x,arr_func(x))#plotting analytical CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_T(x)$')
plt.savefig('TRI_cdf.eps')
plt.savefig('TRI_cdf.pdf')
