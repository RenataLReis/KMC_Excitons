import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab
import scipy 
from scipy.stats import norm
import numpy as np
import pandas as pd
import sys
from scipy.optimize import curve_fit


def fit_function(x,A,mu,sigma):
    return (A/(sigma*sqrt(2*np.pi))*exp(-0.5*(x-mu)**2/sigma**2)


data = open("sum_"+sys.argv[1],"r")
lines = data.readlines()
array = np.asarray(lines,float)
b = int(sys.argv[2])
#np.histogram(array, bins=b)
hist,bins = np.histogram(array,bins=b)
print(type(bins))
#plt.hist(array, b)
binscenters = np.array([0.5*(bins[i]+bins[i+1]) for i in range(len(bins)-1)])

popt, pcov = curve_fit(fit_function,x_data=binscenters,ydata=hist, p0=[20000, 2.0, 2000, 3.0, 0.3])
print(popt)

xspace = np.linspace(np.min(array), np.max(array),10000)
##mu = np.mean(array)
##sigma = np.var(array)
##pdf_x = np.linspace(np.min(array),np.max(array),100)
##pdf_y = 1.0/np.sqrt(2*np.pi*sigma)*np.exp(-0.5*(pdf_x-mu)**2/sigma**2)


#mu, sigma = 0, 0.1
#(mu,sigma)=norm.fit(array)
#s = np.random.normal(mu,sigma)
#count, bins, ignored = plt.hist(s,b,density=True)
#y = scipy.stats.norm.pdf(bins, mu, sigma)
#l = plt.plot(bins, y, 'r', linewidth=2)#(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(bins-mu)**2/(2*sigma**2)), linewidth=2,color='r')

##plt.figure()
##plt.hist(array,b,density=False)
##plt.plot(pdf_x,pdf_y, 'r-')

plt.bar(binscenters, hist, width=bins[1]-bins[0],color='navy')
plt.plot(xspace, fit_function(xspace, *popt), color = 'r', linewidth=2)



plt.show()
