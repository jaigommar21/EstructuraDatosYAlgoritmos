class Heap:

    # Completar con el codigo del laboratorio, pregunta 1

    def builHeap(self):
        pass

    def percolateDown(self):
        return "No se que valor buscar"

class MinHeap(Heap):
    
    def percolateDown(self):
        return "Busco el menor valor"

class MaxHeap(Heap):
    
    def percolateDown(self):
        return "Busco el mayor valor"


p = Heap()
print(p.percolateDown())

p = MinHeap()
print(p.percolateDown())

p = MaxHeap()
print(p.percolateDown())


lista1 = lista2 = [10,3,9,1,2,7,8]
print(lista2)

dic = {1:4, 3:2, 5:4}
print(max(dic))
print(max(dic))