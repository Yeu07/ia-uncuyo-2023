from board import Board
import random
import matplotlib.pyplot as plt



def hillClimbing(n, maxEvaluations, plot = False):
    bestTable = Board(n)
    bestCost = bestTable.calculateCost()
    evaluations = 0
    fitness = []
    iteration = maxEvaluations
    flag = True

    while evaluations < maxEvaluations and flag:
        newTable = Board(n)
        newTable.board = bestTable.board.copy()
        i, j = random.sample(range(n), 2)
        newTable.board[i], newTable.board[j] = newTable.board[j], newTable.board[i]
        newCost = newTable.calculateCost()
        evaluations += 1
        fitness.append(bestCost)
        if newCost < bestCost:
            bestCost = newCost
            bestTable.board = newTable.board

        
        if bestCost == 0:
            iteration = evaluations
            flag = False
        
    if plot:
        plt.plot(fitness)
        plt.title(f'HillClimbing {evaluations} evaluations')
        plt.savefig('tp5-busquedas-locales/Plots/hillClimbing.png')

    return (bestTable, iteration)
