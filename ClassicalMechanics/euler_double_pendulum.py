"""
This is a beginner-friendly implimentation
of double pendulum using euler method
the derivation of equations can be found here:
https://www.myphysicslab.com/pendulum/double-pendulum-en.html
"""

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib import animation

L1 = 1.0
L2 = 1.0
m1 = 1.0
m2 = 1.0
g  = 9.8

def theta1_dot(theta1, theta2, omega1, omega2):
    return omega1

def theta2_dot(theta1, theta2, omega1, omega2):
    return omega2

def omega1_dot(theta1, theta2, omega1, omega2):
    num = -g*(2*m1 + m2)*np.sin(theta1) - m2*g*np.sin(theta1 - 2*theta2) - \
           2*np.sin(theta1 - theta2)*m2*(omega2**2*L2 + omega1**2*L1*np.cos(theta1 - theta2))
    den = L1*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))

    return num/den

def omega2_dot(theta1, theta2, omega1, omega2):
    num = 2*np.sin(theta1 - theta2)*(omega1**2*L1*(m1 + m2) + g*(m1+m2)*np.cos(theta1) +\
        omega2**2*L2*m2*np.cos(theta1 - theta2))
    den = L1*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))

    return num/den

# #################################################################################

t0 = 0.0
tf = 10.0
N  = 10000
T  = np.linspace(t0, tf, N)
dt = T[1] - T[0]

# creating arrays
theta1 = np.zeros(N, dtype=float)
theta2 = np.zeros(N, dtype=float)
omega1 = np.zeros(N, dtype=float)
omega2 = np.zeros(N, dtype=float)

# initial conditions
theta10 = 5*np.pi/6
theta20 = np.pi/3
omega10 = 0.0
omega20 = 0.0

theta1[0] = theta10
theta2[0] = theta20
omega1[0] = omega10
omega2[0] = omega20


# iteration
for i in tqdm(range(1, N)):
    theta10_next = theta10 + theta1_dot(theta10, theta20, omega10, omega20)*dt
    theta20_next = theta20 + theta2_dot(theta10, theta20, omega10, omega20)*dt
    omega10_next = omega10 + omega1_dot(theta10, theta20, omega10, omega20)*dt
    omega20_next = omega20 + omega2_dot(theta10, theta20, omega10, omega20)*dt

    theta10 = theta10_next
    theta20 = theta20_next
    omega10 = omega10_next
    omega20 = omega20_next

    theta1[i] = theta10
    theta2[i] = theta20
    omega1[i] = omega10
    omega2[i] = omega20

# plt.figure(0)
# plt.plot(T, theta1, T, omega1)
# plt.figure(1)
# plt.plot(T, theta2, T, omega2)
# plt.show()

# ##############################################################################
fps = 60
fig = plt.figure(2, figsize=(8, 8))
plt.style.use("dark_background")
ax = plt.axes(xlim=(-(L1 + L2 + 0.5), L1 + L2 + 0.5),\
              ylim=(-(L1 + L2 + 0.5), L1 + L2 + 0.5))
ax.set_aspect('equal')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.plot(0, 0, 'o', ms=5, c='#BCFF21')


line = ax.plot([], [], '-', lw=3, c=f'#FF6A49')[0]
m1 = ax.plot([], [], 'o', ms=5, c=f'#FF6A49')[0]
m2 = ax.plot([], [], 'o', ms=15, c=f'#FF6A49')[0]
traces = ax.plot([], [], 'o', ms =1, c=f'#FF6A49')[0]

x1 =  L1*np.sin(theta1)
y1 = -L1*np.cos(theta1)
x2 = x1 + L2*np.sin(theta2)
y2 = y1 - L2*np.cos(theta2)

skip = int(1 /(fps* dt))   # 50 fps (0.02 frames per second)
def animate(i):
    i *= skip
    x1i = x1[i]
    x2i = x2[i]
    y1i = y1[i]
    y2i = y2[i]
    line.set_data([0, x1i, x2i], [0, y1i, y2i])
    m1.set_data(x1i, y1i)
    m2.set_data(x2i, y2i)
    traces.set_data(x2[max(0, i-100*skip):i:skip],\
                       y2[max(0, i-100*skip):i:skip])

    return line , m1 , m2 , traces

anim = animation.FuncAnimation(
        fig=fig,
        func=animate,
        frames=len(theta1)//skip,
        interval=20,
        blit=True,
    )

plt.show()
# writer = animation.FFMpegWriter(fps=fps, bitrate=-1)
# anim.save("./output/double_pendulum_black.mp4", writer=writer)