#encoding: utf-8

from Tkinter import *
import sys
import os
import tkMessageBox
import time
import os.path


def man():
	tkMessageBox.showinfo('Man', '^C - Count total n lines\n^S - Save\n^X - Exit')

def save(event):
	file = text.get("1.0",END)
	nfile = open(name, 'w')
	nfile.write(file)
	nfile.close()
	menubar.add_cascade(label='Saved')
#	tkMessageBox.showinfo('info', 'Saved !')


def count_lines():
	file = text.get('1.0', END)
	number = 0
	tmp = open('tmp', 'w')
	tmp.write(file)
	tmp.close()
        tmp = open('tmp', 'r')

	for i in tmp.readlines():
		number += 1

	tmp.close()
	os.remove('tmp')
	tkMessageBox.showinfo("Total linenumbers", number)


global name, Text, stop, menubar
try:
	name = sys.argv[1]
except:
	id = 0
	while True:
		if os.path.isfile("New_file"+str(id)):
			id += 1
		else:
			name = "New_file"+str(id)
			break


saved = False
stop = False



def on_return(event):
    # -2c (-2chars) to skip `Return`

	text.tag_add("print", 'end-2c linestart', 'end-2c')
	text.tag_add("def", 'insert-2c wordstart', 'end-2c')
	text.tag_add("while", 'end-2c linestart', 'end-2c')
	text.tag_add("for", 'insert-2c wordstart', 'end-2c')
	text.tag_add("None", 'end-2c linestart', 'end-2c')
	text.tag_add("class", 'insert-2c wordstart', 'end-2c')
	text.tag_add("Return", 'end-2c linestart', 'end-2c')
	text.tag_add("try", 'insert-2c wordstart', 'end-2c')
	text.tag_add("except", 'end-2c linestart', 'end-2c')
	text.tag_add("if", 'insert-2c wordstart', 'end-2c')
	text.tag_add("else", 'end-2c linestart', 'end-2c')
	text.tag_add("elif",'insert-2c wordstart', 'end-2c')


mdit = Tk()
mdit.title(name)
text = Text(mdit)

text.tag_configure("print", foreground="deep sky blue")
text.tag_configure("def", foreground="deep sky blue")
text.tag_configure("while", foreground="deep sky blue")
text.tag_configure("for", foreground="deep sky blue")
text.tag_configure("None", foreground="pink")
text.tag_configure("class", foreground="deep sky blue")
text.tag_configure("Return", foreground="red")
text.tag_configure("try", foreground="deep sky blue")
text.tag_configure("except", foreground="deep sky blue")
text.tag_configure("if", foreground="deep sky blue")
text.tag_configure("else", foreground="deep sky blue")
text.tag_configure("elif", foreground="deep sky blue")


def quit(event):
	mdit.destroy()
	exit(0)

mdit.bind('<Control-s>', save)
mdit.bind('<Control-x>', quit)
mdit.bind('<Control-c>', count_lines)


try:
	filename = open(name, 'r')
	text.insert(INSERT, filename.read())
except:
	None

text.config(bg='black', fg='white', width=200, height=400, insertbackground='white')
text.pack()

menubar = Menu(mdit)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Help", command=man)
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=filemenu)
mdit.config(menu=menubar, bg='black')

mdit.mainloop()

