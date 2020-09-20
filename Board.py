# Team Evee
import random
class Board:
	board1 = [
		[0,2,0,6,0,8,0,0,0],
		[5,8,0,0,0,9,7,0,0],
		[0,0,0,0,4,0,0,0,0],
		[3,7,0,0,0,0,5,0,0],
		[6,0,0,0,0,0,0,0,4],
		[0,0,8,0,0,0,0,1,3],
		[0,0,0,0,2,0,0,0,0],
		[0,0,9,8,0,0,0,3,6],
		[0,0,0,3,0,6,0,9,0]
	]

	board2 = [
		[4,1,0,0,7,0,0,0,5],
		[0,8,0,0,0,6,0,9,0],
		[0,0,0,5,0,0,0,0,0],
		[0,0,7,4,0,1,3,0,0],
		[5,3,0,0,0,0,0,1,2],
		[0,0,4,3,0,8,7,0,0],
		[0,0,0,0,0,4,0,0,0],
		[0,9,0,8,0,0,0,7,0],
		[7,0,0,0,6,0,0,2,8]
	]

	board3 = [
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
	
	boardSolution = [
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
	
	board = [
		[5,3,4,6,7,8,9,1,2],
		[6,7,2,1,9,5,3,4,8],
		[1,9,8,3,4,2,5,6,7],
		[8,5,9,7,6,1,4,2,3],
		[4,2,6,8,5,3,7,9,1],
		[7,1,3,9,2,4,8,5,6],
		[9,6,1,5,3,7,2,8,4],
		[2,8,7,4,1,9,6,3,5],
		[3,4,5,2,8,6,1,7,9]
	]
	
	boardCopy = [
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

	# Difficulty (Values to remove)
	# 1 = 10
	# 2 = 20
	# >2 = 30
	def __init__(self, difficulty):
		self.setDifficulty(difficulty)
		
		self.randomBoard()
		print self.board

		#self.solve()
		
	# Returns the board array
	def getBoard(self):
		return self.board
	
	def getSolution(self):
		return self.boardSolution
	
	def setBoard(self, newBoard):
		self.board = newBoard

	def setDifficulty(self, dif):
		if (dif == 1):
			self.difficulty = 10
		elif (dif == 2):
			self.difficulty = 20
		else:
			self.difficulty = 30

	# Shuffles a fully solved board, and makes sure it is solvable before removing an amount of values based on difficulty
	def randomBoard(self):
		random.shuffle(self.board)
		self.solve()
		
		if (not self.check_board()):
			self.randomBoard()
		else:
			self.boardSolution = copy2DValues(self.board)
			while self.difficulty != 0:
				x = random.randint(0,8)
				y = random.randint(0,8)
				if self.board[x][y] != 0:
					self.board[x][y] = 0
					self.difficulty -= 1
				else:
					print self.difficulty
						
			

	#Displays board to standard output, this will be replaced by GUI.
	def displayboard(self):
		for x in range (len(self.board)): 
			if x % 3 == 0 and x != 0:
				print("=====================================")
			for y in range (len(self.board[0])):
				if y % 3 == 0 and y != 0:
					print "not python3"
					#print('| ', end = "")
				if y == 8:
					print(self.board[x][y])
				else:
					print "not python3"
					#print(board[x][y] , " ",end = "")

	def can_insert(self,num, pos):
		#Go through board
		if(row_column_check(self.board, pos[0],pos[1],num) == False):
			#print("row collumn check rule break")
			return False
		if(box_check(self.board, pos[0],pos[1],num) == False):
			#print("Box rule break")
			return False
		return True

	#Checks to see if current board is complete and correct.
	def check_board(self):
		#Go through board
		for x in range(len(self.board)):
			for y in range(len(self.board[0])):
				if (self.board[x][y] == 0):   #Check to see if the board contains a 0, which means its unfinished.
					return False
				if(row_column_check(self.board, x,y,self.board[x][y]) == False):
				#print("row collumn check rule break")
					return False
				if(box_check(self.board, x,y,self.board[x][y]) == False):
				#print("Box rule break")
					return False
		return True
		
	# Solves the current board using backtracking.
	def solve(self):
		pos = get_next(self.board)
		if not pos:
			return True
		else:
			row,col = pos

		for i in range(1,10):
			if (row_column_check(self.board, row,col,i) == True and box_check(self.board, row,col,i) == True):
				self.board[row][col] = i
				if(self.solve()):
					return True
				self.board[row][col] = 0

		return False
	
	# Returns True if entire 2D array only contains 0, False otherwise
	def isEmpty(self):
		for x in range(8):
			for y in range(8):
				if (self.board[x][y] != 0):
					return False
		return True
		
	def isFilled(self):
		for x in range(8):
			for y in range(8):
				if (self.board[x][y] == 0):
					return False
		return True		
		
#Checks the current box to see if there is any duplicates
def box_check(board,x,y,num):
	#Get current box
	b1 = (y // 3) * 3
	b2 = (x // 3)* 3 

	for i in range(b2,b2+3):
		for a in range(b1,b1+3):
			if(board[i][a] == num and (i,a) != (x,y)):
				return False

	return True
	
#Checks the positions row and column to see if there are any duplicates.
def row_column_check(board,x,y,num):

	for i in range (len(board[0])):

		if board[x][i] == num and y != i:
			#print('position',i,y,'   ',board[i][y],num)
			return False

	for i in range (len(board)):
		if board[i][y] == num and x != i:
			return False

	return True
	
#Returns the position of next next cube with a 0.
def get_next(board):
	for x in range (len(board)):
		for y in range(len(board[0])):
			if(board[x][y] == 0):
				return (x,y)
	return None 
	
def copy2DValues(fromA):
	return [[fromA[y][x] for x in range(len(fromA))] for y in range(len(fromA[0]))]
