import cv2
import numpy as np
import os

# Playing video from file:
video=raw_input("Enter Video Name:")
cap = cv2.VideoCapture(video+'.mp4')

try:
    if not os.path.exists('dataSet'):
        os.makedirs('dataSet')
except OSError:
    print ('Error: Creating directory of dataSet')
    
userID=raw_input("Enter User ID:")
currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './dataSet/User' + '.'+str(userID)+'.'+str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    
    # To stop duplicate images
    currentFrame += 1
    if currentFrame>100:
        break;

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
