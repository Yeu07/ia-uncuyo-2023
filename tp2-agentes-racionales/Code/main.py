from agent import Agent
from agentRandom import AgentRandom
from environment import Environment
import random

import openpyxl

# Crear un nuevo libro de trabajo (workbook)
workbook = openpyxl.Workbook()

sizes = [2, 4, 8, 16, 32, 64, 128]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
repetitions = 10

for size in sizes:
    # Crear una hoja (worksheet) para los resultados de este tamaño
    results_worksheet = workbook.create_sheet(title=f"Size_{size}")
    
    # Agregar encabezados a la tabla
    results_worksheet.append(["Dirt Rate", "Total Performance", "Total Time Units"])
    
    for dirt_rate in dirt_rates:
        for _ in range(repetitions):
            env = Environment(size, size, random.randint(0, size - 1), random.randint(0, size - 1), dirt_rate)
            agent = Agent(env)
            
            while agent.env.get_time_units() > 0 and agent.env.dirt > 0:
                agent.think()
                
            total_performance = agent.env.get_performance()
            total_time_units = 1000 - agent.env.get_time_units()
            
            results_worksheet.append([dirt_rate, total_performance, total_time_units])

# Guardar el archivo Excel
workbook.save("simulation_Agent.xlsx")

print("Archivo Excel creado exitosamente.")

