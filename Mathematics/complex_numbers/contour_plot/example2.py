import matplotlib.pyplot as plt
import numpy as np
from definitions import *

theta = np.linspace(-np.pi, np.pi-0.01, 100)
# circle include origin
x1, y1 = contour_circle(0, 0, 0.5, theta)
# _, a = to_polar(x1, y1)
# print(a)
u1, v1 = complex_sqrt(x1, y1, polar=False)
u11, v11 = f1(x1, y1, polar=False)

# circle donot include origin
x2, y2 = contour_circle(0, 1, 0.5, theta)
# _, a = to_polar(x2, y2)
# print(a)
u2, v2 = complex_sqrt(x2, y2, polar=False)
u21, v21 = f1(x2, y2, polar=False)

# yet Another contour
x4, y4 = contour_rectangle(-4, 3, 3, 2, len(theta))
# _, a = to_polar(x3, y3)
# print(a)
u4, v4 = complex_sqrt(x4, y4, polar=False)

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
plt.plot(u1, v1, label="sqrt(z1)")
plt.plot(u11, v11, label="sqrt(z1^2+1)")
plt.plot(x2, y2, label="z2")
plt.plot(u2, v2, label="sqrt(z2)")
plt.scatter(u21, v21, s=1.5, label="sqrt(z2^2+1)")
plt.plot(x4, y4, label="z4")
plt.plot(u4, v4, label="sqrt(z4)")
plt.legend()
plt.show()