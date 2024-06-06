# Notación Big O

### Descripción
En este proyecto se realizara la comparación de tiempos de ejecución de diferentes algoritmos, los cuales tienen un diferente comportamiento en cuanto al **análisis "Big O"**.
Este último representa la complejidad del peor de los casos de un algoritmo.

## Como ejecutar

Utilizaremos el lenguaje Python para realizar los algoritmos, por lo cual debes tener instalado Python en tu ordenador y luego debes instalar las librerías que utlizaremos de la siguiente forma:

```
pip install matplotlib
```
```
pip install numpy
```
Por último, solo debes ejecutar el proyecto:
```
python index.py
```
## Partes - Descripción del Código

### Funciones

- Algoritmo Constante O(1) - **constant_algorithm**
- Algoritmo Logarítmico O(log n) - **binary_search**
- Algoritmo Lineal O(n) - **linear_search**
- Algoritmo Linealítmetica O(n log n) - **merge_sort**
- Algoritmo Cuadrático O(n^2) - **bubble_sort**
- Algoritmo Exponencial O(2^n) - **fibonacci**

Luego tenemos una función llamada **measure_time** para medir el tiempo de ejecución.

### Variable de entrada

Para ejecutar las funciones, primero debemos pasar como argumento una lista de numeros crecientes del 1 hasta "n".
```
n = 20
```
Este último indíca que tan grande será la lista. Actualmente tiene el valor de 20, pero puedes cambiar el mismo si deseas trabajar con otra dimension de la lista.
Cabe aclara que cada valor de la lista, representa las veces que se ejecutara la función, es decir, si tenemos una lista = [1,2,3], la función primero funcionara una vez, luego dos veces, luego tres veces y cada tiempo de ejecución sera registrado en la lista resultado que nos brinda la función **measure_time**.

### Parte donde ejectuamos y graficamos los resultados

Luego ya tenemos la parte donde ejecutamos cada función y sus resultados son usados para realizar el grafico en donde se podrá apreciar la comparación en sus rendimientos.

## Recomendaciones

Si vas a ejecutar todas las funciones te recomiendo que la variable de ingreso **"n" no sea mayor a 20** ya que la función Exponencial llamada **fibonacci** tiene un tiempo de ejecución de (2^n) y acomparación de las otras, se torna mucho mas lenta con un valor de **"n"** muy grande.
Puedes comentar la ejecución de dicha función como así tambien su grafica, de esta manera podras comparar los tiempos de las otras funciones con un numero de **"n"** más grande.
