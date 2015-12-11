import thread,time
from Tkinter import *
from Tkinter import Image
from Cheesboard import ChessBoard
from Pieces import King,Rook, Piece
import pygame

class Window:
	
	def __init__(self, board):
		self.board = board

		self.BLACK = (  0,   0,   0)
		self.WHITE = (255, 255, 255)
		self.BROWN = (128, 64, 0)
		self.LGREY = (168, 168, 168)
		self.YELLOW = (255, 215, 97)

		self.isHighLighted = False
		self.mouse = None
		self.piece = None

		pygame.init()
		size = [1200, 800]
		self.screen = pygame.display.set_mode(size)
		self.clock = pygame.time.Clock()
		self.myfont = pygame.font.SysFont("monospace", 15)

		self.loadImages()
		self.gameloop()

		self.pygame.quit()


	def create_label(self,window):
		self.console = Label(textvariable=self.console_str, bg = '#00ff00',width= 50) 
		self.console.place(x=800,y=100) 

	def drawBoard(self,):
		x = 25
		y = 25
		gap = 90
		mod = 0

		#CREATE BLOCKS
		for i in range(8):
			for j in range(8):
				if j % 2 == mod:
					pygame.draw.rect(self.screen, self.YELLOW, [x, y, gap, gap])
				else:
					pygame.draw.rect(self.screen, self.BROWN, [x, y, gap, gap])
				x += gap
			y += gap
			x = 25
			if mod == 0: mod = 1
			else: mod = 0

		if self.isHighLighted:
			pygame.draw.rect(self.screen, pygame.Color(255, 0, 255, 20), [(self.mouse[0]*90)+25, (self.mouse[1]*90)+25, gap, gap])


	def drawPieces(self):
		p = self.board.get_w_king()
                print p
                if p is not None:
                    self.screen.blit(self.wKingImg, ((p.row*90)+30,(p.col*90)+30))

                p = self.board.get_b_king()
                if p is not None:
                    self.screen.blit(self.bKingImg, ((p.row*90)+30,(p.col*90)+30))	


		p = self.board.get_w_rook()
                if p is not None:
                    self.screen.blit(self.wRookImg, ((p.row*90)+30,(p.col*90)+30))



	def loadImages(self):
		scaleFactor = 75

		tmpImg = pygame.image.load("bking.gif")
		self.bKingImg = pygame.transform.scale(tmpImg, (scaleFactor,scaleFactor))

		tmpImg = pygame.image.load("wking.gif")
		self.wKingImg = pygame.transform.scale(tmpImg, (scaleFactor,scaleFactor))

		tmpImg = pygame.image.load("wrook.gif")
		self.wRookImg = pygame.transform.scale(tmpImg, (scaleFactor,scaleFactor))


	def drawText(self):
		# render text
		for i in range(8):
			y = 10
			x = (i*90)+65
			self.screen.blit(self.myfont.render(str(i), 1, (0,0,0)), (x, y))

		for i in range(8):
			y = (i*90)+65
			x = 10
			self.screen.blit(self.myfont.render(str(i), 1, (0,0,0)), (x, y))


	def gameloop(self):
	    while True:
			for event in pygame.event.get(): # User did something
				if event.type == pygame.QUIT: # If user clicked close
					pygame.quit()
					quit()
				if event.type == pygame.MOUSEBUTTONDOWN:

					if event.button == 1:
						mousePos = pygame.mouse.get_pos()
						col = ((mousePos[1]-25)/90) 
						row = ((mousePos[0]-25)/90) 
						
						if self.isHighLighted:
							mousePos = pygame.mouse.get_pos()
							col = ((mousePos[1]-25)/90) 
							row = ((mousePos[0]-25)/90)
							print self.board.play_move(row, col,self.piece)

							self.piece = None
							self.isHighLighted = False
						else:
							for p in self.board.pieces:
								if p.row == row and p.col == col:
									self.isHighLighted = True
									self.mouse = (row,col)
									self.piece = p
									break

						


			self.clock.tick(60)

			self.screen.fill(self.WHITE)
			self.drawBoard()
			self.drawPieces()
			self.drawText()

			pygame.display.flip()

if __name__ == '__main__':
        board = ChessBoard(wk=King(0,0,Piece.WHITE) , wr=Rook(0,1,Piece.WHITE) , bk=King(1,2,Piece.BLACK) ) 
        board.draw()
        w = Window(board)
