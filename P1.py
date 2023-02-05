import numpy as np
import matplotlib.pyplot as plt
from memory_profiler import profile
import time
import psutil as ps

@profile
def main():
    print("CPU percentage", ps.cpu_percent())
    print("Virtual memory", ps.virtual_memory())

    start = time.time()

    #create matrices
    A = np.random.randint(2, size = (10000,1000))
    B = np.random.randint(2, size = (1000,100000))
    C = np.random.randint(2, size = (100000,1))

    mid1 = time.time()

    CDF(A, "matrix A")

    mid2 = time.time()
    
    #create matrix D=(A*B)*C
    D = np.matmul(np.matmul(A,B), C)

    end = time.time()

    print("CPU percentage", ps.cpu_percent())
    print("Virtual memory", ps.virtual_memory())

    CDF(D, "matrix D")

    print(f"time to create matrices: {mid1-start}")
    print(f"time to plot A: {mid2-mid1}")
    print(f"time to calculate D: {end-mid2}")

def CDF(A, name):
    #plot the ECDF and save it as a png
    x, counts = np.unique(A, return_counts=True)
    cumsum = np.cumsum(counts)
    y = cumsum / cumsum[-1]

    x = np.insert(x, 0, x[0])
    y = np.insert(y, 0, 0.)
    plt.xlabel("Value")
    plt.ylabel("%")
    plt.title(f"CDF {name}")
    plt.plot(x, y, drawstyle="steps-post")
    plt.grid(True)
    plt.savefig(f"{name}.png")


if __name__=="__main__":
    main()
