import math
import random
from environment import Environment
from searchAlgorithms import *

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
    print(f"BFS: {bfs(env,env.start, env.goal)}")
    print(f"DFS: {dfs(env,env.start, env.goal)}")
    print(f"UCS: {ucs(env,env.start, env.goal)}")
    limit = math.ceil(len(env.grid)*len(env.grid[0])/2)
    print(f"DLS: {dls(env,env.start, env.goal, limit)}")

