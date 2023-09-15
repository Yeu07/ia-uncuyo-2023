from board import Board
import random
import matplotlib.pyplot as plt



def hillClimbing(n, maxEvaluations, plot = False):
    bestTable = Board(n)
    bestCost = bestTable.calculateCost()
    evaluations = 0
    fitness = []

    while evaluations < maxEvaluations:
        newTable = Board(n)
        newTable.board = bestTable.board.copy()
        i, j = random.sample(range(n), 2)
        newTable.board[i], newTable.board[j] = newTable.board[j], newTable.board[i]
        newCost = newTable.calculateCost()
        evaluations += 1
        fitness.append(newCost)
        if newCost < bestCost:
            bestCost = newCost
            bestTable.board = newTable.board

        
        if bestCost == 0:
            if plot:
                plt.plot(fitness)
                plt.title(f'hillClimbing {evaluations} evaluations')
                plt.savefig('hillclimbing.png')
            return (bestTable, evaluations)
        
    if plot:
        plt.plot(fitness)
        plt.title(f'HillClimbing {evaluations} evaluations')
        plt.savefig('hillClimbing.png')

    return (bestTable, evaluations)
