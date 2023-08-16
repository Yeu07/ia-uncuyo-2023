from agent import Agent
from environment import Environment
import random

def evaluate_agent_performance(size, dirt_rate, repetitions):
    for _ in range(repetitions):
        env = Environment(size, size, random.randint(0, size - 1), random.randint(0, size - 1), dirt_rate)
        agent = Agent(env)
        
        while agent.env.get_time_units() > 0 and agent.env.dirt > 0:
            agent.think()
            
        total_performance = agent.env.get_performance()
        total_time_units = (1000 - agent.env.get_time_units())
    
        print(f"Size: {size}x{size}, Dirt Rate: {dirt_rate}")
        print(f"Total Performance: {total_performance}, Total Time Units: {total_time_units}")
        print()

sizes = [2, 4, 8, 16, 32, 64, 128]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
repetitions = 10

for size in sizes:
    for dirt_rate in dirt_rates:
        evaluate_agent_performance(size, dirt_rate, repetitions)
