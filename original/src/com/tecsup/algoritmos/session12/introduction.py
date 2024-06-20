# Binary Search Tree
#
#          5
#        /  \
#       /    \
#     3        7
#    /  \     / \
#   2    4   6   8
#

# Binary Search Tree
#
#            5
#          /  \
#         /    \
#       4        6
#      /          \
#     3            7
#    /              \
#   2                8

#  4,8,12,17,100   --> 4,17,12,8,100

#  4,17,12,8,100

#  Paso 1 : Crear un nodoBST(4)
#  Paso 2 : Seleccionar el siguietne valor 17
#  Paso 3 : Si es menor, creo el nodoBST(17) 
#           y lo coloco a la izquierda
#           Si es mayor a la izquierda 
#  Paso 4 : Selecciono el siguiente valor 8
#  Paso 5 : Buscar el 8 en forma recursiva
#           , si no existe y ahi lo creas
#           aplicas el concepto del paso 3     
#  Paso 6 : 
#
#            4
#                   17
#                12   100
#              8 

nros = [19,244,199]

def obtener_maximo(nros, debug = False):
    m = max(nros)
    if debug:
        print(m)
    return m

obtener_maximo(nros)

""" x = max(nros)
print(x)
 """

#print(nros.index(244))


""""

   x --> f(x) --> retorna algo

   x  --> f(x) : 4x+3 --> 
   1                       7
   2                       11

   No ingreso nada --> f() --> retorna algo 

   No ingreso nada --> f() --> No retorna nada

"""


""" def func1():
    x = 1+2

def func2(n):
    m = n + 4

def func3(m):
    m = m + 4
    #print(m)
    return m 

def func4():
    return 45

func1()
r1 = func1()   # None
print(r1)
func2(12)
r2 = func2(12) # None
print(r2)

func3(3)

r3 = func3(3)   
if f3 > 19 :
    print(f3)


r4 = func4()   
print(r4)

  func_alto
  func_medias
  func_basicas """


def agregar_referencia(l,valor):
    l.append(valor)

def agregar_sobreescribiendo(l,valor):
    l.append(valor)
    return l


listado = [4,5]
agregar_referencia(listado, 8)
print(listado)

listado = [4,5]
listado = agregar_sobreescribiendo(listado, 8)
print(listado)


i = True
print(type(i))
print(str(i))