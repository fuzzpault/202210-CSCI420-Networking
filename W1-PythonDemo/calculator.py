from tkinter import *
import time

expression = ""

def buttonClicked(event=None):
	global l
	global expression
	#print("buttonClicked")
	#print(event.widget.mynumber)
	expression = expression + str(event.widget.mynumber)
	l.config(text = expression)

def evalClicked(event=None):
	global l
	global expression
	expression = str(eval(expression))
	l.config(text = expression)

master = Tk()



keys = []
for i in range(9):
	b1 = Button(master,text=(i+1))
	b1.grid(column= i % 3 , row=int(i / 3))
	b1.bind('<Button>', buttonClicked)
	b1.mynumber = i + 1

b1 = Button(master,text=0)
b1.grid(column= 1 , row=3)
b1.bind('<Button>', buttonClicked)
b1.mynumber = 0

b1 = Button(master,text="+")
b1.grid(column= 0 , row=4)
b1.bind('<Button>', buttonClicked)
b1.mynumber= "+"

b1 = Button(master,text="-")
b1.grid(column= 1 , row=4)
b1.bind('<Button>', buttonClicked)
b1.mynumber= "-"

b1 = Button(master,text="=")
b1.grid(column= 2 , row=4)
b1.bind('<Button>', evalClicked)


l = Label(master, text="nothing here")
l.grid(column = 0, row=5)


mainloop()