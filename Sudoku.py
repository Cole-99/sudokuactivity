import pygame
import Board
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Sudoku:
	def __init__(self):
		self.clock = pygame.time.Clock()
		self.paused = False
		self.showInfo = False

	def set_paused(self, paused):
		self.paused = paused
		
	def show_info(self):
		self.showInfo = not self.showInfo

	def run(self):
		self.running = True
		
		###Pygame initializations###
		pygame.init()
		screen = pygame.display.get_surface()
		width = screen.get_width()
		height = screen.get_height()
		clock = pygame.time.Clock()
		mousePos = pygame.mouse.get_pos()
		font = pygame.font.SysFont("comicsans", 40)
		
		# Colors
		black = (0, 0, 0)
		red = (255, 0, 0)
		gray = (128, 128, 128)
		
		###Game variables###

		# Mouse positions, for debugging can remove
		points = []
		
		# Board object
		# Input is difficulty
		# I don't think we will have time to implement this
		boardRef = Board.Board(3)
		
		# Board array
		board = boardRef.getBoard()
		#Copying original board
		boardOriginal = copy2DValues(board)
		original = get_original_places(boardOriginal)
		print board
		print "\n\n"
		print boardOriginal

		
		# Box size, will change size of entire drawn board
		boxSize = 50
		
		# Array of pygame.Rect objects
		rectBoard = []
		
		# Input
		hasClicked = False
		selected = False
		selectedRect = None
		keyPressed = 0
		
		# Game loop
		while self.running:
			pressed = pygame.key.get_pressed()
			
			 # Pump GTK messages.
			while Gtk.events_pending():
				Gtk.main_iteration()
			if not self.running:
				break
			
			# Handling input
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.VIDEORESIZE:
					pygame.display.set_mode(event.size, pygame.RESIZABLE)
					width = screen.get_width()
					height = screen.get_height()

				if event.type == pygame.MOUSEMOTION:
					pos = pygame.mouse.get_pos()
					#print pos
					points += [pos]
				if event.type == pygame.MOUSEBUTTONDOWN:
					hasClicked = True
					mousePos = pygame.mouse.get_pos()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						keyPressed = 1
					elif event.key == pygame.K_2:
						keyPressed = 2
					elif event.key == pygame.K_3:
						keyPressed = 3
					elif event.key == pygame.K_4:
						keyPressed = 4
					elif event.key == pygame.K_5:
						keyPressed = 5
					elif event.key == pygame.K_6:
						keyPressed = 6
					elif event.key == pygame.K_7:
						keyPressed = 7
					elif event.key == pygame.K_8:
						keyPressed = 8
					elif event.key == pygame.K_9:
						keyPressed = 9
					elif event.key == pygame.K_r:
						board = copy2DValues(boardOriginal)
						boardRef.setBoard(board)
					elif event.key == pygame.K_q:
						board = copy2DValues(boardRef.getSolution())
		
					
					
			
			
			if not self.paused:
				# Clear board before new drawing
				screen.fill((255, 255, 255))

				# Show info
				if self.showInfo:
					text = font.render("Pressing Q shows the solution.", 1, black)
					text_rect = text.get_rect(center=(width/2, height/4))
					screen.blit(text, text_rect)
					
					text = font.render("Pressing R resets the board.", 1, black)
					text_rect = text.get_rect(center=(width/2, height/4 + 30))
					screen.blit(text, text_rect)
					
				# Draw board
				for y in range (9):
					for x in range(9):
						rect = pygame.Rect(((width/2) - ((boxSize * 5) - (boxSize * x))) + (boxSize / 2), ((height/2) - ((boxSize * 5) - (boxSize * y))) + (boxSize / 2), boxSize, boxSize)
						rectBoard += [rect]
						pygame.draw.rect(screen, gray, rect, 5)
						
						# Filling in boxes with values from board array
						if board[x][y] is not 0:
							if boardRef.can_insert(board[x][y], (x, y)):
								drawValue(screen, rect, board[x][y], font, black)
							else:
								drawValue(screen, rect, board[x][y], font, red)
				
				# Vertical lines
				pygame.draw.line(screen, black, (((width/2) - (boxSize * 2) - 1) + (boxSize / 2), ((height/2) - (boxSize * 5) - 2) + (boxSize / 2)), (((width/2) - (boxSize * 2) - 1) + (boxSize / 2), ((height/2) + (boxSize * 4) + 1) + (boxSize / 2)), 6)
				pygame.draw.line(screen, black, (((width/2) + boxSize - 1) + (boxSize / 2), ((height/2) - (boxSize * 5) - 2) + (boxSize / 2)), (((width/2) + boxSize - 1) + (boxSize / 2), ((height/2) + (boxSize * 4) + 1) + (boxSize / 2)), 6)
				
				# Horizontal lines
				pygame.draw.line(screen, black, (((width/2) - (boxSize * 5) - 2) + (boxSize / 2), ((height/2) - (boxSize * 2) - 1) + (boxSize / 2)), (((width/2) + (boxSize * 4) + 1) + (boxSize / 2), ((height/2) - (boxSize * 2) - 1) + (boxSize / 2)), 6)
				pygame.draw.line(screen, black, (((width/2) - (boxSize * 5) - 2) + (boxSize / 2), ((height/2) + boxSize - 1) + (boxSize / 2)), (((width/2) + (boxSize * 4) + 1) + (boxSize / 2), ((height/2) + boxSize - 1) + (boxSize / 2)), 6)
				
				# Mouse tracking can remove later
				for p in points:
					pygame.draw.circle(screen, (255, 14, 255), p, 10)
					
				# Check if user selected a box in board
				if hasClicked:
					keyPressed = 0
					selectedRect = drawBox(screen, mousePos, rectBoard)
					selected = True
					hasClicked = False

					# Get the box number that was selected
					for x in range(len(rectBoard)):
						if selectedRect == rectBoard[x]:
							whatBox = x
							break
					#print whatBox

					if keyPressed is not 0 and whatBox not in original:
						tempPos = [(whatBox - (9 * (whatBox // 9))), (whatBox // 9)]
						#if boardRef.can_insert(keyPressed, tempPos):
						board[tempPos[0]][tempPos[1]] = keyPressed
						#else:
							#pygame.draw.rect(screen, (255, 0, 0), selectedRect, 5)
							
				# Update selected box with number that is typed in, ignores 0
				if selected:
					if selectedRect is not None:
						pygame.draw.rect(screen, (12, 14, 84), selectedRect, 5)
						whatBox = 0
						
						# Get the box number that was selected
						for x in range(len(rectBoard)):
							if selectedRect == rectBoard[x]:
								whatBox = x
								break
						#print whatBox

						if keyPressed is not 0 and whatBox not in original:
							tempPos = [(whatBox - (9 * (whatBox // 9))), (whatBox // 9)]
							#if boardRef.can_insert(keyPressed, tempPos):
							board[tempPos[0]][tempPos[1]] = keyPressed
							#else:
								#pygame.draw.rect(screen, (255, 0, 0), selectedRect, 5)
								
								#if board[tempPos[0]][tempPos[1]] != keyPressed:
									#board[tempPos[0]][tempPos[1]] = keyPressed
									
								#drawValue(screen, selectedRect, keyPressed, font, red)
						#drawValue(screen, selectedRect, keyPressed, font)
					else:
						selected = False
					
			
			# update boardRef with board
			boardRef.setBoard(board)
			# reset board for new values
			points = []
			rectBoard = []
			pygame.display.flip()
			self.clock.tick(30)
			
# Returns the box that the newly drawn box collided with
def drawBox(screen, mPos, rectBoard):
	rect = pygame.Rect(mPos[0] - .5, mPos[1] - .5, 1, 1)
	for r in rectBoard:
		if r.contains(rect):
			pygame.draw.rect(screen, (12, 14, 84), r, 5)
			print "collided"
			return r
	pygame.draw.rect(screen, (12, 14, 84), rect, 5)
	
# Draws the typed in value in the box provided
def drawValue(screen, rect, val, font, color):
	text = font.render(str(val), 1, color)
	screen.blit(text, ((rect.center[0] - 10), (rect.center[1] - 10)))

# Returns a list of the box # an original number was in
# An original number is defined as a number that was given initially with the Sudoku board before any change
def get_original_places(board):
	original_places = []
	count = 0
	for a in range(len(board)):
		for b in range(len(board[0])):
			if board[b][a] != 0:
				original_places.append((count))
			count = count + 1
	return original_places


def copy2DValues(fromA):
	return [[fromA[y][x] for x in range(len(fromA))] for y in range(len(fromA[0]))]
	
def main ():
	pygame.init()
	pygame.display.set_mode((0,0), pygame.RESIZABLE)
	game = Sudoku()
	game.run()

if __name__ == '__main__':
    main()
