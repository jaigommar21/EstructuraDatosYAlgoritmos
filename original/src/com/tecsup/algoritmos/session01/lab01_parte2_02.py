'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
Version : 1.0
Date : 20/03/2023
'''

from graph  import draw
from timeit import default_timer as timer

# Ejercicio 07

#"""

def function(n): 
    count = 0
    for i in range(n//2,n):
        j = 1
        while j + n/2  <= n: 
            k = 1
            while k  <= n: 
                count = count + 1
                k = k * 2
            j = j + 1
        print("*",count)
        #pass
        
function(20)


list_nro_input = [10**i for i in range(0,4)]   
list_nro_input = [1,5,10,50,100,250,500,750,1000,2500,5000,7500,10000] # with pass
list_nro_input = [1,5,10,50,100,250,500,750,1000,2500,5000,7500] # without pass

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

