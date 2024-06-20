ID_FIRST_ELEMENT = 0
 
class Heap:
 
    def __init__(self, heapList = []):
        self.heapList = heapList
        self.size = len(heapList)
 
    def searchElement(self, value):
        
        for i in range(self.size):
            if value == self.heapList[i]:
                return i
        return -1

#        10
#       5  3

lista=[10,5,3]

heap = Heap(lista)

pos = heap.searchElement(8)
print(pos)
