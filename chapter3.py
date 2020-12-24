'''
Chapter:3 (Resizing and Cropping)
'''
import cv2

img = cv2.imread('resources/ye.png')
print(img.shape)

# Resizing an Image
ImgResize = cv2.resize(img,(100,200)) # first define imatge , then (width,height)
ImgStretched = cv2.resize(img,(1200,800))

# Cropping an Image
# as images are itself an array or a matrix of pixels
# so we can deal it simply as deaaling with an array to get a specific part of an image
CroppedImage = img[:200,100:300] # here The height comes first and then the width

cv2.imshow('Window',img)
cv2.imshow('Resized',ImgResize)
cv2.imshow('StretcedImage',ImgStretched)
cv2.imshow('CroppedImage',CroppedImage)
cv2.waitKey(0)
