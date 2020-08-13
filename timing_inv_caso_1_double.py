from scipy import matrix, rand, savetxt, zeros
from time import perf_counter
import matplotlib.pyplot as plt
from numpy import fill_diagonal, double, matrix
from numpy.linalg import inv

Ns = [2, 5, 10,
      12, 15, 20,
      30, 40, 45, 50, 55,
      60, 75, 100,
      125, 160, 2000, 3000]

Ncorridas = 10    #10 corridas

for i in range(Ncorridas):

    dts = []  #Lista tiempos
    mem = []  #Lista memorias utilizadas

    name = (f"caso_1_double{i}.txt")  #!!!
    fid = open(name, "w")

    for N in Ns:  #loop sobre los tamaños de matrices
        print(f"n={N}")

    #lap
        A = zeros((N, N))
        fill_diagonal(A,2)
        for i in range(N):
            for j in range(N):
                if i-1==j or i+1==j:
                    A[i][j] = -1

        A = double(A)    #!!!

        t1 = perf_counter()

        A_inv = inv(matrix(A))

        t2 = perf_counter()

        dt = t2 - t1

        size = 4*(N**2)*8

        dts.append(dt)  #agrego tiempos a la lista dts
        mem.append(size) #agrego memoria utilizada a la lista mem

        fid.write(f"{N} {dt} {size} \n") #Escribo resultados en el archivo de texto correspondiente

        print(f"Tiempo transcurrido = {dt} s")
        print(f"Memoria usada = {size} bytes")

        fid.flush()

    fid.close()


#lectura de archivos para graficar
plt.figure()
for a in range(Ncorridas):

    name = open(f"caso_1_double{a}.txt", "r")      #!!!
    Xaxis = []
    Ytime = []
    Ymemory = []
    lines = []

#obtención de datos de cada linea de los archivos
    for line in name.readlines():
        x = line.strip("\n")
        y = x.split(" ")
        y.pop(3)
        z = [float(a) for a in y]
        lines.append(z)

    for b in lines:
        Xaxis.append(int(b[0]))
        Ytime.append((b[1]))
        Ymemory.append(int(b[2]))

    #formato y diseño del gráfico 1
    plt.subplot(2, 1, 1)
    plt.grid(b=True)
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Rendimiento Inv (caso 1 double)")     #!!!
    plt.ylabel("Tiempo Transcurrido")
    plt.plot(Xaxis, Ytime, "-o")

    plt.xticks((10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000),
               (" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "))
    plt.yticks((0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600),
               ("0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 m", "10 m"))

    #formato y diseño del gráfico 2
    plt.subplot(2, 1, 2)
    plt.grid(b=True)
    plt.xscale("log")
    plt.yscale("log")
    plt.ylabel("Uso Memoria")
    plt.xlabel("Tamaño de la Matriz")
    plt.plot(Xaxis, Ymemory, "-ob")

    plt.xticks((10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000),
               ("10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000", "20000"), rotation=50)
    plt.yticks((1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000),
               ("1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"))

plt.show()