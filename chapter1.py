import cv2

# print('Package imported')

# img = cv2.imread('resources/ye.png')

# cv2.imshow('output',img)
# cv2.waitKey(0)
'''
this will add an infinte delay so that we can view our image,
any number here represents the no of milisecond we wanted the delay
'''
'''
video
'''
# cap = cv2.VideoCapture('resources/video.mp4')
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('video',img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
'''
Webcam
'''
cap = cv2.VideoCapture(0)
cap.set(3,640) #width ID 3
cap.set(4,400) #height ID 4
cap.set(10,100) #brightness ID 10

while True:
    success, img = cap.read()
    cv2.imshow('output',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break