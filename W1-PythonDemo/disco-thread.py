from tkinter import *
import threading
import time

colors = ["green","red","blue","purple"]
ndx = 0

def buttonClicked(event=None):
	global ndx
	ndx += 1

master = Tk()

master.geometry("800x600")
master.configure(background="black")

b1 = Button(master,text="Click me!")
b1.grid(column=1, row=1)
b1.bind('<Button>', buttonClicked)





def changeColors(event=None):
	global master
	global colors
	global ndx
	while True:
		ndx = ndx % len(colors)
		master.configure(background=colors[ndx])
		#ndx += 1
		
		time.sleep(0.1)
	

thread = threading.Thread(target=changeColors, args=[])
thread.start()

mainloop()