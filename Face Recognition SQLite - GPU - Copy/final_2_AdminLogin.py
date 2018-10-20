import sqlite3
from Tkinter import *

creds = 'tempadmin.temp'

def CheckLogin():
    username=uname.get()
    password=pword.get()
    with sqlite3.connect('adminDatabase.db') as adb:
        cursor=adb.cursor()
    find_user=("SELECT * FROM adminDatabase WHERE Username=? AND Password=?")
    cursor.execute(find_user,[(username),(password)])
    results=cursor.fetchall()

    if results:
        for i in results:
            with open(creds, 'w') as f:
                f.write(i[2])
                f.write('\n') 
                f.write(i[0])
                f.close()
        root.destroy()
        import adminPage
        
    else:
        invalid = Tk()
        invalid.title("GODSEYE")
        invalid.geometry('1300x100')
        invalid.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
        invalidMessage = Label(invalid, text='!!! GODSEYE senses INTRUSION !!!',bg="red",fg="yellow")
        invalidMessage.config(font=("Helvetica",30))
        invalidMessage.pack(fill=BOTH)
        invalid.mainloop()


#main window
root=Tk()
root.title("GODSEYE")
#root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
root.configure(background="#033798")

#title
title=Label(root,text="GODSEYE",bg="#033798",fg="#FFFFFF")
title.config(font=("Helvetica 50 bold"))
title.place(x=50, y=40)

#login title
login=Label(root,text="Admin Log In",bg="#033798",fg="#A3B4D7")
login.config(font=("Helvetica 25 bold"))
login.place(x=1100, y=70)

#login information
username=Label(root,text="Username:",bg="#033798",fg="#FFFFFF")
username.config(font=("Helvetica 25 bold"))
#username.place(x=505,y=250)
username.place(x=505,y=230)
password=Label(root,text="Password:",bg="#033798",fg="#FFFFFF")
password.config(font=("Helvetica 25 bold"))
password.place(x=510,y=300)

#empty frames for entry
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=240)
ef1=Frame(root,width=160,height=25,background="#FFFFFF")
ef1.place(x=685,y=310)

#login entry
uname=Entry(root,width=25,borderwidth=0)
uname.place(x=685,y=240)
pword=Entry(root,show="*",width=25,borderwidth=0)
pword.place(x=685,y=311)

#login button
loginButton=Button(root,text="Log In",bg="#F6006B",fg="#FFF8FA",height = 1, width = 20, command=CheckLogin,borderwidth=0)
#loginButton.bind("<Button-1>",login())
loginButton.config(font=("Helvetica 20 bold"))
loginButton.place(x=500,y=400)

#close button
closeButton=Button(root,text="Close GODSEYE",bg="#F6006B",fg="#FFF8FA",command=root.destroy,height = 1, width = 20,borderwidth=0)
closeButton.config(font=("Helvetica 15 bold"))
closeButton.place(x=555,y=600)

root.mainloop()
