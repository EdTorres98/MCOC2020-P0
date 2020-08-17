from time import perf_counter
from scipy import zeros
from numpy import fill_diagonal, matrix, float32
import scipy as sp
import scipy.linalg as spLinalg
import numpy as np

Ns = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55,
      60, 75, 100, 125, 160, 200,
      250,350, 500, 600, 800, 1000,
      2000, 3000, 4000, 5000, 6000,
      7000, 8000, 9000, 10000]

def laplaciana(N, d=float32):   #Laplaciana ayudantía
    L = -(np.eye(N, k=-1, dtype=d)) + 2 *\
        (np.eye(N, dtype=d)) + -(np.eye(N,k=+1, dtype=d))
    return L

#corridas
Ncorridas = 10

names = ["A_invB_inv.txt", "A_invB_npSolve.txt", "A_invB_spSolve.txt",
         "A_invB_spSolve_symmetric.txt", "A_invB_spSolve_pos.txt", "A_invB_spSolve_pos_overwrite.txt"]

files =[open(name, 'w') for name in names]

for N in Ns:

    dts = np.zeros((Ncorridas, len(files)))  #Lista para ingresar tiempos
    print(f"N = {N}")

    for i in range(Ncorridas):
        print(f'i = {i}')

        #(1) A_invB_inv
        A = laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B    #!!
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][0] = dt     #!!

        #(2) A_invB_npSolve
        A = laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A,B)    #!!
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][1] = dt       #!!

        #(3) A_invB_spSolve
        A = laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A,B)    #!!
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][2] = dt       #!!

        #(4) A_invB_spSolve_symmetric
        A = laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A,B,assume_a="sym")    #!!
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][3] = dt       #!!

        #(5) A_invB_spSolve_pos
        A = laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A,B,assume_a="pos")    #!!
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][4] = dt       #!!

        #(6) A_invB_spSolve_pos_overwrite
        A = laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A,B,assume_a="pos",overwrite_a=True)    #!!
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][5] = dt       #!!

    print("dts: ", dts)

    #promedio de cada columna
    dts_mean = [np.mean(dts[:, j]) for j in range(len(files))]
    print("dts_mean: ", dts_mean)

    #Escribo los resultados en el archivo de texto
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()

[file.close() for file in files]