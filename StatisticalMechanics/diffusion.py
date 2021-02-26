"""
This file implements diffusion of a bunch of particles 
put in a bath. the system description id given in diffusion_models.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from diffusion_models import *

step = infinite_surface     # check diffusion_models.py for more

N = 5000                    # Number of particles
x = np.random.random(N)-0.5
y = np.random.random(N)-0.5
vx = np.zeros_like(x)
vy = np.zeros_like(y)
dt = 0.001

# Plots
fig = plt.figure()
fig.subplots_adjust(left   = 0,
                    right  = 1,
                    bottom = 0,
                    top    = 1)
ax = fig.add_subplot(111, aspect='equal',
                     autoscale_on=False,
                     xlim=(-10, 10),
                     ylim=(-10, 10))
plt.axis("off")
p, = ax.plot(x, y, 'o', c="#2E30FF", ms=1)


def animate(i):
    """
    animation routine for matplotlib.animation
    """
    global x, y, vx, vy
    x, y, vx, vy = step(x, y, vx, vy, dt)

    # updating plot
    p.set_data(x, y)

    return p,

ani = animation.FuncAnimation(fig, animate,
                              frames=2000,
                              interval=10,
                              blit=True)
# ani.save('output/diffusion.mp4', fps=100)
plt.show()