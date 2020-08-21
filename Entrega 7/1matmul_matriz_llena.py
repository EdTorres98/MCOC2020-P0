from scipy import matrix, rand, savetxt, matmul
from numpy import double
from time import perf_counter
from matplotlib import pyplot as plt

Ns = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100,
      125, 160, 200, 400, 800, 1000, 2000, 5000, 10000]

Ncorridas = 5

for i in range(Ncorridas):

    name = (f"matmul_matriz_llena{i}.txt")
    fid = open(name, "w")

    for N in Ns:
        print(f"n={N}")

        t1 = perf_counter()
        A = rand(N, N)
        B = rand(N, N)
        A = double(A)
        B = double(B)
        t2 = perf_counter()
        C = A@B
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2

        fid.write(f"{N} {dt1} {dt2}\n")
        fid.flush()

    fid.close()