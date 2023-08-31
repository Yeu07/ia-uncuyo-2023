from node import Node
from environment import Environment
from collections import deque


def performAction(position, action):
    x, y = position
    if action == "arriba":
        return x - 1, y
    elif action == "abajo":
        return x + 1 , y
    elif action == "izquierda":
        return x, y - 1
    elif action == "derecha":
        return x, y + 1

def bfs(env, start, goal):
    node = Node(start)
    queue = [node] 

    visited = set()
    count = 0

    while queue:
        node = queue.pop()
        visited.add(node.position)
        count += 1

        if node.position == goal:
            return count
        
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            x, y = performAction(node.position, action)
            if (x, y) not in visited and env.isValidLocation(x, y):
                new_node = Node((x, y), node, action)
                visited.add(new_node.position)  # Marcamos el nuevo nodo como visitado
                queue.append(new_node)
    
    return None


def dfs(env, start, goal):

    node = Node(start)
    stack = [node]
    visited = set()
    count = 0

    while stack:

        node = stack.pop(0)
        count += 1
        visited.add(node.position)

        if node.position == goal:
            return count
        
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            x, y = performAction(node.position, action)
            if (x,y) not in visited and env.isValidLocation(x,y):
                new_node = Node((x,y), node,)
                stack.insert(0,new_node)

    return None

def ucs(env, start, goal):

    queue = [(0, Node(start))]
    visited = set()
    count = 0

    while queue:
        cost, node = queue.pop(0)
        count += 1

        if node.position == goal:
            return count

        if node.position in visited:
            continue

        visited.add(node.position)
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            x, y = performAction(node.position, action)
            if env.isValidLocation(x, y):
                new_node = Node((x, y), node, action)
                new_cost = cost + 1  # Incrementamos el costo
                queue.append((new_cost, new_node))

        queue.sort(key=lambda x: x[0])  # Ordenar por costo

    return None

def dls(env, start, goal, limit):
    stack = [Node(start)]
    visited = set()
    count = 0

    while stack:
        node = stack.pop()
        count += 1
        visited.add(node.position)
        limit -= 1

        if node.position == goal:
            return count
        
        if limit <= 0:
            return None
        
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            x, y = performAction(node.position, action)
            if (x, y) not in visited and env.isValidLocation(x, y):
                new_node = Node((x, y), node)
                stack.append(new_node)

    return None

    