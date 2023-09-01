import math
import random
from environment import Environment
from algorithm import *
import matplotlib.pyplot as plt
import csv
import statistics

def randomPos(max):
    return random.randint(0, max - 1)

row = 100
columns = 100
obstacles_rate = 0.08
iterations = 30
results = []



for i in range(0,iterations):
    startX = randomPos(row)
    startY = randomPos(columns)
    goalX = randomPos(row)
    goalY = randomPos(columns)
    while (startX,startY) == (goalX,goalY):
        goalX = randomPos(row)
        goalY = randomPos(columns)

    env = Environment(row,columns,startX,startY,goalX,goalY,obstacles_rate)


    optimal_path = aPlus(env, (startX,startY), (goalX,goalY))
    print("Camino óptimo de it " , i , ": ", optimal_path)

    if optimal_path:
        results.append(len(optimal_path) - 1)


plt.boxplot(results)
plt.title('Distribución de costos de caminos óptimos')
plt.xlabel('Iteraciones')
plt.ylabel('Costo del camino')
plt.savefig('boxplot_resultados.png')

mean_cost = statistics.mean(results)
std_deviation = statistics.stdev(results)

print("Media del costo:", mean_cost)
print("Desviación estándar:", std_deviation)
    