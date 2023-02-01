import numpy as np

A = np.random.randint(2, size = (1000000,1000))
B = np.random.randint(2, size = (1000,1000000))
C = np.random.randint(2, size = (1000000,1))

print(f"Matrix A:\n {A}\n")
print(f"Matrix B:\n {B}\n")
print(f"Matrix C:\n {C}\n")

D = np.matmul(A,B)
#print(f"Matrix D:\n {D}\n")


def multiply(A,B):
    global result
    if A.shape[1] == B.shape[0]:
        result = np.zerps((A.shape[0],B.shape[1]), dtype = int)
        for row in range(rows):
            for col in range(cols):
                for elt in range(len(B)):
                    result[row, col] += A[row, elt] * B[elt, col]
        return result
    else:
        return "sorry fail"
