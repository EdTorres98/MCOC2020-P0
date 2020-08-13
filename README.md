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
    
   # Caso 1: Numpy.linalg.inv
   - Analizando el desempeño de single y double es muy similar a diferencia de un peak que ocurre entre N=10 y N=20.
   - En cuanto el procesador utilizó valores cercanos al 40% para ambos, por lo que trabajaba a menos del total de su capacidad.
   - Para las matrices de N = 2000, en ambos tipos de datos se obtuvo un tiempo cercano a 1s y con una memoria utilizada aporx de 100 MB.   
   - Para este caso no se utilizaron "half" ni "loungdouble", ya que no eran compatibles con numpy.linalg.
    
   - Los gráficos obtenidos para cada tipos de datos analizados son los siguientes:
    
   ![Caso 1 Single](https://user-images.githubusercontent.com/69275311/90087522-035be200-dceb-11ea-9222-330354244140.png)
   ![Caso 1 Double](https://user-images.githubusercontent.com/69275311/90087544-12429480-dceb-11ea-8654-ea781788d53c.png)
