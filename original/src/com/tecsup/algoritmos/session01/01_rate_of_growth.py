'''
Tienes un algoritmo que se
denota por la funcion f(n)
, donde n es la cantidad
de datos


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


if __name__ == "__main__":
    n = 1
    print("Tiempo = {} seg".format(f(n)))
    


'''
#    4 
#   n  
def cal_ecuation_aprox(n):
    f = n**4
    return f


if __name__ == "__main__":
    
    n = 1
    exact = cal_ecuation_exact(n) 
    aprox = cal_ecuation_aprox(n)  
    delta = exact - aprox
    print(exact)
    print(delta)

    print("-"*50)

    n = 10
    exact = cal_ecuation_exact(n) 
    aprox = cal_ecuation_aprox(n)  
    delta = exact - aprox
    print(exact)
    print(delta)

    print("-"*50)

    n = 100
    exact = cal_ecuation_exact(n) 
    aprox = cal_ecuation_aprox(n)  
    delta = exact - aprox
    print(exact)
    print(delta)

    print("-"*50)

    n = 1000
    exact = cal_ecuation_exact(n) 
    aprox = cal_ecuation_aprox(n)  
    delta = exact - aprox
    print(exact)
    print(delta)
'''