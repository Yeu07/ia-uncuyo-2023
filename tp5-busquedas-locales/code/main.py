from hillClimbing import hillClimbing

n = 10
maxEvaluations = 100000
solution, cost, evaluations = hillClimbing(n,maxEvaluations)

print(f"Solucion para {n} reinas")

for fila in solution.board:
    print(' '.join('Q' if i == fila else '.' for i in range(n)))

print(f"Costo: {cost}")
print(f"Evaluaciones: {evaluations}")