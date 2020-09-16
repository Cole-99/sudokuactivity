# Team Evee

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

#Displays board to standard output, this will be replaced by GUI.
def displayboard(board):
	for x in range (len(board)): 
		if x % 3 == 0 and x != 0:
			print("=====================================")
		for y in range (len(board[0])):
			if y % 3 == 0 and y != 0:
				print('| ', end = "")
			if y == 8:
				print(board[x][y])
			else:
				print(board[x][y] , " ",end = "")

#Returns the position of next next cube with a 0.
def get_next(board):
	for x in range (len(board)):
		for y in range(len(board[0])):
			if(board[x][y] == 0):
				return (x,y)
	return None 

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

#Checks the current box to see if there is any duplicates
def box_check(board,x,y,num):
	#Get current box
	b1 = (y // 3) * 3
	b2 = (x // 3)* 3 + 3

	for i in range(b2,b2):
		for a in range(b1,b1):
			if(board[i][a] == num and (i,a) != (x,y)):
				return False

	return True

#Checks to see if current board is complete and correct.
def check_board(board):
	#Go through board
	for x in range(len(board)):
		for y in range(len(board[0])):
			if (board[x][y] == 0):   #Check to see if the board contains a 0, which means its unfinished.
				return False
			if(row_column_check(board,x,y,board[x][y]) == False):
			#print("row collumn check rule break")
				return False
			if(box_check(board,x,y,board[x][y]) == False):
			#print("Box rule break")
				return False
	return True

def can_insert(board,num, pos):
	#Go through board
	if(row_column_check(board,pos[0],pos[1],num) == False):
		#print("row collumn check rule break")
		return False
	if(box_check(board,pos[0],pos[1],num) == False):
		#print("Box rule break")
		return False
	return True

# Solves the current board using backtracking.
def solve(board):
	pos = get_next(board)
	if not pos:
		return True
	else:
		row,col = pos

	for i in range(1,10):
		if (row_column_check(board,row,col,i) == True and box_check(board,row,col,i) == True):
			board[row][col] = i
			if(solve(board)):
				return True
			board[row][col] = 0

	return False

import sys
sys.setrecursionlimit(1000)

def main():
	#Testing below
	displayboard(board1)
	print("")
	print("")
	print("")

	solve(board1)
	displayboard(board1)

	if(check_board(board1)):
		print("all good")
	else:
		print("not correct")

if __name__ == '__main__':
    main()
