import cv2 as cv
import numpy as np

def nothing(x):
    print(x)
    
cv.namedWindow('detecting' , cv.WINDOW_AUTOSIZE)

cap = cv.VideoCapture(0)

#Lower values tracker
cv.createTrackbar('Lh', 'detecting', 0, 255, nothing)
cv.createTrackbar('Ls', 'detecting', 0, 255, nothing)
cv.createTrackbar('Lv', 'detecting', 0, 255, nothing)

#Upper values tracker
cv.createTrackbar('Uh', 'detecting', 255, 255, nothing)
cv.createTrackbar('Us', 'detecting', 255, 255, nothing)
cv.createTrackbar('Uv', 'detecting', 255, 255, nothing)

while True:
    # Read img
    # img = cv.imread('smarties.png')
    
    #Read Video
    _ , frame = cap.read()
    
    # Convert img from BGR to HSV
    hsv = cv.cvtColor(frame , cv.COLOR_BGR2HSV)
    
    #Get trackbar values for lower and upper
    Lh = cv.getTrackbarPos('Lh' , 'detecting')
    Ls = cv.getTrackbarPos('Ls' , 'detecting')
    Lv = cv.getTrackbarPos('Lv' , 'detecting')

    Uh = cv.getTrackbarPos('Uh' , 'detecting')
    Us = cv.getTrackbarPos('Us' , 'detecting')
    Uv = cv.getTrackbarPos('Uv' , 'detecting')
    
    lower_values = np.array([Lh , Ls , Lv])
    upper_values = np.array([Uh , Us , Uv])
    
    mask = cv.inRange(hsv ,lower_values,upper_values)
    
    res = cv.bitwise_and(frame , frame , mask=mask)
    
    cv.imshow('detecting the ball' , frame)
    
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    
    k=cv.waitKey(1)
    if k==27:
        break
# if you run code with video    
cap.release()

cv.destroyAllWindows()