import cv2
import numpy as np

class sharpening:
	"""sharpening filter ---
		This class will apply sharpening filter to an image 
		by applying a defined kernel values to the image.
	"""

	def __init__(self):
		pass
	
	def resize(self,image,window_height = 500):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	

	def sharp(self,image):
		# Create sharpening kernel
		kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

		# applying the sharpening kernel to the input image & displaying it.
		sharpened = cv2.filter2D(image, -1, kernel)

		# Noise reduction
		sharpened = cv2.bilateralFilter(sharpened, 9, 75, 75) 
		return sharpened

	def start(self, img_path):
		# Create an image object
		image = cv2.imread(img_path)
		image = self.resize(image, 500)
		tmp_canvas = sharpening()
		res = tmp_canvas.sharp(image)
		cv2.imwrite('sharped.jpg', res)
		cv2.imshow('original',image)
		cv2.imshow('sharp',res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
