import cv2
class BlacknWhite(object):
	"""BlacknWhite Filter
		A class that applies BlacknWhite filter to an image.
		The class uses downsampling, bilateral filter and upsampling to create
		a BlacknWhite filter.
	"""
	def __init__(self):
		pass

	def resize(self,image,window_height = 500):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	
	
	def render(self, img_rgb):
		img_rgb = cv2.imread(img_rgb)
		img_rgb = self.resize(img_rgb,500)
		numDownSamples = 2       # number of downscaling steps
		numBilateralFilters = 50  # number of bilateral filtering steps

		# -- STEP 1 --
		# downsample image using Gaussian pyramid
		img_color = img_rgb
		for _ in range(numDownSamples):
			img_color = cv2.pyrDown(img_color)
		#cv2.imshow("downcolor",img_color)
		#cv2.waitKey(0)
		# repeatedly apply small bilateral filter instead of applying
		# one large filter
		for _ in range(numBilateralFilters):
			img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
		#cv2.imshow("bilateral filter",img_color)
		#cv2.waitKey(0)
		# upsample image to original size
		for _ in range(numDownSamples):
			img_color = cv2.pyrUp(img_color)
		#cv2.imshow("upscaling",img_color)
		#cv2.waitKey(0)
		# -- STEPS 2 and 3 --
		# convert to grayscale and apply median blur
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
		return img_gray

	def start(self, img_path):
		tmp_canvas =BlacknWhite() #make a temporary object
		file_name = img_path #File_name will come here
		res = tmp_canvas.render(file_name)
		cv2.imwrite("BlacNwhite_version.jpg", res)
		cv2.imshow("BlacNwhite version", res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("Image saved as 'BlacNwhite_version.jpg'")
