"""
This script impliments Butcher tableu of different rk methods
available at :
https://en.wikipedia.org/wiki/List_of_Runge%E2%80%93Kutta_methods
"""

import numpy as np

def rk4():
    """
    classical Runge Kutta 4th order
    Butcher tableau
    """

    c = np.array([0, 1/2, 1/2, 1])
    A = np.array([[0., 0., 0., 0.],
                  [1/2, 0., 0., 0.],
                  [0., 1/2, 0., 0.],
                  [0., 0., 1., 0.]])
    b = np.array([1/6, 1/3, 1/3, 1/6])

    return (c, A, b)

