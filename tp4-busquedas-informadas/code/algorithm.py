from queue import PriorityQueue
from node import Node

from queue import PriorityQueue
from node import Node

def performAction(position, action):
    x, y = position
    if action == "arriba":
        return x - 1, y
    elif action == "abajo":
        return x + 1, y
    elif action == "izquierda":
        return x, y - 1
    elif action == "derecha":
        return x, y + 1

def heuristic(state, goal):
    return abs(state.position[0] - goal[0]) + abs(state.position[1] - goal[1])

def aPlus(env, start, goal):
    node = Node(start)
    queue = PriorityQueue()
    queue.put((0, node))
    came_from = {}
    g_score = {node.position: 0}

    while not queue.empty():
        _, current = queue.get()

        if current.position == goal:
            path = getPath(came_from, current)
            return path

        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            next_pos = performAction(current.position, action)

            if env.isValidLocation(*next_pos) and g_score[current.position] + 1 < g_score.get(next_pos, float('inf')):
                next_node = Node(position=next_pos, cost=g_score[current.position] + 1, parent=current)
                came_from[next_node] = current
                g_score[next_pos] = g_score[current.position] + 1
                f_score = g_score[next_pos] + heuristic(next_node, goal)
                queue.put((f_score, next_node))
        
    return None

def getPath(came_from, current):
    path = [current.position]
    while current in came_from:
        current = came_from[current]
        path.append(current.position)
    path.reverse()
    return path




