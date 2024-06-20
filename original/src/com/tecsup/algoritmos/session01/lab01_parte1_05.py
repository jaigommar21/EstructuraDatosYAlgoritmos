'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
Version : 1.0
Date : 20/03/2023
'''

from graph  import draw
from timeit import default_timer as timer

# Logarithmic complexity: 



## Guia de laboratorio

from timeit import default_timer as timer

def logarithms(n): 
    i = 1
    while i <= n: 
        i = i * 2 
        print(i)
        #pass
        
n=10**3

start=timer()
logarithms(n)    
end=timer()

proc_time=end-start
print(f"Processing time -> {proc_time}")


exit(-1)

## Solucion : Guia de laboratorio


#"""






list_nro_input = [10**i for i in range(0,25)]        
results = {}

for n in list_nro_input:
    start = timer()
    logarithms(n)
    end = timer()
    delay = end - start
    results[n] = delay 
    print(f"n = {n} ,time = {delay}")

for key, value in results.items():
    print( f"key={key:7}  value={value}")


# Show graph 
draw(results.keys(),results.values(),'green','Logarithms', 'Iteractions', 'Time(s)')

#"""

