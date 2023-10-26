from board import *


def isAttacked(board, column):
    n = len(board)
    for i in range(n):
        if board[i] == column:
            return True
        offset = n - i
        if board[i] == column - offset or board[i] == column + offset:
            return True
    return False

def isSolution(board, n):
    return len(board) == n

def searchbacktrackingCSP(n):
    it = [0]
    board = backtrackingCSP([],n, it)
    return board, it[0]

def backtrackingCSP(board, n, iterations):
    if len(board) == n:
        return board
    else:
        for col in range(n):
            iterations[0] += 1
            if not isAttacked(board, col):
                board.append(col)
                if isSolution(board, n):
                    return board
                else:
                    solution = backtrackingCSP(board, n, iterations)
                    if solution != None:
                        return solution
                board.pop()
        return None
    
