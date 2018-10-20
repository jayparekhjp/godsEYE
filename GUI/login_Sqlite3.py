import sqlite3
from Tkinter import *


root=Tk()
root.geometry('500x200')
root.title("GODSEYE")
root.iconbitmap()

def login(event):
    print("login")
    for i in range(3):
        username=entryName.get()
        password=entryPassword.get()
        with sqlite3.connect('adminDatabase.db') as adb:
            cursor=adb.cursor()
        find_user=("SELECT * FROM adminDatabase WHERE Username=? AND Password=?")
        cursor.execute(find_user,[(username),(password)])
        results=cursor.fetchall()

        if results:
            for i in results:
                print("Welcome  "+i[2])
            return("exit")

        else:
            print("Username or Password INVALID")
            
        
    
#title
title=Label(root,text="WELCOME TO GODSEYE",bg="black",fg="green")
title.grid(columnspan=3)

#login or signup 
loginName=Label(root,text="Username:")
loginPassword=Label(root,text="Password:")
loginName.grid(row=1,sticky=E)
loginPassword.grid(row=2,sticky=E)

entryName=Entry(root)
entryPassword=Entry(root,show="*")
entryName.grid(row=1,column=1)
entryPassword.grid(row=2,column=1)

#login button
loginButton=Button(root,text="Log In",fg="red")
loginButton.bind("<Button-1>",login)
loginButton.grid(row=3,column=1)

#signup button
#signupButton=Button(root,text="Sign Up",fg="red")
#signupButton.bind("<Button-1>",signup)
#signupButton.grid(row=3,column=1)


root.mainloop()
