from hillClimbing import hillClimbing
from simulatedAnnealing import simulatedAnnealing
from geneticAlgorithm import geneticAlgorithm

def printResults(solution, it, name):
    n = len(solution[it][0].board)
    print(f"Solucion para {n} reinas usando {name}")

    for fila in solution[it][0].board:
        print(' '.join('Q' if i == fila else '.' for i in range(n)))

    print(f"Costo: {solution[it][1]}")
    print(f"Evaluaciones: {solution[it][2]}")


problems = [4, 8, 10]
maxEvaluations = [1000, 10000, 100000]

solutionhillClimbing = []
solutionsimulatedAnnealing = []
solutiongeneticAlgorithm = []


for i in range(len(problems)):

    # Case for 4, 8 and 10 queens with hillClimbing
    solutionhillClimbing.append(hillClimbing(problems[i], maxEvaluations[i]))
    printResults(solutionhillClimbing, i, "hillClimbing")

    # Case for 4,8 and 10 queens with simulatedAnnealing
    solutionsimulatedAnnealing.append(simulatedAnnealing(problems[i], maxEvaluations[i]))
    printResults(solutionsimulatedAnnealing, i, "simulatedAnnealing")

    # Case for 4,8 and 10 queens with geneticAlgorithm
    solutiongeneticAlgorithm.append(geneticAlgorithm(problems[i], maxEvaluations[i]))
    printResults(solutiongeneticAlgorithm, i, "geneticAlgorithm")
