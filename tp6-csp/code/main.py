from backtrackingCSP import searchbacktrackingCSP
from forwardCheckingCSP import searchforwardcheckingCSP
import time
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def excute(function, n):

    start = time.time()
    board, it = function(n)
    end = time.time()
    return end-start, it

def printResults(algortihmName, n, time, it):

    width, height = 400, 200
    image = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 10)
    textTime = f"Tiempo para {n} reinas con {algortihmName}: {time}"
    textIt = f"iteraciones: {it1}"

    draw.text((20,80), textTime, fill="black", font=font)
    draw.text((20,120), textIt, fill="black", font=font)
    image.save(f"tp6-csp/code/results/{algortihmName}-{n}.png")

    print(f"Tiempo para {n} reinas con {algortihmName}: {time}")
    print(f"iteraciones: {it1}")
    print("---------------------------")

if __name__ == "__main__":
    problems = [4, 8, 10, 12, 15]
    algorithmnames = ["backtracking", "forwardchecking"]
    it = 30
    totalTimesbacktracking = []
    totalTimesforwardchecking = []
    totalIterationsbacktracking = []
    totalIterationsforwardchecking = []

    for n in problems:
        time1, it1 = excute(searchbacktrackingCSP, n)
        time2, it2 = excute(searchforwardcheckingCSP, n)

        printResults(algorithmnames[0], n, time1, it1)
        printResults(algorithmnames[1], n, time2, it2)

        

        totalTimesbacktracking.append(time1)
        totalTimesforwardchecking.append(time2)
        totalIterationsbacktracking.append(it1)
        totalIterationsforwardchecking.append(it2)
    
    # Create box plots for execution times
    plt.boxplot([totalTimesbacktracking,totalTimesforwardchecking], labels=algorithmnames)
    plt.title("Distribution of Execution Times")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (seconds)")
    plt.savefig("tp6-csp/code/plots/boxplotTime.png")

    # Create box plots for iterations
    plt.boxplot([totalIterationsbacktracking,totalIterationsforwardchecking], labels=algorithmnames)
    plt.title("Distribution of Iterations")
    plt.xlabel("Algorithm")
    plt.ylabel("Iterations")
    plt.savefig("tp6-csp/code/plots/boxplotIterations.png")


