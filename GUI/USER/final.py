import sqlite3
from Tkinter import *
import random

class Banking:

    def __init__(self,master):
        self.master=master
        master.title("Godseye")
        master.wm_iconbitmap('eye.ico')
        master.configure(background = 'RoyalBlue4')
        
        master.geometry('1280x800+0+0')
        

        fnt=('Calibri Light',30,'bold',)
        self.label1 = Label(master,text='GODSEYE',fg = 'white',bg = 'RoyalBlue4',font=fnt)
        self.label1.place(x=1000,y=50)
        
        self.label2 = Label(master,text='Welcome',fg = 'white',bg = 'RoyalBlue4',font=fnt)
        self.label2.place(x=10,y=50)

        self.balance = Button(master,text='Balance',width = 15,height = 2,activebackground = 'RoyalBlue4',command = self.Balance)
        self.balance.place(x=350,y=260,width=100,height=50)

        self.deposit = Button(master,text='Deposit',width = 15,height = 2,activebackground = 'RoyalBlue4',command = self.Deposit)
        self.deposit.place(x=800,y=260,width=100,height=50)

        self.withdraw = Button(master,text='Withdraw',width = 15,height = 2,activebackground = 'RoyalBlue4',command = self.Withdraw)
        self.withdraw.place(x=350,y=360,width=100,height=50)

        self.setting = Button(master,text='Setting',width = 15,height = 2,activebackground = 'RoyalBlue4',command = self.Setting)
        self.setting.place(x=800,y=360,width=100,height=50)

        self.pin = Button(master,text='Change PIN',width = 15,height = 2,activebackground = 'RoyalBlue4',command = self.PIN)
        self.pin.place(x=350,y=460,width=100,height=50)

        self.help = Button(master,text='Help Guide',width = 15,height = 2,activebackground = 'RoyalBlue4',command = self.Help)
        self.help.place(x=800,y=460,width=100,height=50)

        self.destroy = Button(master,text='Quit',width = 15,height = 2,fg = 'white',bg = 'red',activebackground = 'RoyalBlue4',command=master.destroy)
        self.destroy.place(x=600,y=600,width=100,height=50)


        #self.balance = 10000
        #self.deposit = 500
        #self.withdraw = 400

        self.conn = sqlite3.connect('facebase.db')
        self.c = self.conn.cursor()
        self.c.execute('SELECT * FROM User_Info WHERE acc_no = 54')
        for row in self.c.fetchall():
            self.Name = row [1]

        self.label3 = Label(master,text = str(self.Name),fg = 'white',bg = 'RoyalBlue4',font=fnt)
        self.label3.place(x=10,y=100)
        
    def Balance(self):
        root = Tk()
        root.title("Godseye")
        root.wm_iconbitmap('eye.ico')
        root.configure(background = 'Royalblue4')

        root.geometry('1280x800+0+0')
        fnt=('Calibri Light',30,'bold',)
        label1 = Label(root,text='GODSEYE',fg = 'white',bg = 'RoyalBlue4',font=fnt)
        label1.place(x=1000,y=50)

        
        def read_from_db(self):
            self.c.execute('SELECT * FROM User_Info WHERE acc_no = 54')
            for row in self.c.fetchall():
                self.balance = row [3]
                #print self.balance

        read_from_db(self)
        #self.c.close()
        #self.conn.close()

        label2 = Label(root,text='Your current balance is : '+str(self.balance),fg='red',bg = 'Royalblue4',font=('Calibri Light',20,'bold'))
        label2.place(x=400,y=250)

        
        b1 = Button(root,text='Close',width = 15,height = 2,fg = 'white',bg = 'red',activebackground = 'RoyalBlue4',command=root.destroy)
        b1.place(x=600,y=600,width=100,height=50)
        

        root.mainloop()
        

    def Deposit(self):
        root = Tk()
        root.title("Godseye")
        root.wm_iconbitmap('eye.ico')
        root.configure(background = 'Royalblue4')

        root.geometry('1280x800+0+0')
        fnt=('Calibri Light',30,'bold',)
        label1 = Label(root,text='GODSEYE',fg = 'white',bg = 'RoyalBlue4',font=fnt)
        label1.place(x=1000,y=50)

        label2 = Label(root,text='Deposit amount: ',fg='white',bg = 'Royalblue4',font=('Calibri Light',20,'bold'))
        label2.place(x=400,y=250)

        def read_from_db(self):
            self.c.execute('SELECT * FROM User_Info WHERE acc_no = 54')
            for row in self.c.fetchall():
                self.balance = row [3]
                #print self.balance

        read_from_db(self)
        #self.c.close()
        #self.conn.close()
        
        def Display(event):
            str1=entry1.get()
            deposit = int(str1) + self.balance

            lbl=Label(root,text="Your current balance is: "+str(deposit),fg = 'red',bg = 'RoyalBlue4',font=('Calibri Light',20,'bold'))
            lbl.place(x=450,y=400)
            #print deposit
            conn = sqlite3.connect('facebase.db')
            c = conn.cursor()

            c.execute('UPDATE User_Info SET Balance = ? WHERE acc_no = 54',(deposit,))
            conn.commit()

        entry1 = Entry(root,width=10,fg='black',bg='white',font=('Calibri Light',20,'bold'))
        entry1.place(x=650,y=250)

            
        entry1.bind("<Return>",Display)
        b1 = Button(root,text='Close',width = 15,height = 2,fg = 'white',bg = 'red',activebackground = 'RoyalBlue4',command=root.destroy)
        b1.place(x=600,y=600,width=100,height=50)
        #print deposit
        

    def Withdraw(self):
        root = Tk()
        root.title("Godseye")
        root.wm_iconbitmap('eye.ico')
        root.configure(background = 'Royalblue4')

        root.geometry('1280x800+0+0')
        fnt=('Calibri Light',30,'bold',)
        label1 = Label(root,text='GODSEYE',fg = 'white',bg = 'RoyalBlue4',font=fnt)
        label1.place(x=1000,y=50)

        label2 = Label(root,text='Withdraw amount: ',fg='white',bg = 'Royalblue4',font=('Calibri Light',20,'bold'))
        label2.place(x=400,y=250)
        def read_from_db(self):
            self.c.execute('SELECT * FROM User_Info WHERE acc_no = 54')
            for row in self.c.fetchall():
                self.balance = row [3]
                #print self.balance

        read_from_db(self)
        #self.c.close()
        #self.conn.close()
        
        def Display(event):
            str1=entry1.get()
            deposit = self.balance - int(str1)

            lbl=Label(root,text="Your current balance is: "+str(deposit),fg = 'red',bg = 'RoyalBlue4',font=('Calibri Light',20,'bold'))
            lbl.place(x=450,y=400)
            #print deposit
            conn = sqlite3.connect('facebase.db')
            c = conn.cursor()

            c.execute('UPDATE User_Info SET Balance = ? WHERE acc_no = 54',(deposit,))
            conn.commit()

        entry1 = Entry(root,width=10,fg='black',bg='white',font=('Calibri Light',20,'bold'))
        entry1.place(x=650,y=250)

            
        entry1.bind("<Return>",Display)
        b1 = Button(root,text='Close',width = 15,height = 2,fg = 'white',bg = 'red',activebackground = 'RoyalBlue4',command=root.destroy)
        b1.place(x=600,y=600,width=100,height=50)
        #print deposit

        

        root.mainloop()

    def Setting(self):
        root = Tk()
        root.title("Godseye")
        root.wm_iconbitmap('eye.ico')
        root.configure(background = 'Royalblue4')

        root.geometry('1280x800+0+0')
        fnt=('Calibri Light',30,'bold',)
        label1 = Label(root,text='GODSEYE',fg = 'white',bg = 'RoyalBlue4',font=fnt)
        label1.place(x=1000,y=50)

        
        label2 = Label(root,text='This Feature is yet to be published',fg = 'red',bg = 'Royalblue4',font=('Calibri Light',25,'bold'))
        label2.place(x=350,y=300)
        
        b1 = Button(root,text='Close',width = 15,height = 2,fg = 'white',bg = 'red',activebackground = 'RoyalBlue4',command=root.destroy)
        b1.place(x=600,y=600,width=100,height=50)
        
        root.mainloop()

    def PIN(self):
        root = Tk()
        root.title("Godseye")
        root.wm_iconbitmap('eye.ico')
        root.configure(background = 'Royalblue4')

        root.geometry('1280x800+0+0')
        fnt=('Calibri Light',30,'bold',)
        label1 = Label(root,text='GODSEYE',fg = 'white',bg = 'RoyalBlue4',font=fnt)
        label1.place(x=1000,y=50)

        label2 = Label(root,text='Change Your PIN To: ',fg='white',bg = 'Royalblue4',font=('Calibri Light',20,'bold'))
        label2.place(x=350,y=250)

        label3 = Label(root,text='(Please put only 4-digit no.)',fg='red',bg = 'Royalblue4',font=('Calibri Light',14,'bold'))
        label3.place(x=810,y=250)
        
        def read_from_db(self):
            self.c.execute('SELECT * FROM User_Info WHERE acc_no = 54')
            for row in self.c.fetchall():
                self.balance = row [3]
                #print self.balance

        read_from_db(self)
        #self.c.close()
        #self.conn.close()
        
        def Display(event):
            PIN=entry1.get()
            #deposit = int(str1) + self.balance

            lbl=Label(root,text="Your new PIN is: "+str(PIN),fg = 'red',bg = 'RoyalBlue4',font=('Calibri Light',20,'bold'))
            lbl.place(x=500,y=400)
            #print deposit
            conn = sqlite3.connect('facebase.db')
            c = conn.cursor()

            c.execute('UPDATE User_Info SET PIN = ? WHERE acc_no = 54',(PIN,))
            conn.commit()

        entry1 = Entry(root,width=10,fg='black',bg='white',font=('Calibri Light',20,'bold'))
        entry1.place(x=650,y=250)

            
        entry1.bind("<Return>",Display)
        b1 = Button(root,text='Close',width = 15,height = 2,fg = 'white',bg = 'red',activebackground = 'RoyalBlue4',command=root.destroy)
        b1.place(x=600,y=600,width=100,height=50)
        #print deposit

        

        root.mainloop()

    def Help(self):
        root = Tk()
        root.title("Godseye")
        root.wm_iconbitmap('eye.ico')
        root.configure(background = 'Royalblue4')

        root.geometry('1280x800+0+0')
        fnt=('Calibri Light',30,'bold',)
        label1 = Label(root,text='GODSEYE',fg = 'white',bg = 'RoyalBlue4',font=fnt)
        label1.place(x=1000,y=50)

        label2 = Label(root,text='This Feature is yet to be published',fg = 'red',bg = 'Royalblue4',font=('Calibri Light',25,'bold'))
        label2.place(x=350,y=300)        

        b1 = Button(root,text='Close',width = 15,height = 2,fg = 'white',bg = 'red',activebackground = 'RoyalBlue4',command=root.destroy)
        b1.place(x=600,y=600,width=100,height=50)        

        root.mainloop()


root=Tk()
b=Banking(root)
root.mainloop()



    
