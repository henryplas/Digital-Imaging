import numpy as np 

def nearest_interpolation(f, new_shape):

	i = np.arange(0,new_shape[0])
	j = np.arange(0,new_shape[1])

	x = (f.shape[0] / (2 * new_shape[0])) + i * (f.shape[0] / (new_shape[0])) - 0.5
	y = (f.shape[1] / (2 * new_shape[1])) + j * (f.shape[1] / (new_shape[1])) - 0.5

	yy, xx = np.meshgrid(y, x)

	jj = np.round(yy).astype(int)
	ii = np.round(xx).astype(int)

	g = f[ii,jj]

	return g

def bilinear_interpolation(x, new_shape):
	i = np.arange(0,new_shape[0])
	j = np.arange(0,new_shape[1])

	q = (x.shape[0] / (2 * new_shape[0])) + i * (x.shape[0] / (new_shape[0])) - 0.5
	
	y = (x.shape[1] / (2 * new_shape[1])) + j * (x.shape[1] / (new_shape[1])) - 0.5

	yy, xx = np.meshgrid(y, q)

	positions = (xx, yy)

	nearest_i0 = np.maximum(0, np.floor(positions[0]).astype(int)).astype(int)
	nearest_i1 = np.minimum(x.shape[0] - 1, np.ceil(positions[0]).astype(int)).astype(int)
	nearest_j0 = np.maximum(0, np.floor(positions[1]).astype(int)).astype(int)
	nearest_j1 = np.minimum(x.shape[1] - 1, np.ceil(positions[1]).astype(int)).astype(int)
	
	i_frac = positions[0] - nearest_i0
	j_frac = positions[1] - nearest_j0

	a = x[nearest_i0, nearest_j0]
	b = x[nearest_i0, nearest_j1]
	c = x[nearest_i1, nearest_j0]
	d = x[nearest_i1, nearest_j1]

	e = (1-i_frac)*a + i_frac*c
	f = (1-i_frac)*b + i_frac*d
	g = (1-j_frac)*e + j_frac*f
	g = np.where(g >= 0.5, np.ceil(g), np.floor(g))

	return g


def fourier_transform(x):
	x = np.array(x, np.complex)
	width = x.shape[0]
	n = np.arange(width)
	k = n.reshape((width, 1))
	t = np.exp((-1 * 2 * 1j * np.pi * k * n) / width)
	g = t @ x
	return g

def fourier_transform_2d(f):
	g = fourier_transform(f)
	g = fourier_transform(g.T).T
	return g


