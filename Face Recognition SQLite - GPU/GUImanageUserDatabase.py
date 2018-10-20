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
pageName=Label(root,text="Manage User Database",bg="#033798",fg="#A3B4D7")
pageName.config(font=("Helvetica 25 bold"))
pageName.place(x=900, y=70)

root.mainloop()
