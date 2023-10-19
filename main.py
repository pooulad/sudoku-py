Board = 9
def puzzle(a):
	for i in range(Board):
		for j in range(Board):
			print(a[i][j],end = " ")
		print()
def solve(grid, row, col, num):
	for x in range(9):
		if grid[row][x] == num:
			return False
		    
	for x in range(9):
		if grid[x][col] == num:
			return False


	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

def Suduko(grid, row, col):

	if (row == Board - 1 and col == Board):
		return True
	if col == Board:
		row += 1
		col = 0
	if grid[row][col] > 0:
		return Suduko(grid, row, col + 1)
	for num in range(1, Board + 1, 1): 
	
		if solve(grid, row, col, num):
		
			grid[row][col] = num
			if Suduko(grid, row, col + 1):
				return True
		grid[row][col] = 0
	return False

'''0 means the cells where no value is assigned'''
grid = [[0, 0, 4, 3, 0, 0, 1, 6, 0],
        [1, 7, 0, 0, 0, 8, 0, 4, 0],
	[3, 0, 0, 0, 4, 0, 0, 0, 5],
	[0, 3, 0, 1, 0, 9, 0, 0, 4],
	[0, 0, 2, 0, 0, 0, 3, 0, 0],
	[6, 0, 0, 4, 0, 2, 0, 5, 0],
	[2, 0, 0, 0, 5, 0, 0, 0, 1],
	[0, 6, 0, 7, 0, 0, 0, 9, 2],
	[0, 1, 3, 0, 0, 4, 8, 0, 0]]

if (Suduko(grid, 0, 0)):
	puzzle(grid)
else:
	print("ooops *-* Solution does not exist :(")