grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
	[4, 0, 7, 0, 0, 0, 2, 0, 8],
	[0, 0, 5, 2, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 9, 8, 1, 0, 0],
	[0, 4, 0, 0, 0, 3, 0, 0, 0],
	[0, 0, 0, 3, 6, 0, 0, 7, 2],
	[0, 7, 0, 0, 0, 0, 0, 0, 3],
	[9, 0, 3, 0, 0, 0, 6, 0, 4]]

print(grid)

rows = {x:[] for x in range(10)}
cols = {x:[] for x in range(10)}
square = {(x,y):[] for x in range(3) for y in range(3)}

def update(num,i,j):
        rows[i].append(num)
        cols[j].append(num)
        square[(i//3 , j//3)].append(num)

for i in range(9):
    for j in range(9):
        if grid[i][j] != 0:
            update(grid[i][j] , i, j)


def valid(num, r,c):
    if num in rows[r] or num in cols[c] or num in square[(r//3 , c//3)]:
        return False
    return True

def emptyPos(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
    return None

def sudoku(grid):
    
    val = emptyPos(grid)

    if not val:
        return True
    
    r,c = val

    for num in range(1,10):
        if valid(num,r,c):
            grid[r][c] = num
            update(grid[r][c], r, c)
            if sudoku(grid):
                return True
            grid[r][c] = 0
            rows[r].remove(num)
            cols[c].remove(num)
            square[(r//3 , c//3)].remove(num)

    return False


sudoku(grid)
print(grid)



