'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
Version : 1.0
Date : 20/03/2023
'''

from graph  import draw
from timeit import default_timer as timer

# Ejercicio 02

#"""
list_nro_input = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]    
results = {}
for n in list_nro_input:
    start = timer()
    for i in range(0,n):
        for j in range(0,n):
             for k in range(0,n):
                pass
                #print(f"i = {i} and j = {j} and k = {k}")
    end = timer()
    delay = end - start
    results[n] = delay 
    print(f"n = {n} ,time = {delay}")

for key, value in results.items():
    print( f"key={key:7}  value={value}")

# Show graph 
draw(results.keys(),results.values(),'green','Nested Loops', 'Iteractions', 'Time(s)')


