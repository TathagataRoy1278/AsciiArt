import cv2
import random
from tkinter import *
import math
def send(a,ii,d):
	grayImage = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
	tmp = grayImage
	grayImage = cv2.threshold(grayImage,ii,255,cv2.THRESH_BINARY)
	grayImage = grayImage[1]
	#cv2.imshow("k",grayImage)

	#cv2.waitKey(0)
	#cv2.imshow("d",tmp)
	#cv2.waitKey(0)
	ch = ["*","#","0"]
	img = grayImage
	sp = 20

	width = int(500)
	height = int(400)
	dim = (width, height)
	resized = img
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	if len(a)>100:
		l = 100
	else:
		l = len(a)
	if len(a[0])>80:
		b = 80
	else:
		b = len(a[0])
	
	tmp = cv2.resize(tmp, (l,b), interpolation = cv2.INTER_AREA)
	'''
	o = open("art.txt","w+")
	for i in range(0,len(resized)):
		for j in range(0,len(resized[0])):
			if(resized[i][j]==255):
				o.write(" ")
			else:
				#o.write(ch[int(random.random()*3)])
				o.write("#")

		o.write("\n")
		'''
	ch = ["T","'","o","^"," "," "]
	str = ""
	for i in range(0,len(tmp)):
		for j in range(0,len(tmp[0])):
			str+=ch[abs(int((tmp[i][j]-ii)/d))]
			

		str+="\n"
	return str
cam = None
root = Tk()
displayLab = Label(root,textvariable = "dhjycygjjgy")

displayLab.grid(row=40, column=70, sticky=W) # sticky=W aligns Label to left
c = 0
displayLab.pack()
cam = cv2.VideoCapture("/home/tatan/Downloads/y2mate.com - cgi_animated_short_film_hd_spellbound_by_ying_wu_lizzia_xu_cgmeetup_W_B2UZ_ZoxU_360p.mp4")
while(True):
	if(c%3==0):
		a = cam.read()[1]
		s = send(a,0,50)
		print s
	else:
		pass