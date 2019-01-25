import cv2
import numpy as np

img = cv2.imread('beach.jpg') # gets the input image

s = 128

def resize(image,window_height = 500):
	aspect_ratio = float(image.shape[1])/float(image.shape[0])
	window_width = window_height/aspect_ratio
	image = cv2.resize(image, (int(window_height),int(window_width)))
	return image	


def apply_brightness_contrast(input_img, brightness = 0, contrast = 0): # function to adjust brightnes, contrast and make the image dull


	if brightness != 0:
		if brightness > 0:
			shadow = brightness
			highlight = 255
		else:
			shadow = 0
			highlight = 255 + brightness
		alpha_b = (highlight - shadow)/255
		gamma_b = shadow

		buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
	else:
		buf = input_img.copy()

	if contrast != 0:
		f = 131*(contrast + 127)/(127*(131-contrast))
		alpha_c = f
		gamma_c = 127*(1-f)

		buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

	return buf

blist = [0, -127, 127,   0,  0, 64] # list of brightness values
clist = [0,    0,   0, -64, 64, 64] # list of contrast values

img = resize(img, 500)


out = np.zeros((s*2, s*3, 3), dtype = np.uint8)
out = apply_brightness_contrast(img, -127, 0)
cv2.imshow('car.jpg', img) 
cv2.imshow('out.png', out) 
cv2.imwrite('out.png', out)

cv2.waitKey(0)
cv2.destroyAllWindows()