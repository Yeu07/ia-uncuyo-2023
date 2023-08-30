class Node:
    
    def __init__(self,position, cost=0,parent=None):
        self.parent = parent
        self.position = position
        self.cost = cost
