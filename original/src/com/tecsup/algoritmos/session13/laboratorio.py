ID_FIRST_ELEMENT = 0

class Heap:

    def __init__(self, heapList = []):
        self.heapList = heapList
        self.size = len(heapList)
    
    def parentIndex(self, index):
        return (index-1) //2

    def leftChildIndex(self, index):
        return 2 * index + 1

    def rightChildIndex(self, index):
        return 2 * index + 2

    def searchElement(self, value):
        for i in range(self.size):
            if value == self.heapList[i]:
                return i
        return -1

    def percolateUp(self, i):
        
        pos = i - 1 # get the last position

        while self.parentIndex(pos) >= 0 : # exist parent position?

            parent_pos = self.parentIndex(pos)

            if self.heapList[parent_pos] < self.heapList[pos]: # need to change?
                
                # interchange values    
                tmp = self.heapList[parent_pos] 
                self.heapList[parent_pos] = self.heapList[pos]
                self.heapList[pos] = tmp 

            pos = parent_pos


    def insert(self, k): 
        self.heapList.append(k) 
        self.size = self.size + 1 
        self.percolateUp(self.size)

#
#       10
#     3    9
#    1 2  7 8
#

listado = [10,3,9,1,2,7,8]
heap = Heap(listado)
#print(heap.searchElement(1))

#listado = [10,3,9,1,2,7,8]
#24	8	5	4	3
heap = Heap()
heap.insert(8)
print(heap.heapList)
heap.insert(24)
print(heap.heapList)
"""
heap.insert(5)
print(heap.heapList)
heap.insert(4)
print(heap.heapList)
heap.insert(3)
print(heap.heapList)
heap.insert(7)
print(heap.heapList)
heap.insert(18)
print(heap.heapList)
heap.insert(40)
print(heap.heapList)
#"""
#
#       40
#     24    18
#    8  3  5   7 
#  4
"""
heap.insert(10)
print(heap.heapList)
"""
#"""
#
#         40
#      24       18
#   10    3   5     7 
#  4  8