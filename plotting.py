import scipy as np
import matplotlib.pyplot as plt

Ncorridas = 10

plt.figure()
#lectura de archivos para graficar
for a in range(Ncorridas):

    name = open(f"matmul{a}.txt", "r")
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
    plt.title("Rendimiento A@B")
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