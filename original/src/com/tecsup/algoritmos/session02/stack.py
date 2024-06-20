'''

'''


def despedirse():
    print("Hasta la vista baby..!")

# Recursividad
def imprimir(msg, ns):
    if ns == 0: # Base case
        despedirse()
        return
    else:
        print("nro={}, message={}".format(ns,msg))
        ns = ns - 1
        imprimir(msg, ns)

# Iteraccion
def imprimir2(msg, ns):
    for i in range(ns):
        print("nro={}, message={}".format(i,msg))


if __name__ == "__main__":
    nro_saltos = 10000  # Conocer el concepto de pila
    #imprimir("Hello world...!", nro_saltos)
    imprimir2("Hello world...!", nro_saltos)
