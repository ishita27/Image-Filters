import cv2
import numpy as np

class black_board:
	"""black board filter ---
		This class will apply black board filter to an image 
		by applying reducing a certain threshold colour values 
		to zero of the image.
	"""

	def __init__(self):
		pass

	def resize(self,image,window_height = 500):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	
		
	def render(self,image):
		# Create sharpening kernel
		kernel = np.array([[1,-1,0], [-1,4,-1], [-1,0,-1]])

		# applying the sharpening kernel to the input image & displaying it.
		drawing = cv2.filter2D(image, -1, kernel)

		# Noise reduction
		drawing = cv2.bilateralFilter(drawing, 9, 75, 75) 
		return drawing

	def start(self, img_path):
		# Create an image object
		image = cv2.imread(img_path)
		tmp_canvas = black_board()
		image = tmp_canvas.resize(image,500)
		res = tmp_canvas.render(image)
		cv2.imwrite('black board drawing.jpg', res)
		cv2.imshow('original',image)
		cv2.imshow('black canvas',res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
