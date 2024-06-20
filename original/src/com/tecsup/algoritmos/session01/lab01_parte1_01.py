'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
Version : 1.1
Date : 28/02/2024
'''

## Loops : 

## Guia de laboratorio

"""
from timeit import default_timer as timer

n=10**3
start=timer()
for i in range(0,n):
    print(f"I = {i}")
    #pass
end=timer()
proc_time=end-start
print(f"Processing time -> {proc_time}")


#exit(-1)
"""

## Solucion : Guia de laboratorio

from graph  import draw
from timeit import default_timer as timer


#"""
list_nro_input = [1,10,100,1000,
                  1*10**4,int(2.5*10**4),5*10**4,int(7.5*10**4),
                  1*10**5,int(2.5*10**5),5*10**5,int(7.5*10**5)]    
results = {}
for n in list_nro_input:
    start = timer()
    for i in range(0,n):
        print(f"idx={i}")
        #pass
    end = timer()
    delay = end - start
    results[n] = delay 
    print(f"n = {n} ,time = {delay}")

for key, value in results.items():
    print( f"key={key:7}  value={value}")


# Show graph 
draw(results.keys(),results.values(),'red','Loops', 'Iteractions', 'Time(s)')

#"""

