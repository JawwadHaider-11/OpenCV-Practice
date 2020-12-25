'''
Chapter:5 (Warp Perspective)
'''
import cv2
import numpy as np
img = cv2.imread('resources/card2.jpg')
width, height = 250,350

pts1 = np.float32([[71,15],[113,13],[106,65],[151,52]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
warp = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('Warp',warp)

cv2.imshow('Original',img)
# print(img.shape)
cv2.waitKey(0)