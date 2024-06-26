'''
Definition constant
'''
ID_FIRST_ELEMENT = 0

class Heap:
    '''
    Heap class
    '''
    def __init__(self):
        self.heapList = []
        self.size = 0

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

    def searchElement(self, itm):
        i = 0
        while (i <= self.size):
            if itm == self.heapList[i]:
                return i
            i += 1

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

    def maximumChildIndex(self, idx):

        valueLeftChild = self.leftChild(idx)
        valueRightChild = self.rightChild(idx)

        if valueLeftChild > valueRightChild :
            return self.leftChildIndex(idx)
        elif  valueLeftChild < valueRightChild :
            return self.rightChildIndex(idx)
        else :
            # return any child index
            return self.leftChildIndex(idx)

    def minimumChildIndex(self, idx):

        valueLeftChild = self.leftChild(idx)
        valueRightChild = self.rightChild(idx)

        if valueLeftChild > valueRightChild :
            return self.rightChildIndex(idx)
        elif  valueLeftChild < valueRightChild :
            return self.leftChildIndex(idx)
        else :
            # return any child index
            return self.rightChildIndex(idx)

    """    
            3
          /   \  
        2       4

 index --> 0   1   2
          [2 , 3,  4 ]
    """
    def percolateUp(self):  # del último elemento
        '''
        Apply percolate up to heap
        :return:
        '''
        iChild = self.size - 1  # 2
        iParent = self.parentIndex(iChild) # 0
        while(iParent >= 0):
            #            1                   2
            if self.heapList[iChild] < self.heapList[iParent]:
                tmp = self.heapList[iParent]
                self.heapList[iParent] = self.heapList[iChild]
                self.heapList[iChild] = tmp
            iChild = iParent
            iParent = self.parentIndex(iChild)
            #print(self.heapList)

    def percolateUpItem(self, i):
        iParent = self.parentIndex(i)
        if self.heapList[i] < self.heapList[iParent]:
            tmp = self.heapList[iParent]
            self.heapList[iParent] = self.heapList[i]
            self.heapList[i] = tmp

    def insertUp(self, k):
        '''
        Insert an element at the end
        of heap and apply percolate up
        :param k:
        :return:
        '''
        self.heapList.append(k)
        self.size = self.size + 1
        self.percolateUp() # Del ultimo elemento

#
#
#       10
#     3    9
#    1 2  7 8
#
def sortDownArray():
    '''
    Search minimum child of parent
    '''
    heap = Heap()
#    heap.heapList = [10,3,9,1,2,7,8]
#    #                 0 1 2 3 4 5 6

    heap.heapList = [10,3,9,1,2,7,8]
    #                 0 1 2 3 4 5 6

    # It is important
    heap.size = len(heap.heapList)

    #
    print(heap.heapList)

    #
    heap.percolateUpItem(5)
    #heap.percolateUp()
    #
    print(heap.heapList)



#
#
#       10
#     3    9
#    1 2  7 8
#
def sortMinHeapFromArray():
    '''
    Sort min-heap from array
    :return:
    '''

    list = [10, 9, 3, 1, 2, 7, 8,0,200]

    heap = Heap()

    for i in range(len(list)):
        #print("c[%d] = %d" % (i,list[i]))
        heap.insertUp(list[i])
        #print("--------------------------")
        #print(heap.heapList)
        #print("==========================")
    print(list)
    print(heap.heapList)

if __name__ == '__main__':

    #sortDownArray()
    #sortMinHeapFromArray()

    """    
            3
          /  
        2       

 index --> 0   1 
          [3,  2 ]
    """
    heap = Heap()
    print(heap.heapList)
    heap.insertUp(3)
    print(heap.heapList)
    heap.insertUp(2)
    print(heap.heapList)
    heap.insertUp(1)
    print(heap.heapList)
