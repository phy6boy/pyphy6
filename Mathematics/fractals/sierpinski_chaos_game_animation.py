"""
Sierpinsky triangle using chaos game
Rule:
    draw vertices of eq.triangle
    make a randon point inside triangle
    take a random vertex
    plot midpoint
    take that midpoint as next random point
    repeat
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

# Comment this if you want a white backround
plt.style.use("dark_background")

N = 15000
x = np.zeros(N)
y = np.zeros(N)
c = np.zeros(N, dtype=np.object)

V = ((0, 0), (1, 0), (0.5, np.sqrt(3)/2))
p = (0.5, 0.5)

x[:3] = [j[0] for j in V]
y[:3] = [j[1] for j in V]
c[:3] = ["#FF7029","#3AFF21", "#B450C9"]

for i in range(3, N):
    n = np.random.choice([0, 1, 2])
    v = V[n]
    xm = (p[0] + v[0])/2.
    ym = (p[1] + v[1])/2.
    x[i] = xm
    y[i] = ym
    p = (xm, ym)
    c[i] = c[n]

# print(x)
# print(y)
# print(c)
fig = plt.figure(figsize = (12, 12))
plt.axis("off")
cont_index = 0
for i in tqdm(range(3, N, 50)):
    plt.scatter(x[cont_index:i], y[cont_index:i], c=c[cont_index:i], s=5)
    cont_index = i
    plt.savefig(f"images/Sierpinsky{str((i-3)//50).zfill(4)}.png")


# Note : Inorder to work this, You need to setup ffmpeg.
# Or, you can take images from images folder and make animation.
fps = 20
os.system(f'ffmpeg -r {fps} -s 1920x1080 -i "images/Sierpinsky%04d.png"\
 -vcodec libx264 -crf 20 -pix_fmt yuv420p "video/Sierpinsky.mp4"')
