

from Tkinter import *
from Tkinter import Image

class Window:
	
	def __init__(self):
		window = Tk()
		window.title("we are awesome")
		window.minsize(width=1200, height=800)
		window.resizable(width=False, height=False)

		self.createCanvas(window);

		
		window.mainloop()


	def createCanvas(self, window):
		c = Canvas(window, width=1200, height=800)
		c.pack()

		x = 25
		y = 25
		gap = 90
		mod = 0

		#VERTICAL LINES
		#c.create_line(x, x, x, 100)
#

		#CREATE BLOCKS
		#c.create_rectangle(x, x, x+gap, x+gap, fill="blue") # x y width height
		for i in range(8):
			for j in range(8):
				if j % 2 == mod:
					c.create_rectangle(x, y, x+gap, y+gap, fill="White")
				else:
					c.create_rectangle(x, y, x+gap, y+gap, fill="Black")
				x += gap
			y += gap
			x = 25
			if mod == 0: mod = 1
			else: mod = 0


		self.loadImages(c)

	def loadImages(self, c):
		self.photo = PhotoImage(file="bking.gif")

		self.photo = self.photo.subsample(6,6)
		c.create_image(25, 25, image=self.photo, anchor="nw", state=NORMAL)			

if __name__ == '__main__':
	w = Window()

