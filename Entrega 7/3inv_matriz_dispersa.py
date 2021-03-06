import numpy as np
from numpy.linalg import inv
from numpy import double
from time import perf_counter

Ns = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100,
      125, 160, 200, 400, 800, 1000, 2000, 5000, 10000]

from scipy.sparse.linalg import inv
from scipy.sparse import csc_matrix, lil_matrix

def laplaciana(N, d=double):
    L_lil = lil_matrix(-(np.eye(N, k=-1, dtype=d)) + 2 *\
        (np.eye(N, dtype=d)) + -(np.eye(N,k=+1, dtype=d)))

    L = csc_matrix(L_lil)
    return L

Ncorridas = 5

for N in range(Ncorridas):

    name = (f"inv_matriz_dispersa{N}.txt")
    fid = open(name, "w")

    for i in Ns:
        print(f'i = {i}')

        t1 = perf_counter()
        A = laplaciana(i)
        t2 = perf_counter()
        A_inv = inv(A)
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2

        fid.write(f"{i} {dt1} {dt2}\n")
        fid.flush()

    fid.close()