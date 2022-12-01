grid = [[0,6,8,0,2,0,0,1,3],
        [3,4,2,9,0,0,6,0,0],
        [1,9,0,6,0,3,0,0,0],
        [4,0,0,0,5,0,8,9,1],
        [0,2,0,0,0,0,3,4,0],
        [0,5,0,3,0,0,0,0,0],
        [7,0,4,5,0,0,0,6,0],
        [6,0,5,1,0,0,4,0,9],
        [0,1,0,0,0,4,5,3,8]]

#print(grid)

#To print the matrix in a 3x3 form
import numpy as np
print(np.matrix(grid))
print("\n")

#funtion which determines whether 
#we can put a number on a certain position
def possible(y,x,n):
    global grid

    #checking if there is n in the vertical column
    #And if it does exist, then returning false as
    #There can be only one unique number in a given
    #coloumn in Sudoku
    for i in range(0,9):
        if grid[y][i] == n:
            return False     

    #checking if there is n in the horizontal row
    #And if it does exist, then returning false as
    #There can be only one unique number in a given 
    #row in Sudoku
    for i in range(0,9):
        if grid[i][x] == n:
            return False 

    #finding the coordinates of the starting cell in the
    #the sub 3x3 matrix 
    x_o = (x//3)*3
    y_o = (y//3)*3  

    #checking if the guess can be found in the sub 3x3 matrix
    #and if it is indeed found, then returning false
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y_o+i][x_o+j] == n:
                return False

    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return

    print("Solution: \n")
    print(np.matrix(grid))
    print("\n")
    input('More? ')

solve()  