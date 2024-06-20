class Heap:

    def __init__(self, heapList = []):
        self.heapList = heapList
        self.size = len(heapList)

    def parentIndex (self , index ):
        return (index -1)//2

#         max - heap
#
#            10
#        3        9
#     1    2    7   8
#
#            10[0]
#      3[1]         9[2]
#  1[3]   2[4]  7[5]     8[6]
#
#         0  1  2  3  4  5  6
array = [10, 3, 9, 1, 2, 7, 8]
x = Heap(array)


valor1 = x.parentIndex(1) # parent 0 
valor2 = x.parentIndex(3) # parent 1
valor3 = x.parentIndex(5) # parent 2
print (valor1)
print (valor2)
print (valor3)

'''
TÉCNICA : Eliminar el primer elemento
          o atender el primer elemento

[10, 3, 9, 1, 2, 7, 8]

paso 1 : atiendo al mayor que en ese caso es el 10
[X, 3, 9, 1, 2, 7, 8]

paso 2 : reemplazar el último elemento a la primera 
         posición
[8, 3, 9, 1, 2, 7, 8]

paso 3 : eliminar última posición
[8 , 3, 9, 1, 2, 7]

paso 4 : aplicar el percolate down
¿Cuál es la salida?
[????????]
'''

#         max - heap
#
#            8
#        3        9
#     1    2    7   

#            9
#        3        8
#     1    2    7   

[9 , 3, 8, 1, 2, 7]
