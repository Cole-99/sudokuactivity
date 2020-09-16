import pygame

class Sudoku:
	def __init__(self):
		self.clock = pygame.time.Clock()

	def set_paused(self, paused):
		self.paused = paused
		
	def run(self):
		self.running = True
		pygame.init()
		screen = pygame.display.get_surface()
		width = screen.get_width()
		height = screen.get_height()
		boxSize = 50
		clock = pygame.time.Clock()
		mousePos = pygame.mouse.get_pos()
		points = []
		board = [
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0]
				]	
				
		rectBoard = []
		hasClicked = False
		selected = False
		selectedRect = None
		prevSelectedRect = None
		keyPressed = 0
		font = pygame.font.SysFont("comicsans", 40)
		
		while self.running:
			pressed = pygame.key.get_pressed()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.VIDEORESIZE:
					pygame.display.set_mode(event.size, pygame.RESIZABLE)
					width = screen.get_width()
					height = screen.get_height()

				if event.type == pygame.MOUSEMOTION:
					pos = pygame.mouse.get_pos()
					print pos
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
		
					
					
			
			screen.fill((255, 255, 255))
			
			# Draw board
			for y in range (9):
				for x in range(9):
					rect = pygame.Rect(((width/2) - ((boxSize * 5) - (boxSize * x))), ((height/2) - ((boxSize * 5) - (boxSize * y))), boxSize, boxSize)
					rectBoard += [rect]
					pygame.draw.rect(screen, (255, 14, 255), rect, 5)
					
					if board[x][y] is not 0:
						drawValue(screen, rect, board[x][y], font)
					else:
						drawValue(screen, rect, "", font)
			
			# Vertical lines
			pygame.draw.line(screen, (0, 0, 0), (((width/2) - (boxSize * 2) - 1), ((height/2) - (boxSize * 5) - 2)), (((width/2) - (boxSize * 2) - 1), ((height/2) + (boxSize * 4) + 1)), 6)
			pygame.draw.line(screen, (0, 0, 0), (((width/2) + boxSize - 1), ((height/2) - (boxSize * 5) - 2)), (((width/2) + boxSize - 1), ((height/2) + (boxSize * 4) + 1)), 6)
			
			# Horizontal lines
			pygame.draw.line(screen, (0, 0, 0), (((width/2) - (boxSize * 5) - 2), ((height/2) - (boxSize * 2) - 1)), (((width/2) + (boxSize * 4) + 1), ((height/2) - (boxSize * 2) - 1)), 6)
			pygame.draw.line(screen, (0, 0, 0), (((width/2) - (boxSize * 5) - 2), ((height/2) + boxSize - 1)), (((width/2) + (boxSize * 4) + 1), ((height/2) + boxSize - 1)), 6)
			for p in points:
				pygame.draw.circle(screen, (255, 14, 255), p, 10)
				
			# Check if user selected a box in board
			if hasClicked:
				keyPressed = 0
				selectedRect = drawBox(screen, mousePos, rectBoard)
				selected = True
				hasClicked = False
						
			# Update selected box with number that is typed in, ignores 0
			if selected:
				if selectedRect is not None:
					pygame.draw.rect(screen, (12, 14, 84), selectedRect, 5)
					whatBox = 0
					for x in range(len(rectBoard)):
						if selectedRect == rectBoard[x]:
							whatBox = x
							break
					print whatBox
					
					if keyPressed is not 0:
						board[x - (9 * (x // 9))][x // 9] = keyPressed
					#drawValue(screen, selectedRect, keyPressed, font)
				else:
					selected = False
					

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
def drawValue(screen, rect, val, font):
	text = font.render(str(val), 1, (0,0,0))
	screen.blit(text, ((rect.center[0] - 10), (rect.center[1] - 10)))
	
def main ():
	pygame.init()
	pygame.display.set_mode((0,0), pygame.RESIZABLE)
	game = Sudoku()
	game.run()

if __name__ == '__main__':
    main()
