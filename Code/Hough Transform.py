import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import math,sys
from math import cos,sin,pi
from VisionSecond import Sobel
from collections import defaultdict
from PIL import Image, ImageDraw

rmin = 10
rmax = 20
theta = 360
threshold = 0.18

#For coins use threshold = 0.18 and votes >= 355 (line 49)
#For firstfloor use threshold = 0.20 and votes >= 360

def Hough():
	#LOAD IMAGE
	Img = Image.open(sys.argv[1])
	img = np.array(Image.open(sys.argv[1]))
	size_of_image = Img.size
	 
	image = Image.new("RGB", size_of_image)
	image.paste(Img)

	#GET EDGES
	edges = Sobel(img,threshold)
	rows = len(edges)
	cols = len(edges[0])

	#CREATE ACCUMULATOR
	Acc = defaultdict(int)
	for x in range(rows):
		for y in range(cols):
			if edges[x,y] == 255:
				for r in range(rmin, rmax+1):
					for t in range(0,theta,1):
						a = x - abs(int(r * cos(pi*t/180)))
						b = y - abs(int(r * sin(pi*t/180)))
						Acc[(a,b,r)] += 1
	
	#FIND CIRCLES WITH MOST VOTES
	circles = []
	sorted_Acc =  sorted(Acc.items(), key=lambda i: -i[1])

	for c,votes in sorted_Acc:
			a, b, r = c
			if votes >= 355 and all(abs(x-a)>7 and abs(y-b)>8 for x,y,r in circles):
				circles.append((a,b,r))

	ready_image = ImageDraw.Draw(image)
	for a, b, r in circles:
		 ready_image.ellipse((b-r, a-r, b+r, a+r), outline=(0,255,0,0))	

	#SAVE IMAGE
	image.save("Hough_image.png")

Hough()