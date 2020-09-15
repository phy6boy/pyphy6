import numpy as np
from svgpathtools import svg2paths
import matplotlib.pyplot as plt

def parse_svg(filename, N=1000):
    """
    return tuple of arrays X and Y
    representing coordinates from 
    the svg file 'filename'
    N : number of data needed in X and Y
    """
    path, _ = svg2paths(filename)
    path = path[0]

    X = np.zeros(N, dtype=float)
    Y = np.zeros(N, dtype=float)
    i = 0
    for p in np.linspace(0.0, 1.0, N):
        point = path.point(p)
        X[i] = point.real
        Y[i] = point.imag
        i += 1
    # Y is reversed. reversing
    Y = Y.max() - Y
    # centering origin
    X = X - X.max()/2.0
    Y = Y - Y.max()/2.0

    return X, Y

if __name__ == "__main__":
    X, Y = parse_svg("input/india.svg")
    plt.plot(X, Y)
    plt.show()