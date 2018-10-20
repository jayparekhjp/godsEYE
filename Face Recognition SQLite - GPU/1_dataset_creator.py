import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);

def insrtOrUpdate(id,name,acc_num):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT*FROM Users WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE Users SET Name=' "+str(name)+" ' WHERE ID="+str(id)
        cmd="UPDATE Users SET Account_Number=' "+str(acc_num)+" ' WHERE ID="+str(id)
    else:
        cmd="INSERT INTO Users(ID,Name,Account_Number) Values("+str(id)+",' "+str(name)+" ',' "+str(acc_num)+" ' )"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id=raw_input('Enter User ID:')
name=raw_input('Enter User Name:')
acc_num=raw_input('Enter User Account Number:')
insrtOrUpdate(id,name,acc_num)
sampleNum=0;
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/User."+id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>25):
        break;
cam.release()
cv2.destroyAllWindows()
