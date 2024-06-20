'''
Tienes un algoritmo, que el tiempo de ejecución
esta definido por la funcion f(n), donde n es la 
cantidad de datos

"n" datos
           --------
    ----> |   A    |  --->
           --------
         tiempo de ejecución = f(n)

         4     2
f(n)  = n  + 2n + 100n + 500

'''


#    4     2
#   n  + 2n  + 100n + 500
def f(n):
    t = n**4 + 2*(n**2) + 100*n + 500
    return t

def g(n):
    t = n**4
    return t


if __name__ == "__main__":
    '''
    for n in range(1,4):
        print("Tiempo f({}) = {} seg".format(n,f(n)))
    '''

    list_nro_input = [1,10,100,1000,10000 ]
    
    for n in list_nro_input:
        print("-"*40)
        # f(t)    
        print("Tiempo f({}) = {} seg".format(n,f(n)))
        # g(t)   
        print("Tiempo g({}) = {} seg".format(n,g(n)))
        # delta = f(t)-g(t)
        # variacion = ( delta/f(t) ) * 100
        variacion = ((f(n)-g(n))/f(n))*100
        print("Variacion = {} %".format( round(variacion,3) ) )
        
