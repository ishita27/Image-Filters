import cv2
import numpy as np
import argparse
import random
import os, sys

class old_filter(object):
	"""old_filter effect
		A class that applies a random old filter effect to an image
		using a set of pre-designed filters and applying Arithmetic 
		Operations on Image to add the filter effect on it.
	"""
	
	def __init__(self):
		pass
	
	#function to resize
	#according to the aspect ratio of the image
	def resize(self,image,window_height = 500):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	

	#function that renders the image
	def render(self, img_rgb):
		img = cv2.imread(img_rgb,0)
		img = self.resize(img, 500)
		
		filtern = []
		filters = list(range(1,7))
		for l in filters:
			filtern.append(str(l) +'n')

		#filtern -> stores numbers (1-7) with preceeding n
		#filters -> all numbers (1-7) and elements of filtern
		filters.extend(filtern)
		
		#selects random filter everytime
		selectedfilter = str(random.choice(filters))
		#print(selectedfilter)
		#filter path in generalized form to work in all systems
		filter_path = os.path.abspath(os.path.join('oldfilters','old' + selectedfilter + '.jpg'))
		
		if selectedfilter.endswith('n'):
			#selected file is an normal filter and Arithmetic addition 
			#needs to be applied on it 
			
			old = cv2.imread(filter_path,0)
			old = cv2.resize(old,(img.shape[1],img.shape[0]))
			#cv2.imshow('filter',old)
			#cv2.imshow('image',img)
			
			#Arithmetic add
			add=cv2.add(img,old)
			return add

					
		else:
			#selected file is an inverted filter and Weighted addition 
			#needs to be applied on it 
			
			old = cv2.imread(filter_path, 0)
			old = cv2.resize(old,(img.shape[1],img.shape[0]))
			#print old.shape
			#for i in range(old.shape[0]):
			#	 for j in range(old.shape[1]):
			#		if old[i][j]>200:
			#			old[i][j]=255
			#cv2.imshow('filter',old)
			#cv2.imshow('image',img)
			
			#Weightedadd
			add=cv2.addWeighted(img,0.7,old,0.3,0)
			return add
					

	def start(self, img_path):
		#make a temporary object
		tmp_canvas = old_filter()
		#File_name will come here
		file_name =  img_path
		res = tmp_canvas.render(file_name)
		cv2.imwrite("oldcar.jpg", res)
		cv2.imshow("old version", res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("Image saved as 'car.jpg'")
