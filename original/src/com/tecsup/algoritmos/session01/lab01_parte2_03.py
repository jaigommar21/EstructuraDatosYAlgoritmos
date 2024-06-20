'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
Version : 1.0
Date : 292/02/2024
'''

from graph  import draw
from timeit import default_timer as timer

# Ejercicio 07

#"""

def function(n): 
    count = 0
    for i in range(int(n/2),n):
        j = 1
        while j + n/2  <= n: 
            break
        j = j * 2
        print(count)
            #pass

function(20)

#1,5,10,50,100,500,1000,5000,10000,50000,100000

#list_nro_input = [10**i for i in range(0,8)]        

list_nro_input = [1,5,10,50,100,500,1000,5000,10000,50000,100000]
results = {}

for n in list_nro_input:
    start = timer()
    function(n)
    end = timer()
    delay = end - start
    results[n] = delay 
    print(f"n = {n} ,time = {delay}")

for key, value in results.items():
    print( f"key={key:7}  value={value}")


# Show graph 
draw(results.keys(),results.values(),'green','Logarithms', 'Iteractions', 'Time(s)')

#"""

