from hillClimbing import hillClimbing
from simulatedAnnealing import simulatedAnnealing
from geneticAlgorithm import geneticAlgorithm
import time
import random
import statistics
import csv
import matplotlib.pyplot as plt

problems = [4, 8, 10]
maxEvaluations = [100, 1000, 10000]
it = 30
plot = False

solutionhillClimbing = []
solutionsimulatedAnnealing = []
solutiongeneticAlgorithm = []
timehillClimbing = []
timesimulatedAnnealing = []
timegeneticAlgorithm = []
algorithmnames = ["hillClimbing", "simulatedAnnealing", "geneticAlgorithm"]
randomploti = random.randint(0, len(problems) - 1)
randomplotj = random.randint(0, it - 1)

for i in range(0,len(problems)):

    for j in range(0,it):
        start = time.time()
        # Case for 4, 8 and 10 queens with hillClimbing
        if randomploti == i and randomplotj == j:
            solutionhillClimbing.append(hillClimbing(problems[i], maxEvaluations[i], True))
        else:
            solutionhillClimbing.append(hillClimbing(problems[i], maxEvaluations[i],False))

        end = time.time()
        timehillClimbing.append(end - start)

        start = time.time()
        # Case for 4,8 and 10 queens with simulatedAnnealing
        if randomploti == i and randomplotj == j:
            solutionsimulatedAnnealing.append(simulatedAnnealing(problems[i], maxEvaluations[i], True))
        else:   
            solutionsimulatedAnnealing.append(simulatedAnnealing(problems[i], maxEvaluations[i],False))
        end = time.time()
        timesimulatedAnnealing.append(end - start)

        
        # Case for 4,8 and 10 queens with geneticAlgorithm
        start = time.time()
        if i == randomploti and randomplotj == j:
            solutiongeneticAlgorithm.append(geneticAlgorithm(problems[i], maxEvaluations[i], True))             
        else:
            solutiongeneticAlgorithm.append(geneticAlgorithm(problems[i], maxEvaluations[i],False))
        end = time.time()
        timegeneticAlgorithm.append(end - start)


def calaculatePercentage(solution):

    filtered = [x for x in solution if x[0].calculateCost() == 0]
    return len(filtered) / len(solution) * 100

def averageTime(listtime):

    return sum(listtime) / len(listtime)

def averageState(solution):
    
    return sum([x[1] for x in solution]) / len(solution)


def printResults(solution, algorithmname, time):

    print(f"stats for {algorithmname}")
    print(f"El porcentaje de veces que se llega a un estado de solucion optimo es: {calaculatePercentage(solution)}")
    print(f"El tiempo promedio de ejecucion es: {averageTime(time)}")
    print(f"La desviacion estandar del tiempo es: {statistics.stdev(time)}")
    print(f"El promedio de estados es: {averageState(solution)}")
    print(f"La desviacion estandar de los estados es: {statistics.stdev([x[1] for x in solution])}")
    print("\n")



printResults(solutionhillClimbing, algorithmnames[0], timehillClimbing)
printResults(solutionsimulatedAnnealing, algorithmnames[1] , timesimulatedAnnealing)
printResults(solutiongeneticAlgorithm, algorithmnames[2] , timegeneticAlgorithm)


alltimes = [timehillClimbing, timesimulatedAnnealing, timegeneticAlgorithm]

plt.figure(figsize=(12, 6))
plt.ylim(-0.5, 0.7)
plt.boxplot(alltimes, labels=algorithmnames)
plt.title("Distribución de Tiempos de Ejecución por Algoritmo")
plt.xlabel("Algoritmo")
plt.ylabel("Tiempo de Ejecución (segundos)")
plt.grid(True)
plt.savefig("boxplot.png")

with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['algorithm_name', 'run_n', 'estate_n', 'solution_found']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for j in range(0,len(problems)):
        for i in range(0,it):
            writer.writerow({'algorithm_name': algorithmnames[0], 'run_n': problems[j], 'estate_n': solutionhillClimbing[i][1], 'solution_found': solutionhillClimbing[i][0].calculateCost() == 0})
        for i in range(0,it):
            writer.writerow({'algorithm_name': algorithmnames[1], 'run_n': problems[j], 'estate_n': solutionsimulatedAnnealing[i][1], 'solution_found': solutionsimulatedAnnealing[i][0].calculateCost() == 0})
        for i in range(0,it):
            writer.writerow({'algorithm_name': algorithmnames[2], 'run_n': problems[j], 'estate_n': solutiongeneticAlgorithm[i][1], 'solution_found': solutiongeneticAlgorithm[i][0].calculateCost() == 0})


