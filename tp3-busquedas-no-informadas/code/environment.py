import random
import math

class Environment:
    
    def __init__(self, row, column, startX, startY, goalX, goalY, obstacle_rate):

        self.row = row
        self.column = column
        self.start = (startX, startY)
        self.goal = (goalX, goalY)
        self.obstacle_rate = obstacle_rate

        self.grid = self.createGrid()

    def createGrid(self):
        grid=[[0 for _ in range(self.row)]for _ in range(self.row)]
        obstacle = math.trunc(self.obstacle_rate * self.row * self.column)
        while obstacle > 0:
            x = random.randint(0, self.row - 1)
            y = random.randint(0, self.column - 1 )
            if grid[x][y] == 0 and (x,y) != self.start and (x,y) != self.goal:
                grid[x][y] = 1
                obstacle -=1
        return grid
    
    def isValidLocation(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.column and self.grid[x][y] != 1
            