import cv2

class Vintage(object):
	"""Vintage filter ---
		This class will apply vintage filter to an image 
		by applying a sepia tone to the image.
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
		img_rgb = self.resize(img_rgb, 500)
		img_color = img_rgb
		
		newImage = img_color.copy()
		i, j, k = img_color.shape
		for x in range(i):
			for y in range(j):
				R = img_color[x,y,2] * 0.393 + img_color[x,y,1] * 0.769 + img_color[x,y,0] * 0.189
				G = img_color[x,y,2] * 0.349 + img_color[x,y,1] * 0.686 + img_color[x,y,0] * 0.168
				B = img_color[x,y,2] * 0.272 + img_color[x,y,1] * 0.534 + img_color[x,y,0] * 0.131
				if R > 255:
					newImage[x,y,2] = 255
				else:
					newImage[x,y,2] = R
				if G > 255:
					newImage[x,y,1] = 255
				else:
					newImage[x,y,1] = G
				if B > 255:
					newImage[x,y,0] = 255
				else:
					newImage[x,y,0] = B

		return newImage

	def start(self, img_path):
		tmp_canvas = Vintage()
		file_name = img_path #File_name will come here
		res = tmp_canvas.render(file_name)
		cv2.imwrite("Vintage_version.jpg", res)
		cv2.imshow("Vintage Version", res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("Image saved as 'Vintage_version.jpg'")
