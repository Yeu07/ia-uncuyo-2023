import random

class Board:

    def __init__(self, n):

        # Create random solution
        self.board = [random.randint(0, n - 1) for _ in range(0, n)]
    
    def calculateCost(self):
        n = len(self.board)
        cost = 0

        for i in range(0, n):
            for j in range(i + 1, n):
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == abs(i - j):
                    cost += 1

        return cost
    

        