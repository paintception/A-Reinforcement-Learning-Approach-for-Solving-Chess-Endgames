import thread,time
from Tkinter import *
from Tkinter import Image
from Cheesboard import ChessBoard

class Window:
	
	def __init__(self,board,window):
                self.board = board
		self.createCanvas(window);
            
                self.console_str = StringVar()
                fr = Frame(window)
	        self.create_label(fr)	


        def create_label(self,window):
            self.console = Label(textvariable=self.console_str, bg = '#00ff00',width= 80) 
            self.console.pack(side = TOP, fill=X) 

	def createCanvas(self, window):
		c = Canvas(window, width=800, height=800)
		c.pack(side = LEFT)

		x = 25
		y = 25
		gap = 90
		mod = 0

		#VERTICAL LINES
		#c.create_line(x, x, x, 100)

		#CREATE BLOCKS
		#c.create_rectangle(x, x, x+gap, x+gap, fill="blue") # x y width height
		for i in range(8):
			for j in range(8):
				if j % 2 == mod:
					c.create_rectangle(x, y, x+gap, y+gap, fill="White")
				else:
					c.create_rectangle(x, y, x+gap, y+gap, fill="Brown")
				x += gap
			y += gap
			x = 25
			if mod == 0: mod = 1
			else: mod = 0


		self.loadImages(c)
                self.draw_board(c)

        def draw_board(self,c):
                p = self.board.get_wking()
		c.create_image((p.row * 90) + 25, 25+(p.col * 90), image=self.wking, anchor="nw", state=NORMAL)			
                p = self.board.get_bking()
		c.create_image((p.row * 90) + 25, 25+(p.col * 90), image=self.bking, anchor="nw", state=NORMAL)			
                p = self.board.get_wrook()
		c.create_image((p.row * 90) + 25, 25+(p.col * 90), image=self.wrook, anchor="nw", state=NORMAL)			

	def loadImages(self, c):
		self.bking = PhotoImage(file="bking.gif")
                self.wking =  PhotoImage(file="wking.gif")
                self.wrook =  PhotoImage(file="wrook.gif")
		self.bking = self.bking.subsample(6,6)
		self.wking = self.wking.subsample(6,6)
		self.wrook = self.wrook.subsample(6,6)

def gameloop(window):
    while True:
        window.console_str.set(str(window.console_str.get())+'\n'+'asdfsdf sdf ')
        time.sleep(0.1)

if __name__ == '__main__':
        board = ChessBoard.get_random_chessboard() 
        window = Tk()
        window.title("we are awesome")
        window.minsize(width=1200, height=800)
        window.resizable(width=False, height=False)
        
	w = Window(board,window)
        thread.start_new_thread(gameloop,(w,))
        window.mainloop()
