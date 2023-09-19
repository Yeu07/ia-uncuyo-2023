import random
def createBoard(n):
    board = []
    for i in range(n):
        board.append(random.randint(0, n - 1))
    return board

def calculateCost(board):
    n = len(board)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                cost += 1
            offset = j - i
            if board[i] == board[j] - offset or board[i] == board[j] + offset:
                cost += 1
    return cost
    
def printBoard(solution):
    n = len(solution)
    for i in range(n):
        print(" ---" * n)
        for j in range(n):
            if solution[j] == n - i - 1:
                print("| Q ", end="")
            else:
                print("|   ", end="")
        print("|")
    print(" ---" * n)