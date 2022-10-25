import time
t0= time.time()

suduko =[[0, 0, 0, 0, 3, 1, 0, 0, 0],
        [0, 7, 0, 0, 8, 6, 0, 2, 5],
        [0, 0, 8, 0, 0, 0, 0, 0, 0], 
        [9, 0, 2, 3, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [6, 3, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 5, 0, 0, 3, 7],
        [3, 1, 0, 0, 0, 0, 0, 0, 6],
        [0, 2, 0, 0, 7, 0, 0, 9, 0]]


size = 9

def Suduko(grid, row, col):
    if (row == size - 1 and col == size):
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, size + 1, 1): 
        if SudukoSolver(grid, row, col, num):
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

def Question(a):
    for x in range(size):
        for y in range(size):
            print(a[x][y],end = " ")
        print()

def SudukoSolver(grid, row, col, num):
    srow = row - row % 3
    scol = col - col % 3

    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    for i in range(3):
        for j in range(3):
            if grid[i + srow][j + scol] == num:
                return False
    return True
 
if (Suduko(suduko, 0, 0)):
    print("The Solved Suduko is: \n")
    Question(suduko)
else:
    print("Suduko is not solvable.")


t1 = time.time() - t0
print("Time elapsed: ", t1 ) # CPU seconds elapsed


