from board import Board
import random

def hillClimbing(n, maxEvaluations):
    bestTable = Board(n)
    bestCost = bestTable.calculateCost()
    evaluations = 0

    while evaluations < maxEvaluations:
        newTable = Board(n)
        newTable.board = bestTable.board.copy()
        i, j = random.sample(range(n), 2)
        newTable.board[i], newTable.board[j] = newTable.board[j], newTable.board[i]
        newCost = newTable.calculateCost()
        evaluations += 1

        if newCost < bestCost:
            bestCost = newCost
            bestTable.board = newTable.board

        if bestCost == 0:
            break

    return bestTable, bestCost, evaluations
