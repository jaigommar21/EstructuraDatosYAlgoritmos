
from timeit import default_timer as timer

if __name__ == "__main__":



    '''
    # ------------- Loops -----------
    # Total time : C * n ==>  Cn = omega(n)
    
    nro_inputs = [1,10,100,1000,10000,100000]
    times_exec = []
    n = 100000

    for n in nro_inputs:
        start = timer()
        # Analise the for 
        for i in range(0,n):
            #pass
            print ("i={}".format(i))
        end = timer()
        delay = end - start
        times_exec.append(delay)
        print("Time {}".format(delay))

    print("Times: {} ".format(times_exec))
    #'''


    # ------------- Nested Loops -----------
    # Total time : C * n * n ==>  Cn^2 = omega(n^2)

    nro_inputs = [1,10,100,1000,10000] # WARNING, WITH 10000 CRASH THE SYSTEM 
    times_exec = []
    n = 100000

    for n in nro_inputs:
        start = timer()
        # Analise the for 
        for i in range(0,n):
            for j in range(0,n):
                print (f"i={i}; j={j}")
        end = timer()
        delay = end - start
        times_exec.append(delay)
        print(f"Time {delay}")

    print(f"Times: {times_exec} ")
    

    '''
    # ------------- Nested Loops -----------
    # Total time : C * n * n ==>  Cn^2 = omega(n^2)
    for i in range(0,n):
        for j in range(0,n):
            print ("i={}; j={}".format(i,j))

    # ------------- Consecutive statements -----------
    # Total time :  C1 + C2 * n  +  C3 * n * n ==> omega(n^2)     
    
    n = 100 
    
    for i in range(0,n):
        print ("i={}".format(i))
    
    for i in range(0,n):
        for j in range(0,n):
            print ("i={}; j={}".format(i,j))

    # ------------- If-then-else statements -----------
    # Total time :  C1 + C2 * n  ==> omega(n)     

    if n == 1 :
        print(n)
    else:
        for i in range(0,n):
            print(i)


    # ------------- Logarithm Complexity -----------
    # Total time :  C1 + C2 * n  ==> omega(n)     
    
    def logarithms(n): 
        i=1
        while i <= n: 
            i= i * 2 
            print(i)

    logarithms(100)
    
    
    '''