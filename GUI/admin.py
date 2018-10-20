from Tkinter import *

creds = 'tempfile.temp'

root=Tk()
root.geometry('1000x500')
root.title("GODSEYE")
root.iconbitmap()

def login(event):
    with open(creds) as f:
        data = f.readlines()
        username = data[0].rstrip() 
        passwordassword = data[1].rstrip() 
 
    if loginName.get() == uname and loginPassword.get() == pword: 
        r = Tk() 
        r.title('Login Status')
        r.geometry('150x50') # Makes the window a certain size
        rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
        rlbl.pack() # Pack is like .grid(), just different
        r.mainloop()
    else:
        r = Tk()
        r.title('Login Status')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()

    
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
