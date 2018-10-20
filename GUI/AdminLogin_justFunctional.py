from Tkinter import *

creds = 'tempfile.temp'

root=Tk()
root.geometry('1000x500')
root.title("GODSEYE")
#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.iconbitmap(r'C:\Users\parek\Desktop\GODSEYE\GODSEYE openCV\GUI\icon1.ico')
root.configure(background="#033798")

def login(event):
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip() 
 
    if entryName.get()== uname and entryPassword.get()== pword: 
        #r = Tk() 
        #r.title(':D')
        #r.geometry('150x50') 
        #rlbl = Label(r, text='\n[+] Logged In') 
        #rlbl.pack()
        #r.mainloop()
        import adminPage
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
        

#title
title=Label(root,text="GODSEYE",bg="#033798",fg="#FFFFFF")
title.grid(column=1,row=5)
#title.config(width=25)
title.config(font=("Helvetica",50))

#login
loginName=Label(root,text="Name:")
entryName=Entry(root)
loginPassword=Label(root,text="Password:")
entryPassword=Entry(root,show="*")
loginButton=Button(root,text="Log In",fg="red")
loginButton.bind("<Button-1>",login)

loginName.grid(row=10,sticky=E)
loginPassword.grid(row=11,sticky=E)
entryName.grid(row=10,column=1)
entryPassword.grid(row=11,column=1)
loginButton.grid(row=13,column=1)

#close button
closeButton=Button(root,text="Close GODSEYE",bg="#F6006B",fg="#FFFFFF",command=root.destroy)
closeButton.grid(row=14,column=3)


root.mainloop()
