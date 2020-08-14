import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def plotting(names):

    xtks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

    ytks1 = [0.1e-3, 1e-3, 1e-2, 0.1, 1., 10., 60, 68*10]
    ytklabs1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

    plt.figure()

    for name in names:

        data = np.loadtxt(name)
        Ns = data[:, 0]
        dts = data[:, 1]

        print("Ns: ", Ns)
        print("dts: ", dts)

        plt.loglog(Ns, dts.T,"-o", label=name)
        plt.ylabel("Tiempo transcurrido (s)")
        plt.xlabel("Tamaño matriz $N$")
        plt.grid(True)
        plt.xticks(xtks,xtks, rotation=45)
        plt.yticks(ytks1, ytklabs1)

    plt.tight_layout()
    plt.legend()
    plt.show()

names = ["A_invB_inv.txt", "A_invB_npSolve.txt"]
plotting(names)