# Team Evee
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


	completeboard = [
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

	#TODO start with a random board
	def __init__(self):
		self.board = self.board1
		
	def getBoard(self):
		return self.board

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

	#Returns the position of next next cube with a 0.
	def get_next(self):
		for x in range (len(self.board)):
			for y in range(len(self.board[0])):
				if(self.board[x][y] == 0):
					return (x,y)
		return None 

	def can_insert(self,num, pos):
		#Go through board
		if(self.row_column_check(pos[0],pos[1],num) == False):
			#print("row collumn check rule break")
			return False
		if(self.box_check(pos[0],pos[1],num) == False):
			#print("Box rule break")
			return False
		return True

	#Checks the positions row and column to see if there are any duplicates.
	def row_column_check(self,x,y,num):
		for i in range (len(self.board[0])):
			if self.board[x][i] == num and y != i:
				#print('position',i,y,'   ',board[i][y],num)
				return False

		for i in range (len(self.board)):
			if self.board[i][y] == num and x != i:
				return False

		return True

	#Checks the current box to see if there is any duplicates
	def box_check(self,x,y,num):
		#Get current box
		b1 = (y // 3) * 3
		b2 = (x // 3)* 3 

		for i in range(b2,b2+3):
			for a in range(b1,b1+3):
				if(self.board[i][a] == num and (i,a) != (x,y)):
					return False

		return True

	#Checks to see if current board is complete and correct.
	def check_board(self):
		#Go through board
		for x in range(len(self.board)):
			for y in range(len(self.board[0])):
				if (self.board[x][y] == 0):   #Check to see if the board contains a 0, which means its unfinished.
					return False
				if(self.row_column_check(x,y,self.board[x][y]) == False):
				#print("row collumn check rule break")
					return False
				if(self.box_check(x,y,self.board[x][y]) == False):
				#print("Box rule break")
					return False
		return True

	# Solves the current board using backtracking.
	def solve(self):
		pos = self.get_next(self.board)
		if not pos:
			return True
		else:
			row,col = pos

		for i in range(1,10):
			if (self.row_column_check(row,col,i) == True and self.box_check(row,col,i) == True):
				board[row][col] = i
				if(self.solve(self.board)):
					return True
				self.board[row][col] = 0

		return False
