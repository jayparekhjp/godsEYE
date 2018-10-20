from Tkinter import *
from PIL import ImageTk, Image
import os



creds = 'tempadmin.temp'

def getAdminName():
    with open(creds) as f:
        data = f.readlines() 
        n = data[0].rstrip()
        return n

def getAdminUsername():
    with open(creds) as f:
        data = f.readlines() 
        u = data[1].rstrip()
        return u

def other():
    other=Tk()
    other.geometry('1300x100')
    other.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
    other.title("GODSEYE--OTHER")
    other.configure(background="#033798")
    otherMessage=Label(other,text="THIS ACTIVITY IS HIGHLY CONFIGURABLE AND CAN BE ADDED AS PER COMPANY REQUIREMENTS.",bg="#033798",fg="#FFFFFF")
    otherMessage.config(font=("Helvetica",15))
    otherMessage.pack(fill=BOTH)
    otherCloseButton=Button(other,text="Close",bg="#F6006B",fg="#FFF8FA",command=other.destroy,height = 1, width = 10,borderwidth=0)
    otherCloseButton.config(font=("Helvetica 15 bold"))
    otherCloseButton.place(x=600,y=60)
    other.mainloop()

def retrainDatabase():
    os.system('2_trainer.py')

def manageAdminDatabase():
    execfile("GUImanageAdminDatabase.py")

def addFace():
    os.system('1_dataset_creator.py')

def checkStatus():
    os.system('3_detector.py')

def back():
    root.destroy()
    os.system('AdminLogin_sqlite3_tempAdmin.py')


#main window
root=Tk()
root.title("GODSEYE\\"+getAdminUsername())
#root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
root.configure(background="#033798")

#title frame
#titleFrame=Frame(root, background="#033798")
#titleFrame.config(height=150,width=1400)
#titleFrame.place(x=0,y=0)

#title
title=Label(root,text="GODSEYE",bg="#033798",fg="#FFFFFF")
title.config(font=("Helvetica 50 bold"))
title.place(x=50, y=40)

#image
#img = ImageTk.PhotoImage(Image.open("png4.png"))
#img.configure(background="#033798")
#panel = Label(root, image = img,bg="#033798")
#panel.place(x=400,y=55)

#secondary title
pageName=Label(root,text="Admin Access",bg="#033798",fg="#A3B4D7")
pageName.config(font=("Helvetica 25 bold"))
pageName.place(x=1100, y=70)

#welcome
welcome=Label(root,text="Welcome",bg="#033798",fg="#0188CE")
welcome.config(font=("Helvetica 20"))
welcome.place(x=60,y=175)
adminName=Label(root,text=getAdminName(),bg="#033798",fg="#FFFFFF")
adminName.config(font=("Helvetica 20 bold"))
adminName.place(x=70,y=220)

#button grid

#add face
addFace=Button(root,text="Add Face",bg="#00B6F5",fg="#FFF8FA",height=2,width=20,command=addFace,borderwidth=0)
addFace.config(font=("Helvetica 20 bold"))
addFace.place(x=500,y=180)

#retrain
retrain=Button(root,text="Re-train FaceBase",bg="#00B6F5",fg="#FFF8FA",height=2,width=20,command=retrainDatabase,borderwidth=0)
retrain.config(font=("Helvetica 20 bold"))
retrain.place(x=875,y=180)

#manage admin databse
addAdmin=Button(root,text="Manage Admin Database",bg="#00B6F5",fg="#FFF8FA",height=2,width=20,command=manageAdminDatabase,borderwidth=0)
addAdmin.config(font=("Helvetica 20 bold"))
addAdmin.place(x=500,y=300)

#other
other=Button(root,text="Other",bg="#00B6F5",fg="#FFF8FA",height=2,width=20,command=other,borderwidth=0)
other.config(font=("Helvetica 20 bold"))
other.place(x=875,y=300)

#status
status=Button(root,text="GODSEYE Status",bg="#F6006B",fg="#FFF8FA",height=2,width=36,command=checkStatus,borderwidth=0)
status.config(font=("Helvetica 25 bold"))
status.place(x=500,y=420)

#back button
closeButton=Button(root,text="Back",bg="#F6006B",fg="#FFF8FA",command=back,height = 1, width = 10,borderwidth=0)
closeButton.config(font=("Helvetica 15 bold"))
closeButton.place(x=725,y=600)

#close button
closeButton=Button(root,text="Close",bg="#F6006B",fg="#FFF8FA",command=root.destroy,height = 1, width = 10,borderwidth=0)
closeButton.config(font=("Helvetica 15 bold"))
#closeButton.place(x=575,y=600)
closeButton.place(x=875,y=600)


root.mainloop()
