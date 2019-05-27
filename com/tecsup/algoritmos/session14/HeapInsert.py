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
        return 2*index + 1

    def rightChildIndex(self, index):
        return 2*index + 2

    def leftChild(self, index):
        if 2 * index + 1 <= self.size:
            return self.heapList[self.leftChildIndex(index)]
        return -1

    def rightChild(self, index):
        if 2 * index + 2 <= self.size:
            return self.heapList[self.rightChildIndex(index)]
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

    def percolateDown(self, i):
        while (i * 2) <= self.size:
            minimumChildIndex = self.minimumChildIndex(i)
            if self.heapList[i] > self.heapList[minimumChildIndex]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minimumChildIndex]
                self.heapList[minimumChildIndex] = tmp
            i = minimumChildIndex

    def percolateDownItem(self, i):
        while (i * 2) <= self.size:
            minimumChildIndex = self.minimumChildIndex(i)
            if self.heapList[i] > self.heapList[minimumChildIndex]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minimumChildIndex]
                self.heapList[minimumChildIndex] = tmp
            i = minimumChildIndex

    def percolateUp(self):
        i = self.size - 1
        iParent = self.parentIndex(i)
        while(iParent >= 0):
            if self.heapList[i] < self.heapList[iParent]:
                tmp = self.heapList[iParent]
                self.heapList[iParent] = self.heapList[i]
                self.heapList[i] = tmp
            i = iParent
            iParent = self.parentIndex(i)
            #print(self.heapList)

    def percolateUpItem(self, i):
        iParent = self.parentIndex(i)
        if self.heapList[i] < self.heapList[iParent]:
            tmp = self.heapList[iParent]
            self.heapList[iParent] = self.heapList[i]
            self.heapList[i] = tmp

    def insertUp(self, k):
        self.heapList.append(k)
        self.size = self.size + 1
        self.percolateUp()

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
    #                 0 1 2

    # It is important
    heap.size = len(heap.heapList)

    #
    print(heap.heapList)

    #
    heap.percolateUpItem(2)
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

    list = [10, 3, 9, 1, 2, 7, 8]

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
    sortMinHeapFromArray()