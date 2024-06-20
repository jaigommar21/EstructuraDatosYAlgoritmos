"""
Curso :
Tema : Introduccion a la recursividad


"""



def imprimir2(msg):
    print(msg)

def imprimir(msg):
    imprimir2(msg)

def imprimir3(msg):
    print(msg)
    imprimir3(msg)

def imprimir4(n):
    
    if n == 0 :  # base case
        return
    else:
        print(n)
        imprimir4(n-1)

if __name__ == "__main__":
    
    # recursividad
    #imprimir4(100


    # iteraccion
    for n in range(100):
        imprimir2(100-n)

"""
# Llamada recursiva infinita
def imprimir(msg):
    print(msg)
    imprimir(msg)


if __name__ == "__main__":
    imprimir("Hello World ..!")
"""

"""

# Llamada recursiva FINITA
def imprimir(msg, counter):
    print(msg)
    counter = counter - 1
    if counter>0:  # BASE CASE
        imprimir(msg,counter)

def imprimir3(msg, counter=0):
    print(msg)

if __name__ == "__main__":

    # PROGRAMACION RECURSIVA
    imprimir("REC : Hello World ..!",10)

    # PROGRAMACION ITERACTIVA
    for i in range(10):
        imprimir3("ITE : Hello World ..!")
"""
