'''
Chapter:6 (Joining Images)
'''
import cv2
import numpy as np

img = cv2.imread("resources/card2.jpg")
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))
# def stackImages(scale,matrix):

cv2.imshow('Image',img)
cv2.imshow('Horizontal',imgHor)
cv2.imshow('Vertical',imgVer)



cv2.waitKey(0)