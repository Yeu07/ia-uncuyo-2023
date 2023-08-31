import math
import random
from environment import Environment
from searchAlgorithms import *
import matplotlib.pyplot as plt
import csv
import statistics

def randomPos(max):
    return random.randint(0, max - 1)

row = 100
columns = 100
obstacles_rate = 0.08
iterations = 30
resultsDFS = []
resultsBFS = []
resultsUCS = []
resultsDLS = []


for i in range(0,iterations):
    startX = randomPos(row)
    startY = randomPos(columns)
    goalX = randomPos(row)
    goalY = randomPos(columns)
    while (startX,startY) == (goalX,goalY):
        goalX = randomPos(row)
        goalY = randomPos(columns)
    
    env = Environment(row,columns,startX,startY,goalX,goalY,obstacles_rate)
    resultsBFS.append(bfs(env,env.start, env.goal))
    resultsDFS.append(dfs(env,env.start, env.goal))
    resultsUCS.append(ucs(env,env.start, env.goal))
    limit = math.ceil(len(env.grid)*len(env.grid[0])/2)
    result=dls(env,env.start, env.goal, limit+4000)
    if result != None:
        resultsDLS.append(result)

    print(f"[BFS]: {resultsBFS[i]}")
    print(f"[DFS]: {resultsDFS[i]}")
    print(f"[UCS]: {resultsUCS[i]}")
    if i < len(resultsDLS):
        print(f"[DLS]: {resultsDLS[i]}")
    else:
        print(f"[DLS]: {None}")

algorithms = ["BFS", "DFS", "UCS", "DLS"]

all_results = [resultsBFS, resultsDFS, resultsUCS, resultsDLS ]

plt.boxplot(all_results, labels=algorithms)
plt.ylabel('Número de pasos')
plt.title('Comparación de Algoritmos de Búsqueda')
plt.savefig('boxplot_resultados.png')

mean_results = [statistics.mean(results) for results in all_results]
std_dev_results = [statistics.stdev(results) for results in all_results]

print(" ")

for i, algorithm in enumerate(algorithms):
    print(f"Algoritmo: {algorithm}")
    print(f"Media: {mean_results[i]}")
    print(f"Desviación estándar: {std_dev_results[i]}")
    print()

with open('no-informada-results.csv', 'w', newline='') as csvfile:
    fieldnames = ['algorithm_name', 'run_n', 'estate_n', 'solution_found']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for run_n in range(iterations):
        writer.writerow({'algorithm_name': 'BFS', 'run_n': run_n + 1, 'estate_n': resultsBFS[run_n], 'solution_found': 'Yes' if resultsBFS[run_n] is not None else 'No'})
        writer.writerow({'algorithm_name': 'DFS', 'run_n': run_n + 1, 'estate_n': resultsDFS[run_n], 'solution_found': 'Yes' if resultsDFS[run_n] is not None else 'No'})
        writer.writerow({'algorithm_name': 'UCS', 'run_n': run_n + 1, 'estate_n': resultsUCS[run_n], 'solution_found': 'Yes' if resultsUCS[run_n] is not None else 'No'})
        if run_n < len(resultsDLS):
            writer.writerow({'algorithm_name': 'DLS', 'run_n': run_n + 1, 'estate_n': resultsDLS[run_n], 'solution_found': 'Yes' if resultsDLS[run_n] is not None else 'No'})
        else:
            writer.writerow({'algorithm_name': 'DLS', 'run_n': run_n + 1, 'estate_n': limit , 'solution_found': 'No'})


