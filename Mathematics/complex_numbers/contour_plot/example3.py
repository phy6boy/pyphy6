import matplotlib.pyplot as plt
import numpy as np
from definitions import to_polar, complex_log, contour_circle, contour_rectangle

theta = np.linspace(-np.pi, np.pi-0.01, 100)
x1, y1 = contour_rectangle(-0.5, 0.5, 1, 1, len(theta))
u1, v1 = complex_log(x1, y1, polar=False)

x2, y2 = contour_rectangle(-3, 2, 2, 3, len(theta))
r2, arg2 = to_polar(x2, y2)
arg2[arg2 < 0] += 2*np.pi    # simple technique to avoid multiple values
u2, v2 = complex_log(r2, arg2, polar=True)

x3, y3 = contour_circle(-1, 1, 2, theta)
u3, v3 = complex_log(x3, y3, polar=False)   #use scatter (dot) plot here

# Plotting
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(-4, 4)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x1, y1, label="z1")
plt.scatter(u1, v1, s=2.5, label="w1")
plt.plot(x2, y2, label="z2")
plt.plot(u2, v2, label="w2")
plt.plot(x3, y3, label="z2")
plt.scatter(u3, v3, s=1.9, label="w2")
plt.legend()
plt.show()