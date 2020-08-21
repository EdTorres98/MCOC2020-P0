# MCOC2020-P0

# Mi computador principal

* Marca/modelo: MacBookPro9,2
* Tipo: Notebook
* Año adquisición: 2016
* Procesador:
  * Marca/Modelo: Intel Core i5-3210M
  * Velocidad Base: 2.50 GHz
  * Velocidad Máxima: 3.10 GHz
  * Numero de núcleos: 2
  * Numero de hilos: 4
  * Arquitectura: x86_64
  * Set de instrucciones: Intel AVX
* Tamaño de las cachés del procesador
  * L1d: 64KB
  * L1i: 64KB
  * L2: 256KB
  * L3: 3072KB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad 1600 MHz
  * Numero de (SO)DIMM: 4
* Tarjeta Gráfica
  * Marca / Modelo: Intel HD Graphics 4000
  * Memoria dedicada: 1536 MB
  * Resolución: 1280 x 720
* Disco 1: 
  * Marca: Apple
  * Tipo: SATA
  * Tamaño: 500GB
  * Particiones: 2
  * Sistema de archivos: APFS, NTFS
  
* Dirección MAC de la tarjeta wifi: A4:D1:8C:65:E7:B6
* Dirección IP (Interna, del router): 192.168.18.15
* Dirección IP (Externa, del ISP): 170.82.191.224
* Proveedor internet: Pacifico Cable

# Desempeño MATMUL

![Gráfico](https://user-images.githubusercontent.com/69275311/89700720-7d145a00-d8fe-11ea-88bc-e37b907ef8e4.png)

* ¿Como difiere del gráfico del profesor/ayudante? 
  * En el gráfico de tiempo transcurrido difiere al inicio, ya que para una corrida el tiempo de la primera matriz fue relativamente bajo y para las otras este se elevó cerca de los 0.1s siendo similar al mostrado en el ejemplo. Posteriormente para la última matriz esta se ejecutó cercano a 1s, en diferencia de los 10 segundos mostrados en el ejemplo. Por otro lado el gráfico de uso de memoria es relativamente muy similar al mostrado en el enunciado.

* ¿A qué se pueden deber las diferencias?
  * Al tipo de procesador que se utiliza y a los procesos que se están ejecutando a la misma vez mientras el código está corriendo.
  
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser? 
  * Por un lado el uso de la memoria es lineal ya que a medida que aumenta el tamaño de la matriz que se va utilizando el uso de la memoria también lo hará, por ende si se utiliza en orden creciente, ocurrirá este efecto lineal en el uso de memoria. En cambio el tiempo trnascurrido no lo es, y solo se verá una tendencia a ser lineal en un cierto rango, ya que dependerá de los procesadores que se usarán, en un inicio al haber mas procesos utilizados, estos se irán aminorando como se observa, para luego comenzar a utilizarlos de forma creciente mientras el código sigue corriendo.
  
* ¿Qué versión de python está usando?
 * Python 3.8

* ¿Qué versión de numpy está usando?
 * Numpy 1.19.1

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
 * Sí, se utiliza más de un procesador para la ejecución del código.
 
  ![Captura de Pantalla 2020-08-07 a la(s) 22 57 01](https://user-images.githubusercontent.com/69275311/89701053-aa163c00-d901-11ea-9214-624a84d35450.png)

# Desempeño MIMATMUL

![Gráfico](https://user-images.githubusercontent.com/69275311/89853274-fca06400-db5e-11ea-8ff4-a9447caf243b.png)

* ¿Como difiere del gráfico del profesor/ayudante? 
  * En este caso los gráficos son similares, pero esta vez en el gráfico del tiempo transcurrido no se generan peaks o un comportamiento no lineal como ocurría anteriormente. Esta vez se graficó hasta un N=200 ya que al utilizar los valores de MATMUL se demoraba 1 hora para lograr correr un archivo.

* ¿A qué se pueden deber las diferencias con MATMUL?
  * Se debe a que al utilizar en este caso una función realizada en python puro, los procesadores no trabajarán de la misma manera y en la misma cantidad como ocurría con MATMUL, ya que ahora se realiza en un alto nivel, a diferencia de la multiplicación realizada anteriormente donde era mucho más cercana a un bajo nivel, generando que los procesadores trabajaran de manera más efectiva, por ende, en menor tiempo. En este caso ambos gráficos son relativamente lineales como se observan, ya que en el proceso de generar cada matriz iba tardabando mucho más a medida que aumentaba el N.

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
 * Para MIMATMUL los procesadores que corrían eran más bajos, haciendo que trabajaran los núcleos con un menor desempeño, lo que se traduce en lo que tardaba el programa en terminar de correr a comparación de MATMUL.
 
![Captura de Pantalla](https://user-images.githubusercontent.com/69275311/89854950-3ecba480-db63-11ea-9d4b-5bdd0d3918f7.png)

# Desempeño de INV
    
 * Caso 1: Numpy.linalg.inv
   - Analizando el desempeño de single y double es muy similar a diferencia de un peak que ocurre entre N=10 y N=20.
   - En cuanto al procesador, este utilizó valores cercanos al 40% para ambos, por lo que trabajaba a menos de la mitad del total de su capacidad.
   - Para las matrices de N = 2000, en ambos tipos de datos se obtuvo un tiempo cercano a 1s y con una memoria utilizada aprox de 100 MB.   
   - Para este caso no se utilizaron "half" ni "loungdouble" ya que no eran compatibles con numpy.linalg.
    
   - Los gráficos obtenidos para cada tipos de datos analizados son los siguientes:
    
   ![Captura de Pantalla 2020-08-12 a la(s) 23 00 11](https://user-images.githubusercontent.com/69275311/90089522-9b5bca80-dcef-11ea-8f85-d1efd652c50c.png)

 * Caso 2: Nscipy.linalg.inv, overwrite=False
   - Para las matrices de N = 2000, en el caso de single y half, ocurren con tiempos muy similares, pero half utiliza menos memoria no llegando a 100MB como sí ocurre con single.
   - Por otro lado para el caso de double y longdouble con N=2000 transcurren en tiempos similares utilizando casi la misma memoria de 100MB.  
   - En cuanto al procesador, este utilizó valores cercanos al 60%, por lo que trabaja a mayor capacidad que el caso anterior.  
   - Se puede apreciar que con loungdouble el comportamiento es mucho más lineal que con los otros tipos. 
   
   - Los gráficos obtenidos para cada tipos de datos analizados son los siguientes:
    
   ![merge_from_ofoct](https://user-images.githubusercontent.com/69275311/90090019-e9250280-dcf0-11ea-967b-af50accc0e2d.jpg)

 * Caso 3: scipy.linalg.inv, overwrite=True
   - Para las matrices de N = 2000, en el caso de single y half, ocurren con tiempos muy similares, pero half utiliza menos memoria no llegando a 100MB como sí ocurre con single.
   - Por otro lado para el caso de double y longdouble con N=2000 transcurren en tiempos similares utilizando en este caso loungdouble un valor superior a 100MB. 
   - En cuanto al procesador, este utilizó valores cercanos al 75%, por lo que trabaja a mayor capacidad que el caso anterior, lo que se puede deber a que ahora se utiliza overwrite=True.  
   - Se puede apreciar que con double y loungdouble el comportamiento es mucho más lineal que con los otros tipos, no generandose peaks en algunos tramos. 
   
   - Los gráficos obtenidos para cada tipos de datos analizados son los siguientes:
    
   ![Captura de Pantalla 2020-08-12 a la(s) 23 18 32](https://user-images.githubusercontent.com/69275311/90090515-35bd0d80-dcf2-11ea-9b4d-9f8718800f79.png)
   
+ Análisis de los gráficos obtenidos
   + Observando los datos otorgados en los gráficos se puede apreciar que al obervar N=2000 en los tipos de datos, que single y half utilizan menos tiempos para ejecutarse, alrededor de 0.1s,  pero ambos con mayores utilidades de memoria que son entre 10MB y 100MB. Po Por otro lado 
   double y lungdouble se ejecutan cercanos al tiempo de 1seg y ambos con memorias utilizadas cercanas a 100MB. Por lo que se puede concluir que los tipos d edatos half son los más optimos al trbajaro con ellos ya que se ejecutan en un tiempo inferior y utilizan mcha menos memoria en comparación a los otros 3. Double y longdouble se comportan casi de la misma manera al ser ejecutados.
   
+ ¿Qué algoritmo de inversión cree que utiliza cada método?

  + Para numpy.linalg, se puede determinar que utiliza descomposición Cholesky, ya que necesita mucha más memoria al correr el programa por lo que tarda mucho más si itulizaramos scipy.
  + Para scipy.linalg, se puede determinar que utiliza Cayley-Hamilton, ya que para el desarrollo de este código se utiliza solo la Matriz A durante todo momento, haciendo que este método sea algo más rápido que el anterior.
  
+ ¿Cómo incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso?

  +Al observar los 3 casos analizados, en todos se repite el factor de que double y longdouble que se comportan de alguna de manera linea, lo que no ocurre con single y hand, el los cuales existen peaks en lagunos tramos. Ocurre lo mismo si analizamos cada caso por sepradado, siendo el Caso 2 donde se observan más peaks. Por lo tanto la estructura de caché en este caso venía utilizada utilizando más memoria y repartiendo esta caché, lo que generó los peaks al pasar al siguiente caso (2). En el caso del paralelismo al estar utilizando el procesador para otros procesos, esto genera que el tiempo aumente al ejecutar el código, y también ocurre que luego del caso 2 el comportamiento fue práctimanente linear, ya que estos se encontraban trabajando desde antes, mejorando su productividad y velocidad.
  
 # Desempeño Ax=b
 
 ![Gráfico](https://user-images.githubusercontent.com/69275311/90453135-c3677700-e0bd-11ea-808f-860cbda616ff.png)
  + En primer lugar para analizar el desempeño de Ax=b se realizaron 10 corridas para obtener los promedios, con N desde (2 a 10000)
  + Para los solvers del sistema se utilizaron, inv(), npSolve, spSolve(sym, pos, pos_overwrite)
  + De este gráfico se puede concluir que el np(numpay) desde el inicio hasta N=100 fue el más rápido de todos, llegando hasta aprox 1ms, seguido por inv() y los demás muy similares en los tiempos que de tardaron.
  + Luego para N>200 spSolve(pos_overwrite) fue el más rápido y eficaz al momento de dar las resoluciones, donde se vé una leve intersección en N=10000 entre sym y pos, por lo que para un N>10000 es posible que uno de estos se convierta en el más eficaz para el desarrollo, aunque al definirle que es una matriz simétrica y def. positiva puede que se mantenga ya que los cáculos realizados internamente se van optimizando y ahórrando ejecutar más cálculos para llegar a la solución, como ocurre con los demás métodos.
  + En cambio para inv() luego de N>80 se mantiene dentro del más lento, infiriendo que es más cercano un alto nivel, además de utilizar solamente el método clásico de la invertida.
  + Finalmente spSolve y spSolve sym se mantienen muy iguales desde el inicio hasta el final, por lo que su comportamiento y desempeño es similar.

# Matrices dispersas y complejidad computacional

 + Complejidad algoritmica de MATMUL
 
 ![MATMUL matriz llena](https://user-images.githubusercontent.com/69275311/90937924-db007180-e3d5-11ea-97f8-40dc43d15643.png)
 ![MATMUL matriz dispersa](https://user-images.githubusercontent.com/69275311/90937966-f23f5f00-e3d5-11ea-862c-6356c0620a24.png)
 
  + En el caso de la matriz dispersa, tiene tiempos de ensamblado mayores y un comportamiento menos lineal que la matriz llena, ya que se generan diversos peaks, no ocurriendo lo mismo para los tiempos de solución, donde la matriz llena demora más en generar las soluciones para N mayores, pero genera un comportamiento mucho más lineal. Sin contar que al inicio se genera lo mismo que se venía viendo anteriormente, donde el procesador necesita adaptarse para comenzar a generar ese comportamiento lineal, no siendo asi en el caso de la matriz dispersa, donde comienza sin ese peak inicial.
  + La complejidad asintótica para el ensamblado es N2, tanto para la matriz dispersa y la matriz llena, esto se produce, por que al ir duplicando la matriz en términos de una de sus diagonales, el tiempo se irá cuadruplicando para generar el ensamblado de las matrices.
  + La complejidad asintótica para la solución es N3, tanto para la matriz dispersa y la matriz llena, esto se produce, por que al ir duplicando la matriz en términos de una de sus diagonales, el tiempo en este caso se irá octuplicando para generar las soluciones.
  + En referencia a los tamaños de las matrices se utilizó N=10000 como máximo, ya que para N mayores el programa se congelaba, o demoraba mucho tiempo. En cuanto a los comportamientos se puede observar que la matriz dispersa tiene un comportamiento inicial más constante, sin ir aumentando los tiempos de solución o ensablado, ya que al no ir guardando el trabajo anterior y además no multiplicando todos los términos, ya que si la matriz tiene muchos ceros, no los tomará en cuenta, lo que optimiza el tiempo durante un rango de N, y verificando que para N mayores, los tiempo son mucho menores que una matriz llena.
  + Las corridas para el caso de la matriz dispersa se pueden apreciar con más peaks para N<1000, pero luego comienza a tener un comportamiento más lineal (o sub-lineal), en cambio para la matriz llena solo se observa el peak inicial (que se comentó anteriormente) para luego ir subiendo linealmente hasta tener una tendencia a un N.
  + Cabe destacar que en el gráfico no se ven los N2, N3, N4 de manera lineal, por la dispersión que hay en un inicio, ya que se utilizaron más valores para las corridas realizadas, y había que volver a generar los archivos de texto.
  
