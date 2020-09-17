import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.spatial.distance import pdist, squareform

class Particles:
    """
    class that manages particles, its state, size and 
    mass
    """
    
    def __init__(self, state, size=0.05, m=0.03, e=1.0):
        """
        state : 2d array : (m n)
            each row 'm' contains particles
            each column 'n' is of size 4 : [x, y, vx, vy] of each particle
        size : size of particle
        m    : mass of particle
        e    : coefficient of restitution : [0, 1]
        """

        self.state = np.array(state)
        self.size  = size
        self.m     = m*np.ones(self.state.shape[0])
        self.e     = e

class Arena:
    """
    class that implements the basic fiels that contain particles
    and its properties and how it evolves in time.
    """

    def __init__(self, particles, boundary, g=9.8):
        """
        particles : instance of Particles class
        boundary  : boundary of Arena
        """
        self.particles = particles
        self.time      = 0.0           # start the world
        self.boundary  = boundary
        self.g         = g

    def proceed(self, dt):
        """
        Proceed the Arena from time t to t + dt seconds
        Change the state of the particles in the arena accouding to that
        """

        self.time += dt
        # update state
        # positions : 
        self.particles.state[:, :2] += self.particles.state[:, 2:]*dt

        # finding and updating velocity of collided particles
        # distance matrix : (i, j) value indicate distance between i and jth particle
        dist = squareform(pdist(self.particles.state[:, :2]))
        # finding index of collided particles
        i, j =  np.where(dist < 2*self.particles.size)
        # avoid double counting
        collided = (i < j)
        i = i[collided]
        j = j[collided]

        for i1, i2 in zip(i, j):
            m1 = self.particles.m[i1]
            m2 = self.particles.m[i2]
            e  = self.particles.e

            #location vector
            r1 = self.particles.state[i1,:2]
            r2 = self.particles.state[i2,:2]

            #velocity
            v1 = self.particles.state[i1,2:]
            v2 = self.particles.state[i2,2:]

            # inelastic collition formula
            v1f = (v1*(m1-(e*m2))+(1+e)*v2*m2)/(m1+m2)
            v2f = (v2*(m2-e*m1)+(1+e)*v1*m1)/(m1+m2)

            self.particles.state[i1,2:] = v1f
            self.particles.state[i2,2:] = v2f

        # checking whether the particle is at boundary:
        x_left    = (self.particles.state[:, 0] < self.boundary[0] + self.particles.size)
        x_right   = (self.particles.state[:, 0] > self.boundary[1] - self.particles.size)
        y_bottom  = (self.particles.state[:, 1] < self.boundary[2] + self.particles.size)
        y_top     = (self.particles.state[:, 1] > self.boundary[3] - self.particles.size)

        # updating position of passed particles
        self.particles.state[x_left   , 0] = self.boundary[0] + self.particles.size
        self.particles.state[x_right  , 0] = self.boundary[1] - self.particles.size
        self.particles.state[y_bottom , 1] = self.boundary[2] + self.particles.size
        self.particles.state[y_top    , 1] = self.boundary[3] - self.particles.size

        # velocity also reversed
        self.particles.state[x_left | x_right, 2] *= -self.particles.e
        self.particles.state[y_bottom | y_top, 3] *= -self.particles.e

        # gravity : add if you want it
        # self.particles.state[:, 3] -= self.particles.m * self.g * dt

############################################################################################
# start of execution
# defining initial state
np.random.seed(0)                          # seeding random
state = -0.5 + np.random.random((50,4))    # particles with random position and velocity
state[:,:2] *= 4.0                         # scaling initial velocity

# defining particles and arena
particles = Particles(state)
boundary = [-2,2,-2,2]
arena = Arena(particles, boundary)
dt = 0.025                                 # descrete time step 

# Animation
fig = plt.figure()
fig.subplots_adjust(left   = 0,
                    right  = 1,
                    bottom = 0,
                    top    = 1)
ax = fig.add_subplot(111, aspect='equal',
                     autoscale_on=False,
                     xlim=(-3.0, 3.0),
                     ylim=(-3.0, 3.0))
plt.axis("off")                      # turn axis off because we don't wanr that
# plotting 
N  = state.shape[0]                  # total number of particles
# finding marker size
dx = ax.get_xbound()
dx = dx[1] - dx[0]
fraction = fig.get_figwidth() / dx
size = arena.particles.size
ms = int(fig.dpi * 2 * size * fraction) #markersize

p, = ax.plot([], [], 'bo', ms=ms)       # Represents all particles                    
selected_p       = np.random.randint(N)          # A random particle for highlight
p_highlight,     = ax.plot([], [], 'ro', ms=ms)  # highlighted particle
highlight_path,  = ax.plot([], [], "r-", lw=1)   # path of highlighted particle
highlight_path_x = [state[selected_p, 0]]        # x coordinate of highlighted
highlight_path_y = [state[selected_p, 1]]        # y coordinate of highlighted

ms = int(fig.dpi * 2 * arena.particles.size *\
         fig.get_figwidth()/np.diff(ax.get_xbound())[0]) #markersize

#drawing rectangular box
rect = plt.Rectangle(arena.boundary[::2],                    # bottom left corner
                     arena.boundary[1] - arena.boundary[0],  # length (x axis)
                     arena.boundary[3] - arena.boundary[2],  # width  (y axis)
                     ec='k', lw=2, fc='none')
ax.add_patch(rect)

def init():
    """
    initialisation funtion for animation
    """
    p.set_data([],[])
    p_highlight.set_data([], [])
    highlight_path.set_data([], [])

    return p, p_highlight, highlight_path

def animate(i):
    """
    animation routine for matplotlib.animation
    """
    arena.proceed(dt)                                              # proceed to next step
    highlight_path_x.append(arena.particles.state[selected_p, 0])  # add path of highlighted
    highlight_path_y.append(arena.particles.state[selected_p, 1])

    # updating plot
    p.set_data(arena.particles.state[:,0],
               arena.particles.state[:,1])
    p_highlight.set_data(arena.particles.state[selected_p,0],
                         arena.particles.state[selected_p,1])
    highlight_path.set_data(highlight_path_x, highlight_path_y)

    return p, p_highlight, highlight_path

ani = animation.FuncAnimation(fig, animate,
                              frames=2000,
                              interval=10,
                              blit=True,
                              init_func=init)
ani.save('output/brownian_motion.mp4', fps=100)
# plt.show()
