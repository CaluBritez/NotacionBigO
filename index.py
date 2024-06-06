import time
import matplotlib.pyplot as plt
import numpy as np

# Algoritmo Constante O(1)
def constant_algorithm(arr):
    return arr[0]

# Algoritmo Logarítmico O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Algoritmo Lineal O(n)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Algoritmo Linealítmetica O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Algoritmo Cuadrático O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Algoritmo Exponencial O(2^n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Función para medir el tiempo de ejecución de una función
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Tamaños de entrada
n = 20
#Creamos una lista de numeros de manera creciente hasta alcanzar n
sizes = np.arange(1, n+1)

# Medir tiempos de ejecución
constant_times = [measure_time(constant_algorithm, list(range(n))) for n in sizes]
binary_times = [measure_time(binary_search, list(range(n)), n // 2) for n in sizes]
linear_times = [measure_time(linear_search, list(range(n)), n // 2) for n in sizes]
merge_sort_times = [measure_time(merge_sort, list(range(n))) for n in sizes]
bubble_sort_times = [measure_time(bubble_sort, list(range(n))) for n in sizes]
fibonacci_times = [measure_time(fibonacci, n) for n in sizes]

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(sizes, constant_times, label='O(1) - Constante')
plt.plot(sizes, binary_times, label='O(log n) - Logarítmica')
plt.plot(sizes, linear_times, label='O(n) - Lineal')
plt.plot(sizes, merge_sort_times, label='O(n log n) - Linealítmetica')
plt.plot(sizes, bubble_sort_times, label='O(n^2) - Cuadrática')
plt.plot(sizes, fibonacci_times, label='O(2^n) - Exponencial')

plt.yscale('log')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de la Complejidad de Algoritmos')
plt.legend()
plt.grid(True)
plt.show()
