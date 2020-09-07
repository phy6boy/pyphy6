'''
This program plot compton scatteing 

the equation is: 


             h
      Δλ = ----- (1 - cos(θ))
             mc


'''

import sys,os
sys.path.insert(1,os.path.join(sys.path[0],'..'))
from constants.constants import h,m_e,c

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0,np.pi,100)
lambda_ = h / (m_e *c) * (1 - np.cos(theta))

plt.plot(theta , lambda_,label = r'$\Delta\lambda = \frac{h}{m_0c}\left(1-\cos\theta\right)$')
plt.axvline(np.pi/2 , ymax = 0.5 , color='r' , linestyle = ':')
plt.xticks([0 , np.pi/2 , theta[-1]] , [0 , r'$\pi/2$' , r'$\pi$'])
plt.yticks([0 , lambda_[-1]] , [0 , r'$\frac{2h}{m_0c}$'])
plt.xlabel(r'$\theta\;\longrightarrow$')
plt.ylabel(r'$\Delta\lambda\;\longrightarrow$')
plt.legend()
plt.show()
