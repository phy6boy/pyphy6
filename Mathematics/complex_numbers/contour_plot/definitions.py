import numpy as np

def to_polar(x, y):
	"""
	Take two numbers or np arrays and return polar representation
	of the comblex number(s) x + Iy
	Return:
		tuple (r, arg)
	"""
	r = np.sqrt(x**2 + y**2)
	arg = np.arctan2(y, x)
	return r, arg

def to_cartisian(r, theta):
	"""
	Take two numbers or np arrays and return cartisian representation
	of the comblex number(s) r*exp(i*theta)
	Return:
		tuple (x, y)
	"""
	x = r*np.cos(theta)
	y = r*np.sin(theta)
	return (x, y)

######################## FUNCTION DEFINITIONS #################################

def complex_log(r, theta, polar=True):
	"""
	returns complex logarithm as an ordered pair (u, v)
	for a result u + Iv in complex plane.
	Input:
		If polar is True, then input (r, theta) is represented as
		r*e^(i*theta) else the complex representation is taken as r + I*theta
	"""
	if not polar:
		r, theta = to_polar(r, theta)
	u = np.log(r)
	v = theta
	return u, v

def complex_sqrt(r, theta, polar=True):
	"""
	returns complex square root as an ordered pair (u, v)
	for a result u + Iv in complex plane
	Input:
		If polar is True, then input is (r, theta)
		else input is (x, y)
	"""
	if not polar:
		r, theta = to_polar(r, theta)
	u = np.sqrt(r)*np.cos(theta/2)
	v = np.sqrt(r)*np.sin(theta/2)
	return u, v

def f1(r, theta, polar=True):
	"""
	f(z) = sqrt(z**2 + 1)
	"""
	if not polar:
		r, theta = to_polar(r, theta)
	x = r**2 * np.cos(2*theta) + 1
	y = r**2 * np.sin(2*theta)
	u, v = complex_sqrt(x, y, polar=False)
	return u, v

########################## CONTOUR DEFINITIONS #################################

def contour_circle(x0, y0, r0, theta):
	"""
	returns contour as tuple of numpy arrays
	the length of contour is equal to tat of 
	theta. theta should be a numpy array
	The contour is a circle centered at (x0, y0) 
	with radius r0.
	Returns: 
		ordered pain of cartitian form of complex
		number : (x, y)
	"""
	R = np.sqrt(x0**2 + y0**2)
	angle = np.arctan2(y0, x0)

	x = (R*np.cos(angle) + r0*np.cos(theta))
	y = (R*np.sin(angle) + r0*np.sin(theta))
	return (x, y)

def contour_rectangle(x0, y0, l, b, n):
	"""
	Returns rectangle contour as (x, y)
	Input:
		x0, y0 : coordinate of upper left corner
		l, b : length and breadth
		n : number of samples
	"""
	# sharing n over l and b
	nl = int(n/2 * l/(l+b))
	nb = int(n/2 * b/(l+b)) + 1
	l1x = np.linspace(x0, x0+l, nl)
	l1y = np.ones(nl)*y0
	l2x = l1x[::-1]
	l2y = np.ones(nl)*(y0-b)
	b1x = np.ones(nb)*(x0+l)
	b1y = np.linspace(y0, y0-b, nb)
	b2x = np.ones(nb)*x0
	b2y = b1y[::-1]
	x = np.concatenate([l1x, b1x, l2x, b2x])
	y = np.concatenate([l1y, b1y, l2y, b2y])
	# x = np.concatenate([b1x[nb//2:0:-1], l1x[::-1], b2x[::-1], l2x[::-1], b1x[-1:nb//2 -15:-1]])
	# y = np.concatenate([b1y[nb//2:0:-1], l1y[::-1], b2y[::-1], l2y[::-1], b1y[-1:nb//2 -15:-1]])

	return (x, y)

#################################################################################
