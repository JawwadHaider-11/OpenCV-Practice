'''
Chapter:4 (Adding Shapes and Texts to an image)
'''
import cv2
import numpy as np

# img = np.zeros((512,512)) # this is a gray scale image having only one channel
img = np.zeros((512,512,3),np.uint8)

# img[:40,:40] = 255,0,0 #Coloring
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255, 0, 0),2)
cv2.rectangle(img,(0,0),(100,300),(0,255,0),3)
cv2.circle(img,(400,100),50,(0,0,255),4)

cv2.putText(img,'OPENCV',(255,255),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,220),3)

cv2.imshow('Image',img)
cv2.waitKey(0)