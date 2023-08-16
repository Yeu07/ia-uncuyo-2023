import random
import math
class Environment:
    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.agentX = init_posX
        self.agentY = init_posY
        self.dirt_rate = dirt_rate
        self.performance = 0
        self.time_units = 1000  # Inicializar unidades de tiempo en 1000
        self.grid = [[0 for _ in range(sizeY)] for _ in range(sizeX)]
        self.dirt = math.trunc(dirt_rate*sizeX*sizeY) # Cantidad de celdas csucias restantes

        while self.dirt>0:
            x = random.randint(0,sizeX - 1)
            y = random.randint(0,sizeY - 1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = 1
                self.dirt -= 1
        
        self.dirt = math.trunc(dirt_rate*sizeX*sizeY)



        
        
        
    def accept_action(self, action):
        if self.time_units <= 0:
            return
        if action == "Arriba" and self.agentX > 0:
            self.agentX -= 1
        elif action == "Abajo" and self.agentX < self.sizeX - 1:
            self.agentX += 1
        elif action == "Izquierda" and self.agentY > 0:
            self.agentY -= 1
        elif action == "Derecha" and self.agentY < self.sizeY - 1:
            self.agentY += 1
        elif action == "Limpiar":
            if self.grid[self.agentX][self.agentY] == 1:
                self.grid[self.agentX][self.agentY] = 0
                self.performance += 1
                self.dirt -= 1
        
        self.time_units -= 1  # Descontar una unidad de tiempo
        
    def is_dirty(self):
        return self.grid[self.agentX][self.agentY] == 1
    

    def get_performance(self):
        return self.performance
    
    def get_time_units(self):
        return self.time_units
    
    def print_environment(self):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                if x == self.agentX and y == self.agentY:
                    print("A", end=" ")
                elif self.grid[x][y] == 1:
                    print("D", end=" ")
                else:
                    print(".", end=" ")
            print()