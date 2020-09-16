import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from svg_parser import parse_svg

def fourier_coefficients(X, Y, T, nrange):
    """
    Given X and Y in real space, 
    compute cofficients of fourier series 
    """
    # N = len(X)
    # T = np.linspace(0.0, 1.0, N)
    dt = T[1] - T[0]
    # The array storing cofficients
    Cr = np.zeros(2*nrange + 1, dtype=float)    # real part
    Cc = np.zeros(2*nrange + 1, dtype=float)    # complex part

    for n in range(-nrange, nrange+1):
        s = np.sum(np.exp(-2*np.pi*1j*n*T)*(X + Y*1j)*dt)
        Cr[n+nrange] = s.real
        Cc[n+nrange] = s.imag

    return Cr, Cc

def get_function_and_vectors(Cr, Cc, T, nrange):
    """
    get the position and list of vectors for all positions
    from calculated data
    X : 1d np.array
    Y : 1d np.array
    vectors : 3d np array:
        1st index : Time index
        2nd index : N index
        3rd index : 2, one real and one imag
    """
    N = np.array(range(-nrange, nrange+1))
    X = np.zeros(len(T), dtype=float)
    Y = np.zeros(len(T), dtype=float)
    vectors = np.zeros((len(T), len(N), 2), dtype=float)

    i = 0
    for t in T:
        s = (Cr + Cc*1j)*np.exp(N * 2 * np.pi * 1j*t)
        vectors[i, :, 0] = s.real
        vectors[i, :, 1] = s.imag
        X[i] = np.sum(s).real
        Y[i] = np.sum(s).imag
        i += 1

    return X, Y, vectors

######################################################################
# First, load the dataset
infile = "india.svg"
outfile = "india.mp4"
X , Y = parse_svg(f"input/{infile}")
N = len(X)
T = np.linspace(0.0, 1.0, N)
nrange = 500
ndraw  = 50    # this is the nrange to draw
# Now calculate fourier coefficients
Cr, Cc = fourier_coefficients(X, Y, T, nrange)
# recalculate the data using This coefficents
X1, Y1, vectors = get_function_and_vectors(Cr, Cc, T, nrange)

# animate
# plt.style.use("dark_background")
fig   = plt.figure()
ax    = fig.add_subplot(111, xlim=[-150, 150], ylim=[-150, 150])
plt.axis("off")

def animate(i):
    ax.clear()
    plt.xlim(-150, 150)
    plt.ylim(-150, 150)
    plt.axis("off")
    print("\r" + str(i) + "/1000", end="")
    line, = ax.plot(X1[:i], Y1[:i], color="b")
    v = np.array(sorted(vectors[i, :, 0] + vectors[i, :, 1]*1j,
                             key=lambda i: abs(i), reverse=True))
    v = v[:ndraw]
    
    #drawing vectors
    tipx = 0
    tipy = 0
    vectorlist = []
    for p in v:
        vector = ax.arrow(tipx, tipy, p.real, p.imag, head_width=2.5,
                             head_length=2.5, fc="red", ec="#009034")
        tipx += p.real
        tipy += p.imag
        vectorlist.append(vector)

    return (line, *vectorlist)

anim = animation.FuncAnimation(fig, animate,
                               frames=N, repeat=False, blit=True)
# plt.show()
writer = animation.FFMpegWriter(fps=50, bitrate=-1)
anim.save(f"./output/{outfile}", writer=writer)

# save to file
