'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
Version : 1.0
Date : 20/03/2023
'''

from graph  import draw
from timeit import default_timer as timer

# If then else statements: 


## Guia de laboratorio

from timeit import default_timer as timer

n=10**3
start=timer()

if n == 1 :
    print("Wrong value")
    print(f"{n}")
else :
    for i in range(0,n):
        print(f"idx={i}")
        #pass
    
end=timer()
proc_time=end-start
print(f"Processing time -> {proc_time}")


exit(-1)

## Solucion : Guia de laboratorio


#"""
#list_nro_input = [1,10,100,1000,10000,25000,50000,75000,100000]    
list_nro_input = [1,10,100,1000,
                  1*10**4,int(2.5*10**4),5*10**4,int(7.5*10**4),
                  1*10**5,int(2.5*10**5),5*10**5,int(7.5*10**5)]    
results = {}
for n in list_nro_input:
    start = timer()
    
    if n == 1 :
        print("Wrong value")
        print(f"{n}")
    else :
        for i in range(0,n):
            pass
            #print(f"idx={i}")

    end = timer()
    delay = end - start
    results[n] = delay 
    print(f"n = {n} ,time = {delay}")

for key, value in results.items():
    print( f"key={key:7}  value={value}")


# Show graph 
draw(results.keys(),results.values(),'green','If-then-else', 'Iteractions', 'Time(s)')

#"""

