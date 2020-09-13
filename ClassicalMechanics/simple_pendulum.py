import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from solvers.rk import rk4

c, A, b = rk4()

def rkstep(tn, y1n, y2n, f1, f2, h):
    """
    given tn, y1n and y2n, find next value of y1 and y2,
    find y1n+1, y2n+1 at a time tn + h
    use a method (rk4 by default)
    parameters:
        f : function on the right hand of RK
        f = f(t, y)
        h : time step
        c , A, b : np.arrays corresponding to 
                   butcher tableu of pirticular method
    """
    k10 = f1(tn, y1n, y2n)
    k20 = f2(tn, y1n, y2n)
    k1 = np.zeros_like(c, dtype=float)
    k2 = np.zeros_like(c, dtype=float)
    k1[0] = k10
    k2[0] = k20


    for i in range(1, len(k1)):
        k1[i] = f1(tn + c[i]*h, y1n + h*np.sum(A[i, :i]*k1[:i]), y2n + h*np.sum(A[i, :i]*k1[:i]))
        k2[i] = f2(tn + c[i]*h, y1n + h*np.sum(A[i, :i]*k2[:i]), y2n + h*np.sum(A[i, :i]*k2[:i]))

    y1n1 = y1n + h*np.sum(b*k1)
    y2n1 = y2n + h*np.sum(b*k2)

    return y1n1, y2n1

## Definition of derivatives
def f1(t, th, om):
    """
    dtheta/dt = f1 = om
    """
    return om
def f2(t, th, om):
    """
    domega/dt = f2
    """
    # return (-g/L)*np.sin(th)
    return (-g/L)*(th)

# initial conditions
g = 9.8
L = 1.2
t0 = 0.
tf = 10.
theta0 = -np.pi/3
omega0 = 0.0
N = 10000
# arrays and step size
h  = (tf-t0)/N
T  = np.zeros(N, dtype=float)
TH = np.zeros(N, dtype=float)
OM = np.zeros(N, dtype=float)
# array initialization
T[0]  = t0
TH[0] = theta0
OM[0] = omega0
# iteration
tn = t0
y1n = theta0
y2n = omega0
for i in range(1, len(T)):
    y1n, y2n = rkstep(tn, y1n, y2n, f1, f2, h)
    tn = tn + h
    T[i]  = tn
    TH[i] = y1n
    OM[i] = y2n

# plt.plot(T, TH, T, OM)
# plt.show()

# animation
fig = plt.figure()
ax = plt.axes(xlim=(-(L + 0.5), L + 0.5), ylim=(-(L + 0.5) , L + 0.5))
ax.set_aspect('equal')
ax.plot(0, 0, 'o', ms=5, c='k')
skip = int(0.02 / h)   # 50 fps (0.02 frames per second)
line = ax.plot([], [], '-', lw=2, c='r')[0]
m = ax.plot([], [], 'o', ms=10, c='r')[0]

def animate(i):
    i *= skip
    xi = L*np.cos(TH[i] + np.pi/2)
    yi = -L*np.sin(TH[i] + np.pi/2)
    line.set_data([0, xi], [0, yi])
    m.set_data(xi, yi)

    return line, m

anim = animation.FuncAnimation(
        fig=fig,
        func=animate,
        frames=len(TH)//skip,
        interval=20,
        blit=True,
    )

plt.show()