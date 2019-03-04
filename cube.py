#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
# from matplotlib import pyplot as plt
img = np.zeros((550,550,3),np.uint8)#生成一个空图像,用0填充 dtype数据类型=8bitunsigned

# 空间透视下立方体的边并不一定平行,因此直接用line画比较方便
# cv2.rectangle(img,(256,256),(411,411),(100,100,255),2)#cv::rectangle (InputOutputArray img, Point pt1, Point pt2, const Scalar &color, int thickness=1, int lineType=LINE_8, int shift=0)
# font = cv2.FONT_HERSHEY_SIMPLEX 
# cv2.putText(img, '邓爽', (50, 50), 
#             font, 0.8, (100,100,255), 2, cv2.LINE_AA) 
cv2.line(img,(150,300),(250,300),(100,100,255),2)#AB
cv2.line(img,(250,300),(250,200),(100,100,255),2)#BC
cv2.line(img,(250,200),(150,200),(100,100,255),2)#CD
cv2.line(img,(150,200),(150,300),(100,100,255),2)#DA
cv2.line(img,(150,200),(200,150),(100,100,255),2)#DE
cv2.line(img,(200,150),(300,150),(100,100,255),2)#EF
cv2.line(img,(300,150),(250,200),(100,100,255),2)#FC
cv2.line(img,(300,150),(300,250),(100,100,255),2)#FG
cv2.line(img,(300,250),(250,300),(100,100,255),2)#GB

fmg=cv2.imread("name.jpg",1) # 读取显示在立方体面上的图像 300*300
inpoints=np.float32([(0,0),(300,0),(300,300)]) # 图像上的3个点

# ABCD面仿射
outpoints=np.float32([(0,0),(100,0),(100,100)])# D,C,B,以D为零点
Trans=cv2.getAffineTransform(np.array(inpoints),np.array(outpoints))# 计算仿射变换
cols,rows,channels=fmg.shape # 获取图像尺寸
transimg=cv2.warpAffine(fmg,Trans,(cols,rows))# 旋转已扭曲图像
cols,rows,channels=transimg.shape # 获取旋转后图像的尺寸
mask=img[200:200+rows,150:150+cols] # 在原图上选取对应区域作为ROI-region of interest
mask=cv2.add(mask,transimg) #Put fmg in ROI and modify the main image
img[200:200+rows,150:150+cols]=mask[0:rows,0:cols] # 替换区域

# CDEF面仿射
outpoints=np.float32([(50,0),(150,0),(100,50)])# E,F,C,以(150,150)为零点
Trans=cv2.getAffineTransform(np.array(inpoints),np.array(outpoints))# 计算仿射变换
cols,rows,channels=fmg.shape # 获取图像尺寸
transimg=cv2.warpAffine(fmg,Trans,(cols,rows))# 旋转已扭曲图像
cols,rows,channels=transimg.shape # 获取旋转后图像的尺寸
mask=img[150:150+rows,150:150+cols] # 在原图上选取对应区域作为ROI-region of interest
#print(mask.shape)
mask=cv2.add(mask,transimg) #Put fmg in ROI and modify the main image
img[150:150+rows,150:150+cols]=mask[0:rows,0:cols] # 替换区域

# BCFG面仿射
outpoints=np.float32([(0,50),(50,0),(50,100)])#C,F,G 以(250,150)为零点
Trans=cv2.getAffineTransform(np.array(inpoints),np.array(outpoints))# 计算仿射变换
cols,rows,channels=fmg.shape # 获取图像尺寸
transimg=cv2.warpAffine(fmg,Trans,(cols,rows))# 旋转已扭曲图像
cols,rows,channels=transimg.shape # 获取旋转后图像的尺寸
mask=img[150:150+rows,250:250+cols] # 在原图上选取对应区域作为ROI-region of interest
# print(mask.shape) # 空白图像尺寸设为512 时,由于需要显示的图片尺寸为(300,300),250+300>512导致图像被截,add时尺寸不一致无法相加
mask=cv2.add(mask,transimg) #Put fmg in ROI and modify the main image
img[150:150+rows,250:250+cols]=mask[0:rows,0:cols] # 替换区域


cv2.imshow('cube with name',img)
cv2.waitKey(0) #关闭窗口/键盘ESC退出
cv2.destroyAllWindows() 
# 也可以设置检测用户输入ESC
# while 1:
# 	key=cv2.waitKey(1) #等待键盘输入,间隔1ms
# 	# print key 鼠标需要点一下视频窗口,使程序接收键盘输入而不是命令行接收键盘输入
# 	if key == 27 : #ESC键的ASCII码
# 		print "detect ESC"
# 		cv2.destroyAllWindows() #关闭所有图像窗口