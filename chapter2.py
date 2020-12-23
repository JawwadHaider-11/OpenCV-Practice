import cv2
# print('Package imported')
import numpy as np

img = cv2.imread('resources/ye.png')
kernel = np.ones((5,5),np.uint8)
'''
Below we are covering some basic functions that can be done on an image
'''
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurImage = cv2.GaussianBlur(grayImage,(7,7),0)
cannyImage = cv2.Canny(img,100,100)
dilatedImage = cv2.dilate(cannyImage,kernel)
erodedImage = cv2.erode(dilatedImage,kernel)

# cv2.imshow('GrayImage',grayImage)
# cv2.imshow('BlurImage',blurImage)
cv2.imshow('CannyImage',cannyImage)
cv2.imshow('DilatedImage',dilatedImage)
cv2.imshow('ErodedImage',erodedImage)

cv2.waitKey(0)

