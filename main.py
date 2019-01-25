import argparse as arg
import sys

import blacknwhite_filter
import cartoon_filter
import sketch_filter
import negative_filter
import vintage_filter
import cool_filter

bnw = blacknwhite_filter.BlacknWhite()
crt = cartoon_filter.Cartoonizer()
skch = sketch_filter.Sketcher()
ngtv = negative_filter.Negative()
vntg = vintage_filter.Vintage()
cool = cool_filter.Cool()

parser = arg.ArgumentParser('Image-Filters')

parser.add_argument("-i", "--image", required = True,  metavar = '', help = "Input Image Path")
args = parser.parse_args()

#main function
if __name__ == '__main__':
	print("Please select filter :\n" \
		"1. Black and White\n" \
		"2. Cartoon\n" \
		"3. Cool\n" \
		"4. Sketch\n" \
		"5. Negative\n" \
		"6. Vintage\n" \
		"0 to exit\n")
	
	filter_num = input("Select filters from 1, 2, 3, 4, 5, 6 : ")
	while(filter_num != 0):
		if(filter_num == "1"):

			bnw.start(args.image)
	
		elif(filter_num == "2"):

			crt.start(args.image)

		elif(filter_num == "3"):

			cool.start(args.image)

		elif(filter_num == "4"):

			skch.start(args.image)

		elif(filter_num == "5"):

			ngtv.start(args.image)

		elif(filter_num == "6"):

			vntg.start(args.image)

		elif(filter_num == "0"):

			print("Exit")
			sys.exit()

		filter_num = input("\nSelect filters from 1, 2, 3, 4, 5, 6 : ")
