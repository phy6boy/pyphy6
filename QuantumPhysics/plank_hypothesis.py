'''
This program plots the difference between
 the plank hypothesis and Rayliegh-jenes hypothesis
πρν
Reyliegh-Jeans formulae for blackbody radiation:
                          2
                       8πν  kT
            ρ(ν)dν =  --------- dν
                           3
                          c

the Plank's blackbody spectrum:
                           2               
                        8πν       hν
            ρ(ν)dν =  ------- ------------ dν
                          3     (hν/kT)
                         c     e       -1

 
Experimental Plot:

            ^
            |         
            |        + +
            |      +    +
            |      +     +
            |     +        +
            |    +           +
            |    +            + 
            |   +              +
            |  +                 +
            | +                    +++++++++
            +______________________________________>

'''

import sys,os
sys.path.insert(1,os.path.join(sys.path[0],'..'))
from constants.constants import h,k_b,c


import matplotlib.pyplot as plt
import numpy as np

# T = 1595

def plank_distr(nu,T):
	return (8*np.pi*nu**2*h*nu)/(c**3*(np.exp(h*nu/(k_b*T))-1))


freq = np.linspace(0.01e14,4e14,100)

energy = plank_distr(freq,1595)
energy1 = plank_distr(freq,2000)
energy2 = plank_distr(freq,3000)

def classic_distr(nu,T):
	return (8*np.pi*nu**2*k_b*T)/c**3

classic_energy = classic_distr(freq,1595)


plt.plot(freq,energy,label="Plank's prediction")
plt.ylim(-0.2e-17,4e-17)
plt.plot(freq,classic_energy,'--',label="Reyleigh-Jeanes prediction")
#plt.plot(freq,energy,freq,energy1,freq,energy2)
plt.legend()
plt.show()
