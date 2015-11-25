import thread,time
from Tkinter import *
from Tkinter import Image
from Cheesboard import ChessBoard
import pygame

class Window:
	
	def __init__(self, board):
		self.board = board

		self.BLACK = (  0,   0,   0)
		self.WHITE = (255, 255, 255)
		self.BROWN = (148, 37, 0)
		self.LGREY = (168, 168, 168)

		pygame.init()
		size = [1200, 800]
		self.screen = pygame.display.set_mode(size)
		self.clock = pygame.time.Clock()

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
					pygame.draw.rect(self.screen, self.LGREY, [x, y, gap, gap])
					pass
				else:
					pygame.draw.rect(self.screen, self.BROWN, [x, y, gap, gap])
				x += gap
			y += gap
			x = 25
			if mod == 0: mod = 1
			else: mod = 0


	def drawPieces(self):
		p = self.board.get_wking()
		self.screen.blit(self.wKingImg, ((p.row*90)+30,(p.col*90)+30))

		p = self.board.get_bking()
		self.screen.blit(self.bKingImg, ((p.row*90)+30,(p.col*90)+30))	


		p = self.board.get_wrook()
		self.screen.blit(self.wRookImg, ((p.row*90)+30,(p.col*90)+30))



	def loadImages(self):
		scaleFactor = 75

		tmpImg = pygame.image.load("bking.gif")
		self.bKingImg = pygame.transform.scale(tmpImg, (scaleFactor,scaleFactor))

		tmpImg = pygame.image.load("wking.gif")
		self.wKingImg = pygame.transform.scale(tmpImg, (scaleFactor,scaleFactor))

		tmpImg = pygame.image.load("wrook.gif")
		self.wRookImg = pygame.transform.scale(tmpImg, (scaleFactor,scaleFactor))

	def gameloop(self):
	    while True:
			for event in pygame.event.get(): # User did something
				if event.type == pygame.QUIT: # If user clicked close
					sys.exit()

			self.clock.tick(1)

			self.screen.fill(self.WHITE)
			self.drawBoard()
			self.drawPieces()

			pygame.display.flip()

			#self.samlpeMove()

if __name__ == '__main__':
		board = ChessBoard.get_random_chessboard() 

		w = Window(board)
