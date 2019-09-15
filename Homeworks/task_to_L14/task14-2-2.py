#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataset import Dataset
from task6_module import run
from tkinter import Tk, Label, Button, Entry, Canvas, Frame, TOP,\
 LEFT, RIGHT, YES, BOTH, X, N, StringVar, END
from tkinter import messagebox as mb


class DrawData:
	def __init__(self):
		self.root = Tk()
		self.make_canvas()
		self.root.mainloop()	

	def make_geometry(self):
		self.root.geometry('480x80+300+200')

	def make_canvas(self, relation = None):
		relation = self.root if relation is None else relation
		Canvas(relation, width=500, height=500, bg="lightblue", cursor="pencil").pack()



class MyFirstApp:
	def __init__(self):
		self.root = Tk()
		self.var = StringVar()
		self.make_geometry()
		self.make_buttons()
		self.root.mainloop()

	def make_geometry(self):
		self.root.geometry('480x120+300+200')

	def make_buttons(self):
		# Title
		Label(self.root, text='Showing information from experiment').pack()
		# frame with input text
		frame_of_entering_text = Frame(self.root, bg = 'blue')
		frame_of_entering_text.pack(side=TOP, fill=X)
		Label(frame_of_entering_text, text='Enter name of file').pack(side=LEFT, anchor=N)
		# text processing
		self.filename_entry = Entry(frame_of_entering_text,  textvariable = self.var)
		self.filename_entry.pack(side=LEFT, fill=BOTH, expand=YES)
		# initialization of buttons
		run_btn = Button(frame_of_entering_text, text='Run', command=self.run)
		draw_btn = Button(self.root, text='Draw', command=self.draw)
		quit_btn = Button(self.root, text='Quit', command=self.root.destroy)
		# show buttons
		run_btn.pack(side=RIGHT, anchor=N)
		draw_btn.pack()
		quit_btn.pack()

	def run(self):
		filename = self.var.get()
		try:
			self.data = Dataset(filename)
			d = run(*self.data.get())
			print(d)

		except FileNotFoundError:
			mb.showerror("ERROR!", "File {} not found, pleas try again".format(filename))
			self.filename_entry.delete(0, END)

	def draw(self):
		...
		DrawData()
	

if __name__ == '__main__':
	MyFirstApp()

