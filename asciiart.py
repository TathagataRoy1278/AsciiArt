import cv2
import random
a = cv2.imread("test.jpg");
ii = int(input())# this defines the minimum threshold of colour after which the desired picture is obtained, which varies from person to person, so tweak it to find
#optimum configuration, generally ranges from [0,150]
d = int(input())#This defines the amount of variance of colour in the picture, A picture with uniform lighting has a low value, while a picture with high contrast value,
#has high value, generally ranges from [20,80]
grayImage = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
tmp = grayImage
grayImage = cv2.threshold(grayImage,ii,255,cv2.THRESH_BINARY)
grayImage = grayImage[1]
cv2.imshow("k",grayImage)

cv2.waitKey(0)
ch = ["*","#","0"]
img = grayImage

# resize image
tmp = cv2.resize(tmp, (200,180), interpolation = cv2.INTER_AREA)

o = open("art.txt","w+")
for i in range(0,len(tmp)):
	for j in range(0,len(tmp[0])):
		if(tmp[i][j]<=ii):
			o.write("#")
		elif tmp[i][j]<=ii+d:
			o.write("0")
		elif tmp[i][j]<=ii+2*d:
			o.write("~")
		elif tmp[i][j]<=ii+3*d:
			o.write("*")
		else:
			o.write(" ")
	
	o.write("\n")
