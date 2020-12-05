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

ch = ["*","#","0"]
img = grayImage

# resize image
tmp = cv2.resize(tmp, (125,50), interpolation = cv2.INTER_AREA)

o = open("art.txt","w+")
for i in range(0,len(tmp)):
	for j in range(0,len(tmp[0])):
		if(tmp[i][j]<=ii):
			print('#',end = '')
		elif tmp[i][j]<=ii+d:
			print('0',end = '')
		elif tmp[i][j]<=ii+2*d:
			print('~',end = '')
		elif tmp[i][j]<=ii+3*d:
			print('*',end = '')
		else:
			print(' ',end = '')
	print()
