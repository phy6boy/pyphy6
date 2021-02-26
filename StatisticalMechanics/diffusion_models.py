"""
file : diffusion_models.py

implemetation of 'steps' in file diffusion.py

each function describe here takes a set of
 parameters and update some of it
"""

import numpy as np

def infinite_surface(x, y, vx, vy, dt):
    '''
    A bunch of paticles put in an infinite plane surface. 
    modelled with euler-maruyana method
    '''
    gamma = 1.0
    vx = vx - gamma*vx*dt + 500*np.random.randn(len(vx))*dt
    vy = vy - gamma*vy*dt + 500*np.random.randn(len(vy))*dt

    x = x + vx*dt
    y = y + vy*dt

    return (x, y, vx, vy)


def surface_with_B(x, y, vx, vy, dt):
    '''
    A bunch of paticles put in an infinite plane surface.
    Magnetic field is applied perpendicular to plane. 
    modelled with euler-maruyana method
    '''
    gamma = 1.0
    eB = 0.01
    vx = vx - gamma*vx*dt - eB*vy + 600*np.random.randn(len(vx))*dt
    vy = vy - gamma*vy*dt + eB*vx + 600*np.random.randn(len(vy))*dt

    x = x + vx*dt
    y = y + vy*dt

    return (x, y, vx, vy)


def harmonic_dish(x, y, vx, vy, dt):
    '''
    A bunch of paticles put in a harmonic dish.
    modelled with euler-maruyana method
    '''
    gamma = 1.0
    k = 0.1
    vx = vx - gamma*vx*dt - k*x + 600*np.random.randn(len(vx))*dt
    vy = vy - gamma*vy*dt - k*y + 600*np.random.randn(len(vy))*dt

    x = x + vx*dt
    y = y + vy*dt

    return (x, y, vx, vy)