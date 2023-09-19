from board import Board
import random
import math
import matplotlib.pyplot as plt

def simulatedAnnealing(n, maxEvaluations, plot):
    bestTable = Board(n)
    bestCost = bestTable.calculateCost()
    evaluations = 0
    fitness = []
    iteration = maxEvaluations
    flag = True
    temperature = 1000
    coolingRate = 0.003

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
            if random.uniform(0, 1) < math.exp((bestCost - newCost) / temperature):
                bestCost = newCost
                bestTable.board = newTable.board

        temperature *= 1 - coolingRate

        if bestCost == 0:
            iteration = evaluations
            flag = False

    if plot:
        plt.plot(fitness)
        plt.title(f'Simulated Annealing {evaluations} evaluations')
        plt.xlabel('Iterations')
        plt.ylabel('Cost')
        plt.savefig('tp5-busquedas-locales/Plots/simulatedAnnealing.png')

    return (bestTable, iteration)

