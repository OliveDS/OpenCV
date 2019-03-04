#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np

#allocating image space color 
frame = np.zeros((500,500,3),np.uint8)

#drawing lines
cv2.line(frame,(150,300),(250,300),(255,0,0),2)#AB
cv2.line(frame,(250,300),(250,200),(255,0,0),2)#BC
cv2.line(frame,(250,200),(150,200),(255,0,0),2)#CD
cv2.line(frame,(150,200),(150,300),(255,0,0),2)#DA
cv2.line(frame,(150,200),(200,150),(255,0,0),2)#DE
cv2.line(frame,(200,150),(300,150),(255,0,0),2)#EF
cv2.line(frame,(300,150),(250,200),(255,0,0),2)#FC
cv2.line(frame,(300,150),(300,250),(255,0,0),2)#FG
cv2.line(frame,(300,250),(250,300),(255,0,0),2)#GB

#read image
fmg=cv2.imread("go.jpg",1)
#resize to tranimg
#set points in source image
inpoints=np.float32([(0,199),(199,199),(0,0)])#a,b,c

#front face
#setting points in transform space
outpoints=np.float32([(0,99),(99,99),(0,0)])
#getting transform matrix
Trans=cv2.getAffineTransform(np.array(inpoints),np.array(outpoints))
cols,rows,channels=fmg.shape
transimg=cv2.warpAffine(fmg,Trans,(cols,rows))
cols,rows,channels=transimg.shape
mask=frame[200:200+rows,150:150+cols]
mask=cv2.add(mask,transimg)
frame[200:200+rows,150:150+cols]=mask[0:rows,0:cols]

#top face
#setting points in transform space
outpoints=np.float32([(0,49),(99,49),(49,0)])
#getting transform matrix
Trans=cv2.getAffineTransform(np.array(inpoints),np.array(outpoints))
cols,rows,channels=fmg.shape
transimg=cv2.warpAffine(fmg,Trans,(cols,rows))
cols,rows,channels = transimg.shape
mask=frame[150:150+rows,150:150+cols]
mask=cv2.add(mask,transimg)
frame[150:150+rows,150:150+cols]=mask[0:rows,0:cols]

#rightt face
#setting points in transform space
outpoints=np.float32([(00,49),(00,149),(49,0)])
#getting transform matrix
Trans=cv2.getAffineTransform(np.array(inpoints),np.array(outpoints))
cols,rows,channels=fmg.shape
transimg=cv2.warpAffine(fmg,Trans,(cols,rows))
cols,rows,channels = transimg.shape
mask=frame[150:150+rows,250:250+cols]
mask=cv2.add(mask,transimg)
frame[150:150+rows,250:250+cols]=mask[0:rows,0:cols]
cv2.imshow('myframe',frame)
while 1:
 key = cv2.waitKey(1)
 if key>0:
   break
cv2.destroyAllWindows()
