import sys
import cv2
import os
import time
from PIL import Image as Img
from PIL import ImageTk
from tkinter import filedialog
import gtts as gTTS
from tkinter import *
import tkinter.messagebox

import blacknwhite_filter
import cartoon_filter
import sketch_filter
import negative_filter
import vintage_filter
import cool_filter
import dull

bnw = blacknwhite_filter.BlacknWhite()
crt = cartoon_filter.Cartoonizer()
skch = sketch_filter.Sketcher()
ngtv = negative_filter.Negative()
vntg = vintage_filter.Vintage()
cool = cool_filter.Cool()
dull = dull.Dull()

class Window:
	global imageWindow
	global path

	def __init__(self, master):

		master.title("Image Filters")
		master.configure(background='black')
		master.geometry("800x800+500+300")

		self.imageWindow = None
		self.path = ''


		# Load image button
		self.load_button = Button(master, text="Load image", command=self.select_image, bg="orange", relief=RAISED)
		self.load_button.pack(side=TOP, anchor=E)

		#  filter buttons
		self.bnw_button = Button(master, text="Black N White", command=self.BlackNwhite_filter, bg="orange", relief=RAISED)
		self.bnw_button.pack(side=TOP, anchor=E, expand="yes")

		self.crt_button = Button(master, text="Cartoon", command=self.Cartoon_filter, bg="orange", relief=RAISED)
		self.crt_button.pack(side=TOP, anchor=E, expand="yes")

		self.skch_button = Button(master, text="Sketch", command=self.Sketch_filter, bg="orange", relief=RAISED)
		self.skch_button.pack(side=TOP, anchor=E, expand="yes")

		self.ngtv_button = Button(master, text="Negative", command=self.Negative_filter, bg="orange", relief=RAISED)
		self.ngtv_button.pack(side=TOP, anchor=E, expand="yes")

		self.vntg_button = Button(master, text="Vintage", command=self.Vintage_filter, bg="orange", relief=RAISED)
		self.vntg_button.pack(side=TOP, anchor=E, expand="yes")

		self.cool_button = Button(master, text="Cool", command=self.Cool_filter, bg="orange", relief=RAISED)
		self.cool_button.pack(side=TOP, anchor=E, expand="yes")

		self.cool_button = Button(master, text="Dull", command=self.Dull_filter, bg="orange", relief=RAISED)
		self.cool_button.pack(side=TOP, anchor=E, expand="yes")

		# Quit Button
		self.quit_button = Button(master, text="Quit", command=master.quit, bg="orange", relief=RAISED)
		self.quit_button.pack(side=TOP, anchor=E, expand="yes")

	def BlackNwhite_filter(self):
		bnw.start(self.path)

	def Cartoon_filter(self):
		crt.start(self.path)

	def Sketch_filter(self):
		skch.start(self.path)

	def Negative_filter(self):
		ngtv.start(self.path)

	def Vintage_filter(self):
		vntg.start(self.path)
	
	def Cool_filter(self):
		cool.start(self.path)

	def Dull_filter(self):
		dull.start(self.path)

	# function to select and load image 
	def select_image(self):

		# get image path
		self.path = filedialog.askopenfilename()
		
		if len(self.path) > 0:
			image = cv2.imread(self.path) #read image
			image = cv2.resize(image, (500, 600)) #resize image
			cv2.imwrite("original_image.jpg", image) #save original image
			# swap channels
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

			# convert image to PIL format
			image = Img.fromarray(image)

			# convert image to ImageTk format
			image = ImageTk.PhotoImage(image)

		# if the image window is None, initialize it
		if self.imageWindow is None:
			self.imageWindow = Label(image=image)
			self.imageWindow.image = image
			self.imageWindow.pack(side=LEFT)

		# otherwise, update the window
		else:
			self.imageWindow.configure(image=image)
			self.imageWindow.image = image


# initialize the app window
root = Tk()

b = Window(root)
root.mainloop()