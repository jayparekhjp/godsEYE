from Tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

theLabel = Label(root, text="WELCOME TO GODSEYE",bg="black",fg="green")
theLabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame, text="Button 1", fg="red")
button2=Button(topFrame, text="Button 2", fg="blue")
button3=Button(topFrame, text="Button 3", fg="green")
button4=Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

label1=Label(root,text="Label1",bg="blue",fg="yellow")
label1.pack(fill=X)
label2=Label(root,text="Label2",bg="yellow",fg="red")
label2.pack(fill=Y)

img = ImageTk.PhotoImage(Image.open("svg1.svg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()
