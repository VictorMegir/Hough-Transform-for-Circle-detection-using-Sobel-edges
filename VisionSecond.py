import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import scipy,sys
from PIL import Image, ImageDraw
from scipy import signal
from scipy import misc
from PIL import Image

def thres(threshold,Smag):
	max_value = np.amax(Smag)
	threshold *= max_value
	for i in range(1,len(Smag)):
		for j in range(1,len(Smag[1])):
			if Smag[i,j] > threshold :
				Smag[i,j] = 255
			else:
				Smag[i,j] = 0
	return Smag

def checkArgs():
	if(len(sys.argv)<3):
	    print("Too few arguments.Input an image and a threshold.")
	    quit()

	global imge,threshold,img_size
	imge = Image.open(sys.argv[1])
	threshold = float(sys.argv[2])
	img_size = imge.size

	
	if threshold < 0 or threshold > 1:
		print("Threshold must be between 0 and 1")
		quit()
	
def Sobel(imge,threshold):
	imge = np.array(imge)
	width = len(imge)
	height = len(imge[1])
	if len(imge.shape) == 3:
		iya = np.zeros((width,height))
		for i in range(1,width):
			for j in range(1,height):
				s = 0
				for z in range(0,2):
					s += imge[i,j,z]
				iya[i,j] = s/3
	else:
		iya = imge
	        
	Cx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
	Cy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

	Sx = scipy.signal.convolve2d(iya,Cx,mode='full', boundary='fill', fillvalue=0)
	Sy = scipy.signal.convolve2d(iya,Cy,mode='full', boundary='fill', fillvalue=0)

	Smag = abs(Sx) + abs(Sy)
	Simage = thres(threshold,Smag)
	return Simage

def main():
	checkArgs()
	Simage = Sobel(imge,threshold)
	imgplot = plt.imshow(Simage, cmap = 'Greys_r')
	plt.savefig("Edge_map.png")
	plt.show()
	
#main()