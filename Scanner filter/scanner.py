from PIL import Image
import numpy as np
import cv2


class scanner:
	
	"""Scanner effect
		This class will apply applies a scanner effect to an image
		by maximizing white colour pixels, scaling the contrast 
		and enhancing sharpness. 
	"""
	
	def __init__(self):
		pass

	def resize(self,image,window_height = 500):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	
	
	def map(x, in_min, in_max, out_min, out_max):
		return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

	def sharp(self, image):
		# Create our shapening kernel
		kernel = np.zeros( (9,9), np.float32)
		kernel[4,4] = 2.0   #Identity, times two 

		#Create a box filter:
		boxFilter = np.ones( (9,9), np.float32) / 97.0

		#Subtract the two:
		kernel = kernel - boxFilter

		# applying the sharpening kernel to the input image & displaying it.
		sharpened = cv2.filter2D(image, -1, kernel)
		sharpened = cv2.bilateralFilter(sharpened, 9, 75, 75) # Noise reduction
		return sharpened

	def saturation(self, image):
		hsvimage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV).astype("float32")

		(h,s,v) = cv2.split(hsvimage)
		s=s*1.2
		v=v+2
		h=h-2
		s = np.clip(s,0,255)
		v = np.clip(v,0,255)
		h = np.clip(h,0,255)
		hsvimage = cv2.merge([h,s,v])

		return hsvimage

	def whitebalance(self, image):

		value = 125
		h, s, v = cv2.split(image)

		lim = 255 - value
		v[((v > lim) & (v < 190))] = 200

		v[v <= lim] += 13#map(v,0,lim,0,255)
		cv2_image = cv2.merge((h, s, v))
		return cv2_image

	# Method to process the red band of the image
	def normalizeRed(self, intensity):
		iI = intensity
		minI = 59
		maxI = IR[1]

		minO = 0
		maxO = 255

		iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)+20
		return iO


	# Method to process the green band of the image
	def normalizeGreen(self, intensity):
		iI = intensity  
		minI = 54
		maxI = IG[1]

		minO = 0
		maxO = 255

		iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)+20
		return iO


	# Method to process the blue band of the image
	def normalizeBlue(self, intensity):
		iI = intensity
		minI = 59
		maxI = IB[1]

		minO = 0
		maxO = 255

		iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)+20
		return iO 



image = cv2.imread("./doc.jpg")
tmp_canvas = scanner()
cv2_image = tmp_canvas.sharp(image)				#resize no used before sharpness filtering as degrades picture quality
image = tmp_canvas.resize(image,500)
cv2_image = tmp_canvas.resize(cv2_image,500)
cv2_image = tmp_canvas.saturation(cv2_image)

cv2_image = tmp_canvas.whitebalance(cv2_image)

cv2_image = cv2.cvtColor(cv2_image.astype("uint8"),cv2.COLOR_HSV2RGB)

pil_image = Image.fromarray(cv2_image)

#imageObject.show()

# Split the red, green and blue bands from the Image
multiBands = pil_image.split()


IR = multiBands[0].getextrema()
IG = multiBands[1].getextrema()
IB = multiBands[2].getextrema()


# Apply point operations that does contrast stretching on each color band
normalizedRedBand = multiBands[0].point(tmp_canvas.normalizeRed)

normalizedGreenBand = multiBands[1].point(tmp_canvas.normalizeGreen)

normalizedBlueBand = multiBands[2].point(tmp_canvas.normalizeBlue)

# Create a new image from the contrast stretched red, green and blue brands
normalizedImage = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))

normalizedImage.show()
# Display the original image 
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)
#image = image.resize((500,700))
image.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
