from backtrackingCSP import searchbacktrackingCSP
from forwardChainingCSP import searchforwardChainingCSP
from board import printBoard
import time
import matplotlib.pyplot as plt


def excute(function, n):

    start = time.time()
    baord, it = function(n)
    end = time.time()
    return end-start, it

problems = [4, 8, 10, 12, 15]
algorithmnames = ["backtracking", "forwardChaining"]
it = 30


for n in problems:
 
    time1, it1 = excute(searchbacktrackingCSP,n)
    time2, it2 = excute(searchforwardChainingCSP, n)

    print(f"Tiempo para {n} reinas con backtracking: {time1}")
    print(f"iteraciones: {it1}")

    print("-----------------------------------------------------")
    print(f"Tiempo para {n} reinas con forwardChaining: {time2}")
    print(f"iteraciones: {it2}")
    print("-----------------------------------------------------")


