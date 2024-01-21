#!/home/mark/software/anaconda3/bin/python

import begin
import enum

MAXROW = 10
MAXCOL = 10

class STATUS:
    dead = "0"
    alive = "1"
    
class GRID:
    row = []
    col = []
    grid = {}
    
    def __init__(self):
        for i in range(MAXROW):
            for j in range(MAXCOL):
                grid[i,j] = STATUS.dead
        

@begin.start
def run():
    print("Conway's gave of life")
    print("area = {0}x{1}".format(MAXROW, MAXCOL))
    
    grid = {}
    for i in range(MAXROW):
        for j in range(MAXCOL):
            grid[i,j] = 0
            
    print(grid[3,4])
    
    status = STATUS
    map = GRID
    print(map.grid[3,4])
    #print(grid.grid[2,3])
    #print("grid[1][3]: {0}".format(grid.grid[1,3]))
    
    

          
    
    