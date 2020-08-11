from scipy import matrix, rand, savetxt
from time import perf_counter
import matplotlib.pyplot as plt

def mimatmul(A,B):
    Ca = len(A[0])
    Cb = len(A[1])
    Fa = len(A)

    #arma matriz con 0
    Maxb = [[0 for b in range(Cb)] for a in range(Fa)]

    #rellena filas y columnas
    for i in range(Fa):
        for j in range(Cb):
            for k in range(Ca):
                Maxb[i][j] += A[i][k] * B[k][j]

    return Maxb