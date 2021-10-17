import cv2 as cv
import numpy as np


def nothing(x):
    print(x)
    

# Create black img
img = np.zeros((300 , 400 , 3) , np.uint8)
cv.namedWindow('image')

# Create Trackbar 
cv.createTrackbar('B' , 'image' ,0 , 255, nothing )
cv.createTrackbar('G' , 'image' ,0 , 255, nothing )
cv.createTrackbar('R' , 'image' ,0 , 255, nothing )
switch = cv.createTrackbar('SWITCH','image', 0 , 1 , nothing)


while True:
    cv.imshow('image' , img)
    k = cv.waitKey(1)
    if k ==27:
        break
    # Get values in Trackbar
    b = cv.getTrackbarPos('B' , 'image')
    g = cv.getTrackbarPos('G' , 'image')
    r = cv.getTrackbarPos('R' , 'image')
    s = cv.getTrackbarPos('SWITCH' , 'image')
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()