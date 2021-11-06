import random as rand
import numpy as np
import sys
import os

#constants
beta = 1.15*0.53 #(7.2*(10**(-20)))*(0.848*(10**(-19)))  #(Am)^-1
e = 1.60217662*(10**(-19)) #Electron charge
rb = 5.291777211*(10**(-11)) #bohr's radius

#forster radii
R11 = 0#6.04*(10**(-9)) #m 
R12 = 0
R21 = 0#5.2*(10**(-9))
R22 = 2.0*(10**(-9))#2.87*(10**(-9))

#material1(6T)
#mu1 = 6.49*e*rb #dipole moment in Am²
#T1_emi = 4.05*(10**(-7)) #emission time in s
#r1bar = 2.66*(10**(-9)) #medium distance between molecules in m
#k1_emi = 1/T1_emi #emission rate in s**(-1)
#k11_F = (1/T1_emi)*(R11/(mu1*beta+r1bar))**6 #Forster rate in s**(-1) 
#P1_hop = k11_F/(k1_emi+k11_F) #hopping probability 
#dt1 = 1/k11_F #time between hops in s

#material2(P6P)
mu2 = 0 #5.7*e*rb
T2_emi = 2*(10**(-9)) #1.18*(10**(-9))
r2bar = 10**(-9) #1.35*(10**(-9))
k2_emi = 1/T2_emi
k22_F = (1/T2_emi)*(R22/(mu2*beta+r2bar))**6
P2_hop = k22_F/(k2_emi+k22_F)
dt2 = 1/k22_F
#r21bar = (r1bar+r2bar)/2
#mu21 = (mu1+mu2)/2
P2_emi = k2_emi/(k2_emi+k22_F) 

#interface
#k12_F = 0 #(1/T1_emi)*(R12/(mu1*beta+r1bar))**6 #it's not actually that
#k21_F = (1/T2_emi)*(R21/(mu21*beta+r21bar))**6
#P12_hop = k12_F/(k12_F+k11_F)
#P21_hop = k21_F/(k21_F+k22_F)

#parameters
n_rounds = 10#int(sys.argv[2]) 
n_excitons = int(sys.argv[1])
interface1 = -1.0*(10**(-6)) #(float(sys.argv[1]))*(10**(-9))
interface2 = 1.0*(10**(-6)) #(float(sys.argv[1]))*(10**(-9))
#yzero = (50*(10**(-9)))*rand.uniform(-1.0,1.0)#sys.argv[1]# {0,50,100,150,200,250}nm


#annihilation function
def annihil(): 
    global state, n_anni, n_uni
    for i in range(0,n_excitons-1):
        if (state[i] != 0):
            for j in range(i+1,n_excitons):
                if (state[j] != 0): 
                    if (abs(y[i]-y[j]) <= r2bar):
                        state[j] = 0
                        n_anni = n_anni + 1
                        print('n_anni=',n_anni)
                        print(t, y[i], 'anni', file=open("T_death_"+sys.argv[1],"a"))
                        print(t, y[i], file=open("T_anni_"+sys.argv[1],"a")) 
                        continue
                      
#exciton random generation function                    
def generation(): 
    y0 = np.empty(n_excitons)
    for i in range(0,n_excitons):
        a1 = rand.uniform(-1.0,1.0)
        y0[i] = (1.0*(10**(-6)))*a1
    return y0    #returns an array with all excitons' initial positions


#KMC
for n_uni in range(0,n_rounds):
    n_emitted2, n_anni = 0, 0 #no excitons emitted nor annihilated
    state = np.ones(n_excitons) #dead-alive vector. all excitons "alive" at this point
    y = generation() #gives the initial position of excitons. an array with n_excitons elements
    #print('y0=',y)
    t = 0
    uni = str(n_uni)
    #for i in range(0,n_excitons): #comment this block if not interested in trajectories
        #exc = str(i)
        #print(0,y[i],file=open("rand_exc_"+exc+"_uni_"+uni,'a')) #prints the first line of the trajectory file
    while (n_emitted2 + n_anni < n_excitons): # for each time-step, do:
        for i in range(0,n_excitons):
            if (state[i].all() == 0): #if all excitons are "dead", breaks out of the innermost loop
                continue
            else:
                annihil()
                a2 = rand.random()                         
                if (y[i] > interface1 or y[i] < interface2): #material2
                    if (a2 <= 0.5):
                        dr = r2bar
                    else:
                        dr = -r2bar
                elif (y[i] >= interface1):
                    dr = r2bar
                elif (y[i] == interface2):
                    dr = -r2bar
                T = str(t)  
                uni = str(n_uni)
                exc = str(i)                                                                       # print(y[i], file=open("sum_P6P_uni_"+uni+"_exc_"+exc+"_t_"+T,"a")) #comment this line if not interested in trajectories
                d = rand.random()
                if (d <= P2_emi):
                    n_emitted2 = n_emitted2 + 1
                    print('n_emi=',n_emitted2)
                    print(t, y[i], 'emit', file=open("T_death_"+sys.argv[1],"a")) 
                    print(t, y[i], file=open("T_emi_"+sys.argv[1],"a"))  #prints the time and position of emission for this exciton, in this universe 
                    state[i] = 0 #switches the entry of the dead-alive vector
                    continue
                else:       
                    y[i] = y[i] + dr
                    #print(y[i])
                    #print(t+dt2, y[i], file=open("rand_exc_"+exc+"_uni_"+uni,'a')) #comment this line if not interested in trajectories
        t = t + dt2                           # next time-step

















 
