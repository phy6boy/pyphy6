import matplotlib.pyplot as plt
import numpy as np
from definitions import to_polar, complex_log, contour_circle, contour_rectangle

theta = np.linspace(-np.pi, np.pi-0.01, 100)
# circle include origin
x1, y1 = contour_circle(0, 0, 1, theta)
# _, a = to_polar(x1, y1)
# print(a)
u1, v1 = complex_log(x1, y1, polar=False)

# circle donot include origin
x2, y2 = contour_circle(2, 2, 1, theta)
# _, a = to_polar(x2, y2)
# print(a)
u2, v2 = complex_log(x2, y2, polar=False)

# Another contour
x3, y3 = contour_rectangle(-0.5, 0.5, 1, 1, len(theta))
# _, a = to_polar(x3, y3)
# print(a)
u3, v3 = complex_log(x3, y3, polar=False)

# yet Another contour
x4, y4 = contour_rectangle(-4, 3, 3, 2, len(theta))
# _, a = to_polar(x3, y3)
# print(a)
u4, v4 = complex_log(x4, y4, polar=False)

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
plt.plot(u1, v1, label="w1")
plt.plot(x2, y2, label="z2")
plt.plot(u2, v2, label="w2")
plt.plot(x3, y3, label="z3")
plt.plot(u3, v3, ".", label="w3")
plt.plot(x4, y4, label="z4")
plt.plot(u4, v4, label="w4")
plt.legend()
# uncomment to save
# plt.savefig("branch_point_ln_z.svg")
plt.show()