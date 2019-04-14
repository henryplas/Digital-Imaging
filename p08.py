import numpy as np
import glob
import skimage
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage import img_as_float64, img_as_ubyte

def image_test():
	file = glob.glob('Y0030001.jpg')
	for thing in file:
		image = io.imread(thing)
	image = image[460:-460,880:-680]
	image = resize(image, (299,299), anti_aliasing=False)
	image = img_as_float64(image) / 2
	image = img_as_ubyte(image)
	io.imsave('test.jpg', image)

def average_maker():

	average = np.zeros((299,299,3))
	n = 1000
	files = glob.glob('101MEDIA/*.jpg')
	for file in files:
		image = io.imread(file)
		image = image[460:-460,880:-680]
		# image = rgb2gray(image)
		image = resize(image, (299,299), anti_aliasing=True)
		image = img_as_float64(image)
		average = average + image

	average = img_as_ubyte(average / n)
	io.imsave('average.jpg', average)
	

def difference_maker():
	average = io.imread('average.jpg')
	average = img_as_float64(average)
	n = 0
	for file in glob.glob('beePics/*.jpg'):
		image = io.imread(file)

		image = image[460:-460,880:-680]
		image = resize(image, (299,299), anti_aliasing=True)
		image = img_as_float64(image)
		image = abs(average - image)

		name = 'difference' + str(n) + '.png'
		image = img_as_ubyte(image)
		image = rgb2gray(image)
		io.imsave(name, image)
		n += 1


# image_test()
# average_maker()
difference_maker()











