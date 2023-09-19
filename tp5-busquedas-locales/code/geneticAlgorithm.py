import random
from board import Board
import matplotlib.pyplot as plt
def crossover(parent1, parent2):
    
        # Randomly select a crossover point
        # Create a child solution
        # Copy the first part of the first parent
        # Copy the second part of the second parent
        # Return the child solution
    
        crossoverPoint = random.randint(0, len(parent1.board) - 1)
        child = Board(len(parent1.board))
        child.board = parent1.board[:crossoverPoint] + parent2.board[crossoverPoint:]
        return child

def mutation(child):
        
        # Randomly select a mutation point
        # Mutate the child solution
        # Return the mutated child solution
        
        mutationPoint = random.randint(0, len(child.board) - 1)
        child.board[mutationPoint] = random.randint(0, len(child.board) - 1)
        return child



def geneticAlgorithm(n, maxGenerations, plot):

    # 100 individuals
    # Selection for tournament
    # Operators of crossover and mutation
    # Replace the entired population
    # Stop condition: maxGenerations

    populationSize = 100
    popultion = []
    generation = 0
    fitness = []
    iteration = maxGenerations
    flag = True

    for i in range(populationSize):
        popultion.append(Board(n))

    while generation < maxGenerations and flag:
        popultion = sorted(popultion, key=lambda x: x.calculateCost())
        bestpopultion = popultion[0]
        bestsolution = popultion[0].calculateCost()
        fitness.append(bestsolution)

        if bestsolution == 0:
            iteration = generation
            flag = False
             
        
        newpopultion = [bestpopultion]

        for i in range(1, populationSize):
            parent1 = random.choice(popultion[:int(populationSize/2)])
            parent2 = random.choice(popultion[:int(populationSize/2)])
            child = crossover(parent1,parent2)
            child = mutation(child)
            newpopultion.append(child)
        
        popultion = newpopultion
        generation += 1
    
    if plot:
        plt.plot(fitness)
        plt.title(f'GeneticAlgorithm {generation} generations')
        plt.savefig('tp5-busquedas-locales/Plots/geneticAlgorithm.png')

    return (bestpopultion, iteration)
    