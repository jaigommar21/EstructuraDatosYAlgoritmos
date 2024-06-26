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

    def leftChildValue(self, index):
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

    def rightChildValue(self, index):
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

        valueLeftChild = self.leftChildValue(idx)
        valueRightChild = self.rightChildValue(idx)

        if valueLeftChild > valueRightChild :
            return self.leftChildIndex(idx)
        elif  valueLeftChild < valueRightChild :
            return self.rightChildIndex(idx)
        else :
            # return any child index
            return self.leftChildIndex(idx)


    def minimumChildIndex(self, idx):
        valueLeftChild = self.leftChildValue(idx)
        valueRightChild = self.rightChildValue(idx)
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
         #   print("i = %d" % i)
         #   print("minimumChildIndex = %d" % minimumChildIndex)
            if self.heapList[i] > self.heapList[minimumChildIndex]:
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
        self.heapList[0] = self.heapList[self.size - 1]
        self.size = self.size - 1
        self.heapList.pop()
        self.percolateDown(0)

    def buildHeap(self,list):
        '''
        Built heap from array
        :param list:
        :return:
        '''
        i = len(list) // 2
        self.size = len(list)
        self.heapList = list
        while i >= 0:
            self.percolateDown(i)
            i = i - 1

    def interchangeTopWithBottomOfHeap(self):
        '''
        interchange first and last element
        of heap
        :return:
        '''
        tmp = self.heapList[0]
        self.heapList[0] = self.heapList[self.size-1]
        self.heapList[self.size - 1] = tmp
        self.size = self.size-1
        #self.percolateDown(0)


class MaxHeap(Heap):

    def percolateDown(self, i):
        '''
        Apply percolate down to heap
        :return:
        '''
        while self.leftChildIndex(i) < self.size:
            maximumChildIndex = self.maximumChildIndex(i)
            if self.heapList[i] < self.heapList[maximumChildIndex]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[maximumChildIndex]
                self.heapList[maximumChildIndex] = tmp
            i = maximumChildIndex

def exampleHeapSortFromArrayUnsorted():
    '''
    Apply heap sort from an array unsorted
    :return:
    '''
    list = [10,3,9,1,2,7,8,12,465,7767,21,45,0, 12345,666, 13]

    print("====== Array Unsorted =======")
    print(list)

    heap = MaxHeap()
    heap.buildHeap(list)
    
    """
    print("========== Heaps ============")
    print(heap.heapList)
    """
    
    print("======- Start Sorted ========")
    for i in range(len(heap.heapList)):
        #print("--- Extract %d number -----"%(i+1))
        heap.interchangeTopWithBottomOfHeap()
        heap.percolateDown(0)
        #print(heap.heapList)

    print("======- Array Sorted ========")
    print(heap.heapList)
    
if __name__ == '__main__':

    exampleHeapSortFromArrayUnsorted()