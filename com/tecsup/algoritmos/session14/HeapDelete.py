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
        #print("valueLeftChild = %d" % valueLeftChild)
        #print("valueRightChild = %d" % valueRightChild)

        if valueRightChild == -1 :
            return self.leftChildIndex(idx)

        if valueLeftChild > valueRightChild :
            return self.rightChildIndex(idx)
        elif  valueLeftChild < valueRightChild :
            return self.leftChildIndex(idx)
        else :
            # return any child index
            return self.rightChildIndex(idx)

    def percolateDown(self, i):
        '''
        Apply percolate down to heap
        :return:
        '''
        while self.leftChildIndex(i) < self.size:
          #  print(self.heapList)
            minimumChildIndex = self.minimumChildIndex(i)
          #  print("i = %d" % i)
          #  print("minimumChildIndex = %d" % minimumChildIndex)
            if self.heapList[i]  > self.heapList[minimumChildIndex]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minimumChildIndex]
                self.heapList[minimumChildIndex] = tmp
            i = minimumChildIndex

    def percolateDownItem(self, i):
            minimumChildIndex = self.minimumChildIndex(i)
            if self.heapList[i] > self.heapList[minimumChildIndex]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minimumChildIndex]
                self.heapList[minimumChildIndex] = tmp

    def percolateUp(self):
        '''
        Apply percolate up to heap
        :return:
        '''
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
        '''
        Insert an element at the end
        of heap and apply percolate up
        :param k:
        :return:
        '''
        self.heapList.append(k)
        self.size = self.size + 1
        self.percolateUp()

    def deleteTop(self):
        '''
        Delete an element from top
        of heap and apply percolate doown
        :return:
        '''
        self.heapList[0] = self.heapList[self.size-1]
        self.size = self.size-1
        self.heapList.pop()
        self.percolateDown(0)
#
#
#       10
#     3    9
#    1 2  7 8
#
def examplePercolateDownItem():
    '''
    Percolate download
    '''
    heap = Heap()
#    heap.heapList = [10,3,9,1,2,7,8]
#    #                 0 1 2 3 4 5 6

    heap.heapList = [10,3,9,1,2,7,8]
    heap.size = len(heap.heapList)
    #
    print("--------------------------")
    print(heap.heapList)
    heap.percolateDownItem(0)
    print(heap.heapList)
    print("--------------------------")
    print(heap.heapList)
    heap.percolateDownItem(1)
    print(heap.heapList)
    print("--------------------------")
    print(heap.heapList)
    heap.percolateDownItem(2)
    print(heap.heapList)


#
#
#       10
#     3    9
#    1 2  7 8
#
def examplePercolateDown():
    '''
    Percolate download
    '''
    heap = Heap()
#    heap.heapList = [10,3,9,1,2,7,8]
#    #                 0 1 2 3 4 5 6

    heap.heapList = [10,3,9,1,2,7,8]
    heap.size = len(heap.heapList)
    #
    print("--------------------------")
    print(heap.heapList)
    heap.percolateDown(0)
    print(heap.heapList)
    print("--------------------------")
    print(heap.heapList)
    heap.percolateDown(1)
    print(heap.heapList)
    print("--------------------------")
    print(heap.heapList)
    heap.percolateDown(2)
    print(heap.heapList)

#
#
#       1
#     2    7
#   10 3  9  8
#
def deleteHeapMin():
    '''
    Delete heap
    :return:
    '''

    heap = Heap()
    heap.heapList = [1, 2, 7, 10, 3, 9, 8]
    heap.size = len(heap.heapList)

 #   print(heap.heapList)
 #   heap.deleteTop()
 #   print(heap.heapList)

    print("======================")
    for i in range(len(heap.heapList)):
        print(heap.heapList)
        heap.deleteTop()
        print("---------------------")

    print(heap.heapList)


if __name__ == '__main__':

     # examplePercolateDownItem()
     # examplePercolateDown()
     deleteHeapMin()