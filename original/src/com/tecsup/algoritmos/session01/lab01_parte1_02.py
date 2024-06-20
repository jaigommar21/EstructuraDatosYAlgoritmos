'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
Version : 1.0
Date : 20/03/2023
'''

from graph  import draw
from timeit import default_timer as timer

## Nested Loops : 

## Guia de laboratorio

from timeit import default_timer as timer

n=10**3
start=timer()
for i in range(0,n):
    for j in range(0,n):
        print(f"i = {i} and j = {j} ")
        #pass
end=timer()
proc_time=end-start
print(f"Processing time -> {proc_time}")


exit(-1)

## Solucion : Guia de laboratorio

#"""
list_nro_input = [1, 10, 100, 200, 400, 600, 800, 1000, 1200, 1400]    
results = {}
for n in list_nro_input:
    start = timer()
    for i in range(0,n):
        for j in range(0,n):
            pass
            #print(f"i = {i} and j = {j} ")
    end = timer()
    delay = end - start
    results[n] = delay 
    print(f"n = {n} ,time = {delay}")

for key, value in results.items():
    print( f"key={key:7}  value={value}")

# Show graph 
draw(results.keys(),results.values(),'green','Nested Loops', 'Iteractions', 'Time(s)')

