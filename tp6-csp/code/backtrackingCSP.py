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
    
    return backtrackingCSP([],n, 0)

def backtrackingCSP(board, n, it = 0):
    if len(board) == n:
        return board, it
    else:
        for col in range(n):
            if not isAttacked(board, col):
                board.append(col)
                if isSolution(board, n):
                    return board, it
                else:
                    solution, it = backtrackingCSP(board, n, it +1)
                    if solution != None:
                        return solution, it
                board.pop()
        return None, it
    

