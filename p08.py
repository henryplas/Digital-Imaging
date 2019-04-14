import numpy as np
import glob
import skimage
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage import img_as_float64, img_as_ubyte



#I used this function to test out data types and the functions that I used
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
	#Some quick initializations, create an empty array to hold the image sums
	#before addition and division
	average = np.zeros((299,299,3))
	n = 1000 #known value of 1000 images
	files = glob.glob('101MEDIA/*.jpg') # I had a folder of images with this name
	
	for file in files:
		image = io.imread(file)
		
		#find 1000x1000x3 section of the image that is important
		image = image[460:-460,880:-680]
		image = resize(image, (299,299), anti_aliasing=True)
		image = img_as_float64(image) #convert to floats for math
		average = average + image

	average = img_as_ubyte(average / n) # covert back to 8 bit before saving image
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

		name = 'difference' + str(n) + '.png' # creting new names
		image = img_as_ubyte(image)
		image = rgb2gray(image) # convert to greyscale for ease of analysis
		io.imsave(name, image) #save new image after every interation
		n += 1


# image_test()
average_maker()
difference_maker()












