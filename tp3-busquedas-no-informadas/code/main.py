import math
import random
from environment import Environment
from searchAlgorithms import *
import matplotlib.pyplot as plt

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
    result=dls(env,env.start, env.goal, limit)
    if result != None:
        resultsDLS.append(result)

algorithms = ["BFS", "DFS", "UCS", "DLS"]

all_results = [resultsBFS, resultsDFS, resultsUCS, resultsDLS ]

plt.boxplot(all_results, labels=algorithms)
plt.ylabel('Número de pasos')
plt.title('Comparación de Algoritmos de Búsqueda')
plt.savefig('boxplot_resultados.png')



