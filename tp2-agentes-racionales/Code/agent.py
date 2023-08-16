from environment import Environment
import random

class Agent:
    def __init__(self, env):
        self.env = env
        
    def up(self):
        self.env.accept_action("Arriba")
        
    def down(self):
        self.env.accept_action("Abajo")
        
    def left(self):
        self.env.accept_action("Izquierda")
        
    def right(self):
        self.env.accept_action("Derecha")
        
    def suck(self):
       self.env.accept_action("Limpiar")
        
    def idle(self):
        pass
        
    def perspective(self):
        return self.env.is_dirty()
    
    def think(self):
        if self.perspective():
            self.suck()
        else:
            # Move randomly
            actions = ["Arriba", "Abajo", "Izquierda", "Derecha", "Idle"]
            random_action = random.choice(actions)
            
            if random_action == "Arriba":
                self.up()
            elif random_action == "Abajo":
                self.down()
            elif random_action == "Izquierda":
                self.left()
            elif random_action == "Derecha":
                self.right()
            elif random_action == "Idle":
                self.idle()


