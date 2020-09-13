import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from solvers.rk import rk4
from tqdm import tqdm

c, A, b = rk4()

def rkstep(tn, th1n, om1n, th2n, om2n, f1, f2, f3, f4, h):
    """
    given tn, th1n and om1n, find next value of y1 and y2,
    find th1n+1, om1n+1 at a time tn + h
    use a method (rk4 by default)
    parameters:
        f : function on the right hand of RK
        f = f(t, y)
        h : time step
        c , A, b : np.arrays corresponding to 
                   butcher tableu of pirticular method
    """
    k10 = f1(tn, th1n, om1n, th2n, om2n)
    k20 = f2(tn, th1n, om1n, th2n, om2n)
    k30 = f3(tn, th1n, om1n, th2n, om2n)
    k40 = f4(tn, th1n, om1n, th2n, om2n)
    k1 = np.zeros_like(c, dtype=float)
    k2 = np.zeros_like(c, dtype=float)
    k3 = np.zeros_like(c, dtype=float)
    k4 = np.zeros_like(c, dtype=float)
    k1[0] = k10
    k2[0] = k20
    k3[0] = k30
    k4[0] = k40


    for i in range(1, len(k1)):
        k1[i] = f1(tn + c[i]*h, th1n + h*np.sum(A[i, :i]*k1[:i]),\
                   om1n + h*np.sum(A[i, :i]*k1[:i]),\
                   th2n + h*np.sum(A[i, :i]*k1[:i]),\
                   om2n + h*np.sum(A[i, :i]*k1[:i]))
        k2[i] = f2(tn + c[i]*h, th1n + h*np.sum(A[i, :i]*k2[:i]),\
                   om1n + h*np.sum(A[i, :i]*k2[:i]),\
                   th2n + h*np.sum(A[i, :i]*k2[:i]),\
                   om2n + h*np.sum(A[i, :i]*k2[:i]))
        k3[i] = f3(tn + c[i]*h, th1n + h*np.sum(A[i, :i]*k3[:i]),\
                   om1n + h*np.sum(A[i, :i]*k3[:i]),\
                   th2n + h*np.sum(A[i, :i]*k3[:i]),\
                   om2n + h*np.sum(A[i, :i]*k3[:i]))
        k4[i] = f4(tn + c[i]*h, th1n + h*np.sum(A[i, :i]*k4[:i]),\
                   om1n + h*np.sum(A[i, :i]*k4[:i]),\
                   th2n + h*np.sum(A[i, :i]*k4[:i]),\
                   om2n + h*np.sum(A[i, :i]*k4[:i]))

    th1n1 = th1n + h*np.sum(b*k1)
    om1n1 = om1n + h*np.sum(b*k2)
    th2n1 = th2n + h*np.sum(b*k3)
    om2n1 = om2n + h*np.sum(b*k4)

    return th1n1, om1n1, th2n1, om2n1

## Definition of derivatives
def f1(t, th1, om1, th2, om2):
    """
    dtheta1/dt = f1 = om1
    """
    return om1
def f2(t, th1, om1, th2, om2):
    """
    domega1/dt = f2
    """
    num = -g*(2*m1 + m2)*np.sin(th1) - m2*g*np.sin(th1-2*th2) - \
           2*np.sin(th1 - th2)*m2*(om2**2*L2+om1**2*L1*np.cos(th1-th2))
    den = L1*(2*m1 + m2 - m2*np.cos(2*th1 - 2*th2))

    return num / den

def f3(t, th1, om1, th2, om2):
    """
    dtheta2/dt = f3 = om2
    """
    return om2

def f4(t, th1, om1, th2, om2):
    """
    domega2/dt = f4
    """
    num = 2*np.sin(th1 - th2)*(om1**2*L1*(m1 + m2) +\
          g*(m1+m2)*np.cos(th1) + om2**2*L2*m2*np.cos(th1-th2))
    den = L2*(2*m1 + m2 - m2*np.cos(2*th1 - 2*th2))

    return num / den

# initial conditions
g = 9.8
t0 = 0.
tf = 20.
N = 20000
h  = (tf-t0)/N
T  = np.zeros(N, dtype=float)

n = 5   # number of pendula
mass1 = [1. for i in range(n)]; mass2 = [1. for i in range(n)];
l1 = [1.2 for i in range(n)]; l2 = [1.2 for i in range(n)];
theta10 = [5*np.pi/6 for i in range(n)] ; theta20 = [np.pi/2.6 + 0.00001*i for i in range(n)];
omega10 = [0.0 for i in range(n)]; omega20 = [0.0 for i in range(n)];

# arrays
TH1 = np.zeros((n, N), dtype=float)
OM1 = np.zeros((n, N), dtype=float)
TH2 = np.zeros((n, N), dtype=float)
OM2 = np.zeros((n, N), dtype=float)
# array initialization
T[0]  = t0
TH1[:, 0] = theta10
OM1[:, 0] = omega10
TH2[:, 0] = theta20
OM2[:, 0] = omega20

# iteration
for p in range(n):
    tn = t0
    th1n = theta10[p]
    om1n = omega10[p]
    th2n = theta20[p]
    om2n = omega20[p]
    L1 = l1[p]
    L2 = l2[p]
    m1 = mass1[p]
    m2 = mass2[p]
    for i in tqdm(range(1, len(T))):
        th1n, om1n, th2n, om2n = rkstep(tn, th1n, om1n, th2n, om2n, f1, f2, f3, f4, h)
        tn = tn + h
        T[i]  = tn
        TH1[p, i] = th1n
        OM1[p, i] = om1n
        TH2[p, i] = th2n
        OM2[p, i] = om2n

# plt.figure(1)
# plt.plot(T, TH1, T, OM1)
# plt.figure(2)
# plt.plot(T, TH2, T, OM2)
# plt.show()

# animation
fig = plt.figure(figsize=(8, 8))
# plt.style.use("dark_background")
ax = plt.axes(xlim=(-(np.max(l1)+np.max(l2) + 0.5), np.max(l1)+np.max(l2) + 0.5),\
              ylim=(-(np.max(l1)+np.max(l2) + 0.5), np.max(l1)+np.max(l2) + 0.5))
ax.set_aspect('equal')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.plot(0, 0, 'o', ms=5, c='k')
skip = int(0.02 / h)   # 50 fps (0.02 frames per second)

lines, m1s, m2s, traces = [], [], [], []
for p in range(n):
    lines.append(ax.plot([], [], '-', lw=3, c=f'C{p}')[0])
    m1s.append(ax.plot([], [], 'o', ms=4, c=f'C{p}')[0])
    m2s.append(ax.plot([], [], 'o', ms=15, c=f'C{p}')[0])
    traces.append(ax.plot([], [], 'o', ms =1, c=f'C{p}')[0])

x1 =  np.array(l1).reshape((-1, 1))*np.sin(TH1)
y1 = -np.array(l1).reshape((-1, 1))*np.cos(TH1)
x2 = x1 + np.array(l2).reshape((-1, 1))*np.sin(TH2)
y2 = y1 - np.array(l2).reshape((-1, 1))*np.cos(TH2)

def animate(i):
    i *= skip
    for p in range(n):
        x1i = x1[p, i]
        x2i = x2[p, i]
        y1i = y1[p, i]
        y2i = y2[p, i]
        lines[p].set_data([0, x1i, x2i], [0, y1i, y2i])
        m1s[p].set_data(x1i, y1i)
        m2s[p].set_data(x2i, y2i)
        traces[p].set_data(x2[p, max(0, i-100*skip):i:skip],\
                           y2[p, max(0, i-100*skip):i:skip])

    return lines+m1s+m2s+traces

anim = animation.FuncAnimation(
        fig=fig,
        func=animate,
        frames=len(TH1[0])//skip,
        interval=20,
        blit=True,
    )

# plt.show()
writer = animation.FFMpegWriter(fps=50, bitrate=-1)
anim.save("./output/double_pendulum.mp4", writer=writer)