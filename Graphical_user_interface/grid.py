from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Shyam Singh")
#showing it onto the screen
# myLabel1.pack()
# myLabel2.pack()

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()