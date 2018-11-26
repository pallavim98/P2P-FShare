import sys
from cl2 import cli
from tkinter import *
from tkinter import messagebox
from server import serve
from tkinter import filedialog

 
def send():

	t = folder_path.get()
	messagebox.showinfo("Information","sending files...")
	serve(t)

def receive():
	t = folder_path.get()
	s = sip.get()
	a = cli(s,t)
	messagebox.showinfo("Information",a)

def browse_button():

    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)


gui = Tk()

sip = StringVar()
gui.geometry('450x250+500+300')
gui.configure(background = "#a1dbcd")
gui.title('FileShare')


L1 = Label(gui, text="Server ip", fg = "#383a39", bg = "#a1dbcd", font = ("Helvetica",16)).pack()
E1 = Entry(gui, bd =5, width = 30, textvariable = sip).pack()


folder_path = StringVar()

button2 = Button(text="Browse", command=browse_button, width = 20, fg = "#a1dbcd", bg="#383a39").pack(expand = True,side=TOP) 


L2 = Label(gui, textvariable=folder_path,fg = "#383a39", bg = "#a1dbcd",font = ("Helvetica",10)).pack()

b1 = Button(gui,text="Send", command = send, fg = "#a1dbcd", bg="#383a39").pack(padx=50,pady=20,expand = True,side = LEFT)
b2 = Button(gui,text="receive", command = receive,fg = "#a1dbcd", bg="#383a39").pack(padx=50,pady=20,expand = True,side = LEFT)


gui.mainloop()