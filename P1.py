import numpy as np
import matplotlib.pyplot as plt


def main():
    A = np.random.randint(2, size = (10000,1000))
    B = np.random.randint(2, size = (1000,100000))
    C = np.random.randint(2, size = (100000,1))

    print(f"Matrix A:\n {A}\n")
    print(f"Matrix B:\n {B}\n")
    print(f"Matrix C:\n {C}\n")

    plot(A, "matrix A")
    #D = np.matmul(np.matmul(A,B), C)
    #print(f"Matrix D:\n {D}\n")


def plot(A, name):
    #CDF
    x, counts = np.unique(A, return_counts=True)
    cumsum = np.cumsum(counts)
    y = cumsum / cumsum[-1]

    x = np.insert(x, 0, x[0])
    y = np.insert(y, 0, 0.)
    plt.xlabel("Value")
    plt.ylabel("%")
    plt.title(f"CDF {name}")
    plt.plot(x, y, drawstyle='steps-post')
    plt.grid(True)
    plt.show()


if __name__=="__main__":
    main()
