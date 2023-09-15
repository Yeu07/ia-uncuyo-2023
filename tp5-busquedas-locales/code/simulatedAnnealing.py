from board import Board
import random
import math
import matplotlib.pyplot as plt

def simulatedAnnealing(n, maxEvaluations, plot = False):
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
        else:
            delta = newCost - bestCost
            if random.random() < math.exp(-delta / 100):
                bestCost = newCost
                bestTable.board = newTable.board

        if bestCost == 0 :
            iteration = evaluations
            flag = False
        
    if plot:
        plt.plot(fitness)
        plt.title(f'SimulatedAnnaling {evaluations} evaluations')
        plt.savefig('tp5-busquedas-locales/Plots/simulatedAnnaling.png')
    
    return (bestTable, iteration)

