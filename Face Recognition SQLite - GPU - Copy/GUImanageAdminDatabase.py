import sqlite3
from Tkinter import *
import os


creds = 'tempadmin.temp'


def getAdminUsername():
    print("getAdminUsername CALLED")
    with open(creds) as f:
        data = f.readlines() 
        u = data[1].rstrip()
        return u

def addAdmin():
    found=0
    while found==0:
        sqlusername=uname.get()
        with sqlite3.connect('adminDatabase.db') as adb:
            cursor=adb.cursor()
        findAdmin=("SELECT * FROM adminDatabase WHERE Username=?")
        cursor.execute(findAdmin,[sqlusername])

        if cursor.fetchall():
            alreadyExists=Tk()
            alreadyExists.title("GODSEYE--USERNAME TAKEN")
            alreadyExistsMessage=Label(alreadyExists,text="Username Taken, please try again")
            alreadyExistsMessage.pack()
            alreadyExists.mainloop()

            
def deleteAdmin():
    print("deleteAdmin CALLED")
    username=uname.get()
    password=pword.get()
    name=name.get()
    with sqlite3.connect('adminDatabase.db') as adb:
        cursor=adb.cursor()
    find_user=("SELECT * FROM adminDatabase WHERE Username=? AND Password=?")
    cursor.execute(find_user,[(username),(password)])
    results=cursor.fetchall()
    if results:
        for i in results:
            i[0]=NULL
            i[1]=NULL
            i[2]=NULL
        deleted=Tk()
        deleted.title("GODSEYE--ADMIN ACCOUNT DELETED")
        deleted.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
        deletedMessage=Label(deleted,text="Admin Deleted")
        deletedMessage.pack()
        deleted.mainloop()
    else:
        notFound=Tk()
        notFoundMessage=Label(deleted,text="Admin Doesn't Exist")
        notFound.title("GODSEYE--ADMIN NOT FOUND")
        notFound.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico') 
        notFoundMessage.pack()
        notFound.mainloop()

    

    
def back():
    print("back CALLED")
    root.destroy()
    os.system('adminPage.py')



#main window
root=Tk()
root.title("GODSEYE\\"+getAdminUsername())
#root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
root.configure(background="#033798")

#title
title=Label(root,text="GODSEYE",bg="#033798",fg="#FFFFFF")
title.config(font=("Helvetica 50 bold"))
title.place(x=50, y=40)

#secondary title
pageName=Label(root,text="Manage Admin Database",bg="#033798",fg="#A3B4D7")
pageName.config(font=("Helvetica 25 bold"))
pageName.place(x=900, y=70)

#admin information
name=Label(root,text="Admin Name:",bg="#033798",fg="#FFFFFF")
name.config(font=("Helvetica 25 bold"))
name.place(x=465,y=160)
username=Label(root,text="Username:",bg="#033798",fg="#FFFFFF")
username.config(font=("Helvetica 25 bold"))
username.place(x=505,y=230)
password=Label(root,text="Password:",bg="#033798",fg="#FFFFFF")
password.config(font=("Helvetica 25 bold"))
password.place(x=510,y=300)

#empty frames for entry
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=170)
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=240)
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=310)

#admin entry
name=Entry(root,width=25,borderwidth=0)
name.place(x=685,y=170)
uname=Entry(root,width=25,borderwidth=0)
uname.place(x=685,y=240)
pword=Entry(root,show="*",width=25,borderwidth=0)
pword.place(x=685,y=311)

#add admin
deleteAdmin=Button(root,text="Add Admin",bg="#00B6F5",fg="#FFF8FA",height=1,width=20,command=addAdmin,borderwidth=0)
deleteAdmin.config(font=("Helvetica 20 bold"))
#deleteAdmin.place(x=500,y=180)
deleteAdmin.place(x=510,y=400)

#delete admin
addAdmin=Button(root,text="Delete Admin",bg="#00B6F5",fg="#FFF8FA",height=1,width=20,command=deleteAdmin,borderwidth=0)
addAdmin.config(font=("Helvetica 20 bold"))
#addAdmin.place(x=500,y=300)
addAdmin.place(x=510,y=475)

#back button
closeButton=Button(root,text="Back",bg="#F6006B",fg="#FFF8FA",command=back,height = 1, width = 10,borderwidth=0)
closeButton.config(font=("Helvetica 15 bold"))
closeButton.place(x=540,y=600)

#close button
closeButton=Button(root,text="Close",bg="#F6006B",fg="#FFF8FA",command=root.destroy,height = 1, width = 10,borderwidth=0)
closeButton.config(font=("Helvetica 15 bold"))
#closeButton.place(x=575,y=600)
closeButton.place(x=690,y=600)

root.mainloop()
