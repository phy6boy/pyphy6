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

import math
#angle
theta_in_degree = float(input('enter the angle of scattering(in degree) : '))

theta_in_radian = lambda theta_in_degree : theta_in_degree*math.pi / 180

def calculate_delta(theta):
	return (h / (m_e * c)) * (1 - math.cos(theta))

ans = calculate_delta(theta_in_radian(theta_in_degree))

print(f'The difference in wave length = {"%0.3e" %ans} m')

wavelength = input('enter the wavelength to compute resulting wavelength: ')

if wavelength:
	wavelength = float(wavelength)
	wavelength = wavelength + ans
	print(f'wavelength is : {"%0.4e" %wavelength}')
