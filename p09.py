import sklearn
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture 
import skimage
from skimage import io
import glob
import numpy as np
import matplotlib.pyplot as plt


def load_image() :
	image = glob.glob('Y0030001.jpg')
	for thing in image:
		image = io.imread(thing)
	return image


def gauss_mix(flat_image,shape,n=2):
	guass = GaussianMixture(n_components=n)
	guass.fit(flat_image)
	c = guass.predict(flat_image)
	c = c.reshape((shape))
	img = plt.imshow(c)
	plt.show()

def color_classifier(flat_image,shape,n=2):
	kmeans = KMeans(n_clusters=n, n_jobs=-1)
	kmeans.fit(flat_image)
	c = kmeans.predict(flat_image)
	c = c.reshape((shape))
	img = plt.imshow(c)
	plt.show()


f = np.array(load_image())
shape = f.shape[0], f.shape[1]
x = f.reshape((f.shape[0] * f.shape[1], 3))
gauss_mix(x,shape,4)