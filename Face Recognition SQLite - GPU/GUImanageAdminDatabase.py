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
        username=uname.get()
        with sqlite3.connect('adminDatabase.db') as adb:
            cursor=adb.cursor()
        findAdmin=("SELECT * FROM adminDatabase WHERE Username=?")
        cursor.execute(findAdmin,[username])

        if cursor.fetchall():
            alreadyExists=Tk()
            alreadyExists.geometry('1300x100')
            alreadyExists.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
            alreadyExists.title("GODSEYE--USERNAME TAKEN")
            alreadyExists.configure(background="#033798")
            alreadyExistsMessage=Label(alreadyExists,text="OOPS! USERNAME ALREADY TAKEN!",bg="red",fg="yellow")
            alreadyExistsMessage.config(font=("Helvetica",30))
            alreadyExistsMessage.pack(fill=BOTH)
            alreadyExistsCloseButton=Button(alreadyExists,text="Close",bg="#F6006B",fg="#FFF8FA",command=alreadyExists.destroy,height = 1, width = 10,borderwidth=0)
            alreadyExistsCloseButton.config(font=("Helvetica 15 bold"))
            alreadyExistsCloseButton.place(x=600,y=60)
            alreadyExists.mainloop()
        else:
            found=1
    name=n.get()
    username=uname.get()
    password=pword.get()
    passwordR=pwordR.get()
    if password=="":
        nullPassword=Tk()
        nullPassword.geometry('1300x100')
        nullPassword.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
        nullPassword.title("GODSEYE--PASSWORD NOT ENTERED")
        nullPassword.configure(background="#033798")
        nullPasswordMessage=Label(nullPassword,text="OOPS! EMPTY PASSWORD WON'T WORK!",bg="red",fg="yellow")
        nullPasswordMessage.config(font=("Helvetica",30))
        nullPasswordMessage.pack(fill=BOTH)
        nullPasswordCloseButton=Button(nullPassword,text="Close",bg="#F6006B",fg="#FFF8FA",command=nullPassword.destroy,height = 1, width = 10,borderwidth=0)
        nullPasswordCloseButton.config(font=("Helvetica 15 bold"))
        nullPasswordCloseButton.place(x=600,y=60)
        nullPassword.mainloop()
    if name=="":
        nullName=Tk()
        nullName.geometry('1300x100')
        nullName.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
        nullName.title("GODSEYE--NAME NOT ENTERED")
        nullName.configure(background="#033798")
        nullNameMessage=Label(nullName,text="OOPS! YOU FORGOT TO ENTER NAME!",bg="red",fg="yellow")
        nullNameMessage.config(font=("Helvetica",30))
        nullNameMessage.pack(fill=BOTH)
        nullNameCloseButton=Button(nullName,text="Close",bg="#F6006B",fg="#FFF8FA",command=nullName.destroy,height = 1, width = 10,borderwidth=0)
        nullNameCloseButton.config(font=("Helvetica 15 bold"))
        nullNameCloseButton.place(x=600,y=60)
        nullName.mainloop()
    if password!=passwordR:
        noMatch=Tk()
        noMatch.geometry('1300x100')
        noMatch.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
        noMatch.title("GODSEYE--PASSWORD NOT MATCHED")
        noMatch.configure(background="#033798")
        noMatchMessage=Label(noMatch,text="OOPS!ENTER SAME PASSWORD BOTH TIMES!",bg="red",fg="yellow")
        noMatchMessage.config(font=("Helvetica",30))
        noMatchMessage.pack(fill=BOTH)
        noMatchCloseButton=Button(noMatch,text="Close",bg="#F6006B",fg="#FFF8FA",command=noMatch.destroy,height = 1, width = 10,borderwidth=0)
        noMatchCloseButton.config(font=("Helvetica 15 bold"))
        noMatchCloseButton.place(x=600,y=60)
        noMatch.mainloop()
    insertData=("INSERT INTO adminDatabase(Username,Password,Name) VALUES(?,?,?)")
    cursor.execute(insertData,[(username),(password),(name)])
    adb.commit()
    adminAdded=Tk()
    adminAdded.geometry('1300x100')
    adminAdded.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
    adminAdded.title("GODSEYE--WELCOME TO GODSEYE")
    adminAdded.configure(background="#033798")
    adminAddedMessage=Label(adminAdded,text="YIPPIE! NEW ADMIN ADDED, WELCOME TO GODSEYE!",bg="red",fg="yellow")
    adminAddedMessage.config(font=("Helvetica",30))
    adminAddedMessage.pack(fill=BOTH)
    adminAddedCloseButton=Button(adminAdded,text="Close",bg="#F6006B",fg="#FFF8FA",command=adminAdded.destroy,height = 1, width = 10,borderwidth=0)
    adminAddedCloseButton.config(font=("Helvetica 15 bold"))
    adminAddedCloseButton.place(x=600,y=60)
    adminAdded.mainloop()
    
    
    
    
            
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
passwordR=Label(root,text="Re-enter Password:",bg="#033798",fg="#FFFFFF")
passwordR.config(font=("Helvetica 25 bold"))
passwordR.place(x=365,y=370)

#empty frames for entry
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=170)
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=240)
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=310)
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=380)

#admin entry
n=Entry(root,width=25,borderwidth=0)
n.place(x=685,y=170)
uname=Entry(root,width=25,borderwidth=0)
uname.place(x=685,y=240)
pword=Entry(root,show="*",width=25,borderwidth=0)
pword.place(x=685,y=310)
pwordR=Entry(root,show="*",width=25,borderwidth=0)
pwordR.place(x=685,y=380)

#add admin
addAdmin=Button(root,text="Add Admin",bg="#00B6F5",fg="#FFF8FA",height=1,width=20,command=addAdmin,borderwidth=0)
addAdmin.config(font=("Helvetica 20 bold"))
#addAdmin.place(x=500,y=180)
addAdmin.place(x=510,y=440)

#delete admin
#deleteAdmin=Button(root,text="Delete Admin",bg="#00B6F5",fg="#FFF8FA",height=1,width=20,command=deleteAdmin,borderwidth=0)
#deleteAdmin.config(font=("Helvetica 20 bold"))
#deleteAdmin.place(x=500,y=300)
#deleteAdmin.place(x=510,y=475)

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
