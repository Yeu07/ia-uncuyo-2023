class Node:
    def __init__(self, position, cost=0, parent=None):
        self.parent = parent
        self.position = position
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

