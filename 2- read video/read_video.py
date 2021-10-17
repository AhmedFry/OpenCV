import cv2


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # read form my camera 
                            # 'video.mp4' read from stored videos
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # for resoluation
out = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640,480)) # (filename , fourcc , frames per sec , size)

print('video is open :' , cap.isOpened())

# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#set width and height

cap.set(3 , 720) # width
cap.set(4 , 720) # height

while (cap.isOpened()):
    rat , frame = cap.read()
    if rat == True:
        out.write(frame)
        
        font = cv2.FONT_HERSHEY_DUPLEX
        text = 'First code in openCV'
        frame = cv2.putText(frame, text ,(20 , 50 ) , font , 1 , (0,255,255) , 5)   
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        
        
        
        cv2.imshow('frame', gray)
        
        
        if cv2.waitKey(1) == ord('q'): 
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()

