import cv2

print(cv2.__version__)

img  = cv2.imread('./img.jpg' , 0) # 0 for gray scale
                                   # 1 for color 

print(img)

cv2.imshow('first',img)
k = cv2.waitKey(0)   # cv2.waitKey(5000) >>>> mean 5 sec

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('img_form_opencv.jpg' , img)
    cv2.destroyAllWindows()
