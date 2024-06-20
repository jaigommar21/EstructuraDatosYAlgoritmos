# PREGUNTA 1
"""
from timeit import default_timer as timer
import sys
from graph  import draw

# Factorial function
def factorial(n):
    if n == 0: 
        return 1
    else:
        return n*factorial(n-1)


# Using
if __name__ == "__main__":
    times = []
    sys.setrecursionlimit(3600)    
    list_nros = [1,2,4,8,16,32,64,128,256,512,768,1024,1280,1536,1792, 2048 ,2304,2560,2816,3072,3328,3584]
    for nro in list_nros :
        #print(nro)
        time_inicial =  timer() 
        fac = factorial(nro)
        #print(fac)  
        time_final = timer() 
        times.append(time_final - time_inicial)
        print(times)

    # Show graph 
    draw(list_nros,times,'g','Factorial vs Processing Time', 'Number', 'Time(s)')





#"""

# PREGUNTA 3

#### LANZAR UN DADO

#### for i in range(2,13):
####    print("suma de 2 dados ", i)

#### con 1 bit cuantas combinaciones se puede hacer?
#### con 2 bits cuantas combinaciones se puede hacer?


#"""
# Using
if __name__ == "__main__":

    #numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    numeros  = [ i for i in range(1001)]
    print(numeros)
    #for n in numeros:
    #    print(n)

#"""






