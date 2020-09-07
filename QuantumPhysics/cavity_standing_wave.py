#credit MuhsinIbnAlAzeez

'''
This is an animation showing a standing wave in a cavity 

'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 2
a = 10
E0 = 5
c = 3

x = np.linspace(0,a,100)
t = np.linspace(0,10,100)

E = E0*np.sin(n*(np.pi/a)*x)

fig = plt.figure()
ax = fig.add_subplot(111,xlim=(0,a), ylim=(-E0-5,E0+5))
plt.title("n = {}".format(n))

line, = ax.plot([], [])

def init():
    line.set_data([], [])
    return line

def animate(i):
	time = np.sin(1000*np.pi*(n/a)*i)
	Et = E*time
	line.set_data(x,Et)
	return line

ani = animation.FuncAnimation(fig, animate, t,
                              interval=25, init_func=init)

plt.show()
