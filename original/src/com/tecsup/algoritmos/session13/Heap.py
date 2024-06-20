'''
'''

ID_FIRST_ELEMENT = 0

class Heap:

    def __init__(self, heapList = []):
        self.heapList = heapList
        self.size = len(heapList)

    def parentIndex(self, index):
        return (index-1) //2

    def leftChildIndex(self, index):
        return 2 * index + 1

    def leftChild(self, index):
        '''
        Get value of left child
        :param index:
        :return:
        '''
        leftIndex = self.leftChildIndex(index)
        if leftIndex < self.size:
            return self.heapList[leftIndex]
        return -1

    def rightChildIndex(self, index):
        return 2 * index + 2

    def rightChild(self, index):
        '''
        Get value of right child
        :param index:
        :return:
        '''
        rightIndex = self.rightChildIndex(index)
        if rightIndex < self.size:
            return self.heapList[rightIndex]
        return -1

    def searchElement(self, value):
        for i in range(self.size):
            if value == self.heapList[i]:
                return i
        return -1

    def getMinimum(self):
        '''
        Get Maximum value for Min-Heap
        :return:
        '''
        if self.size == 0:
            return -1
        return self.heapList[ID_FIRST_ELEMENT]

    def getMaximum(self):
        '''
        Get Maximum value for Max-Heap
        :return:
        '''
        if self.size == 0:
            return -1
        return self.heapList[ID_FIRST_ELEMENT]

    def  build_max_heap(self):
        '''
        Metodo que ordena un max heap
        '''
        #  0 1 2
        # [1,2,3]
        #
        # Percolate Down : arriba hacia abajo
        # navegar desde index 0 a 2
        #
        # Percolate Up : abajo hacia arriba
        # navegar desde index 2 a 1
        
        # Percolate Up
        print(self.heapList)
        i = len(self.heapList) - 1
        
        while i > 0: # Realizar el proceso hasta el index = 1            
            print("Percolate Up",i)
            #print(self.heapList)

            j = i
            j_p = self.parentIndex(j)
            while  j_p >= 0 :
                # Posicion del padre
                #print("hijo",i,"-padre", i_p)
                if self.heapList[j] > self.heapList[j_p]:
                    tmp = self.heapList[j_p]
                    self.heapList[j_p] = self.heapList[j]
                    self.heapList[j] =  tmp
                    print("interchange" ,self.heapList)
                
                j = j_p
                j_p = self.parentIndex(j)

            i = i - 1 
        
        #print(self.heapList)
#
#       10
#     3    9
#    1 2  7 8
#
def searchParent():
    '''
    Search index of parent
    '''
    heap = Heap()
    heap.heapList = [10,3,9,1,2,7,8]
    #                 0 1 2 3 4 5 6
    print(heap.heapList)

    # Parent of 3 ( index = 1 )
    idx = 1
    idxParent = heap.parentIndex(idx)
    print('Parent of index=%.0f is index=%.0f' %(idx, idxParent))

    # Parent of 9 ( index = 2 )
    idx = 2
    idxParent = heap.parentIndex(idx)
    print('Parent of index=%.0f is index=%.0f' %(idx, idxParent))

    print('------- Again ...! ---------' )

    for idx in range(1,len(heap.heapList)):
        idxParent = heap.parentIndex(idx)
        print('Parent of index=%.0f is index=%.0f' %(idx, idxParent))

#
#       10
#     3    9
#    1 2  7 8
#
def searchChild():
    '''
    Search index of child left or right
    '''
    heap = Heap()
    heap.heapList = [10,3,9,1,2,7,8]
    #                 0 1 2 3 4 5 6
    print(heap.heapList)

    print('=============================================')
    print('==================== Left ===================')
    print('=============================================')

    # Left child of parent 10 ( index = 0 )
    idxParent = 0
    idxLeftChild = heap.leftChildIndex(idxParent)
    print('Left child of parent with index=%.0f is index=%.0f'
          %(idxParent, idxLeftChild))

    print('---------------- Again ...! ----------------')

    for idxParent in range(3):
        idxLeftChild = heap.leftChildIndex(idxParent)
        print('Left child of parent with index=%.0f is index=%.0f'
              % (idxParent, idxLeftChild))

    print('=============================================')
    print('==================== Right ==================')
    print('=============================================')

    # Right child of parent 10 ( index = 0 )
    idxParent = 0
    idxRightChild = heap.rightChildIndex(idxParent)
    print('Right child of parent with index=%.0f is index=%.0f'
          %(idxParent, idxRightChild))

    print('---------------- Again ...! ----------------')

    for idxParent in range(3):
        idxRightChild = heap.rightChildIndex(idxParent)
        print('Right child of parent with index=%.0f is index=%.0f'
              % (idxParent, idxRightChild))

#
#       10
#     3    9
#    1 2  7 8
#
def searchElement():
    '''
    Search element value for Max-Heap
    '''
    heap = Heap()
    heap.heapList = [10,3,9,1,2,7,8]
    #                 0 1 2 3 4 5 6

    # It is important
    heap.size = len(heap.heapList)

    #
    print(heap.heapList)

    valueElement= 9
    idx = heap.searchElement(valueElement)

    print('The index of element %.0f is %.f' % (valueElement, idx) )

#
#       10
#     3    9
def printMaximumValue():
#    1 2  7 8
#
    '''
    Get maximum value for Max-Heap
    '''
    heap = Heap()
    heap.heapList = [10,3,9,1,2,7,8]
    #                 0 1 2 3 4 5 6
    heap.size = len(heap.heapList)

    #
    print(heap.heapList)

    print('Maximum value from Heap is %.0f' % heap.getMaximum())

#
#       10
#     3    9
#    1 2  7 8
#

#   



def printChild():
    '''
    Print right and left children for Max-Heap
    '''
    heap = Heap()
    heap.heapList = [10,3,9,1,2,7,8]
    #                 0 1 2 3 4 5 6
    heap.size = len(heap.heapList)

    #
    print(heap.heapList)

    # Only analize the first 3 elements.
    for idxParent in range(3):
        valueLeft = heap.leftChild(idxParent)
        valueRight = heap.rightChild(idxParent)
        print('Parent with index %.0f have left child '
              'value %.0f and right child value %.0f '
              % (idxParent, valueLeft, valueRight))

if __name__ == '__main__':
    #searchParent()
    #searchChild()
    #searchElement()
    #printMaximumValue()
    #printChild()

    # inicialmente esta desordenado
    mi_max_heap = [1,2,3,5,12,19,25,100] 

    heap = Heap(mi_max_heap)

    heap.build_max_heap()

    print(heap.heapList)


