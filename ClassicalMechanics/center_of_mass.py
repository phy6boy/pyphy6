# This program calculate center of mass of
# some 2D systems about origin and z axis
import numpy as np
import matplotlib.pyplot as plt

def disc():
    # generares disc (radius 1) as x, y pairs
    # returns : numpy arrays x and y
    x = np.linspace(-1, 1, 2000)
    y = np.linspace(-1, 1, 2000)

    u,v = np.meshgrid(x, y)

    cx = u[u**2+v**2<=1]
    cy = v[u**2+v**2<=1]

    return cx, cy

def disc_with_hole():
    # generares disc (radius 1) as x, y pairs
    # with a hole of radius 1/2
    # returns : numpy arrays x and y
    x = np.linspace(-1, 1, 2000)
    y = np.linspace(-1, 1, 2000)

    u,v = np.meshgrid(x, y)

    mask = np.logical_and(u**2+v**2<=1, (u-0.5)**2+v**2>=0.25)
    cx = u[mask]
    cy = v[mask]

    return cx, cy

# ############################################
# CALCULATION
x, y = disc_with_hole()
N = len(x)   # number of particles
M = 3.0/4.0  # mass
m = M / N   # masss of each particle
Cx = (m*x).sum()/M  # Center of mass x coord.
Cy = (m*y).sum()/M  # Center of mass y coord.
print(f"Center of Mass : ({round(Cx, 3)}, {round(Cy, 3)})")

# x, y = disc_with_hole()
# print(x.shape, y.shape)
fig, ax = plt.subplots()
ax.set_aspect("equal")
plt.scatter(x, y, s=0.5)
plt.show()