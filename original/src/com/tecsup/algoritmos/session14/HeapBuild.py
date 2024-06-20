from abc import abstractmethod

#
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

        if valueRightChild == -1 :
            return self.leftChildIndex(idx)

        if valueLeftChild > valueRightChild :
            return self.rightChildIndex(idx)
        elif  valueLeftChild < valueRightChild :
            return self.leftChildIndex(idx)
        else :
            # return any child index
            return self.rightChildIndex(idx)

    def getTop(self):
        '''
        Get root value for Heap
        :return:
        '''
        if self.size == 0:
            return -1
        return self.heapList[0]

    @abstractmethod
    def percolateDown(self, i):
        pass

    def buildHeap(self,list):
        '''
        Built heap from array
        :param list:
        :return:
        '''
        i = len(list) // 2
        self.size = len(list)
        self.heapList = list
        print("")
        while i >= 0:
            tmp = self.heapList[i]
            print("percolate-down ", tmp , " <<", self.heapList)
            self.percolateDown(i)
            print("percolate-down ", tmp , " >>", self.heapList)
            print("")
            i = i - 1

    def delete(self):
        '''
        Delete an element from top
        of heap and apply percolate doown
        :return:
        '''
        ret = self.heapList[0]
        self.heapList[0] = self.heapList[self.size-1]
        self.size = self.size-1
        self.heapList.pop()
        self.percolateDown(0)
        return ret

    @abstractmethod
    def percolateUp(self, i):
        pass

    def insert(self, k):
        '''
        Insert an element at the end
        of heap and apply percolate up
        :param k:
        :return:
        '''
        self.heapList.append(k)
        self.size = self.size + 1
        self.percolateUp(self.size - 1)

    def interchangeTopWithBottom(self):
        '''
        interchange first and last element
        of heap
        :return:
        '''
        tmp = self.heapList[0]
        self.heapList[0] = self.heapList[self.size-1]
        self.heapList[self.size - 1] = tmp
        self.size = self.size-1
        self.percolateDown(0)

class MinHeap (Heap):

    def percolateDown(self, i):
        '''
        Apply percolate down to bottom
        :return:
        '''
        while self.leftChildIndex(i) < self.size:
            minimumChildIndex = self.minimumChildIndex(i)
            if self.heapList[i] > self.heapList[minimumChildIndex]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minimumChildIndex]
                self.heapList[minimumChildIndex] = tmp
            i = minimumChildIndex

    def percolateUp(self, i):
        '''
        Apply percolate up to heap
        :return:
        '''
        iParent = self.parentIndex(i)
        while(iParent >= 0):
            #print(iParent)
            #print(i)
            if self.heapList[iParent] > self.heapList[i]:
                tmp = self.heapList[iParent]
                self.heapList[iParent] = self.heapList[i]
                self.heapList[i] = tmp
            i = iParent
            iParent = self.parentIndex(i)
            #print(self.heapList)



class MaxHeap (Heap):

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
    
    def percolateUp(self, idx_child):
        '''
        Apply percolate down to heap
        :return:
        '''
        idx_parent = self.parentIndex(idx_child)
        while(idx_parent >= 0):
            if self.heapList[idx_parent] < self.heapList[idx_child]:
                tmp = self.heapList[idx_parent]
                self.heapList[idx_parent] = self.heapList[idx_child]
                self.heapList[idx_child] = tmp
            idx_child = idx_parent
            idx_parent = self.parentIndex(idx_child)
            #print(self.heapList)


LIST_ORIGIN = [3, 9, 10, 1, 7, 2, 8, 20, 5]

#
#
# output >> [1, 3, 2, 5, 7, 10, 8, 20, 9]
#
def exampleMinHeapBuild():

    list = LIST_ORIGIN
    print("input <<",list)
    heap = MinHeap()
    heap.buildHeap(list)
    print("output >>",heap.heapList)

#
#
# 
# output : [20, 9, 10, 5, 7, 2, 8, 1, 3]
#
def exampleMaxHeapBuild():

    list = LIST_ORIGIN
    print(list)
    heap = MaxHeap()
    heap.buildHeap(list)
    print(heap.heapList)

#
#
def deleteTopMinHeap():
    '''
    Delete heap
    :return:
    '''

    list = LIST_ORIGIN
    print(list)
    heap = MinHeap()
    heap.buildHeap(list)

    #print(heap.heapList)
    #heap.deleteTop()
    #print(heap.heapList)

    print("=========================")
    for i in range(len(heap.heapList)):
        print(heap.heapList)
        ret = heap.delete()
        print("------------------------")
        print("attend --> ", ret)
        
    print(heap.heapList)

#
#
def deleteTopMaxHeap():
    '''
    Delete heap
    :return:
    '''
    
    list = LIST_ORIGIN
    print(list)
    heap = MaxHeap()
    heap.buildHeap(list)

    #print(heap.heapList)
    #heap.deleteTop()
    #print(heap.heapList)

    print("=========================")
    for i in range(len(heap.heapList)):
        print(heap.heapList)
        ret = heap.delete()
        print("------------------------")
        print("attend --> ", ret)
 
    print(heap.heapList)

#
# output >> [1, 3, 2, 5, 7, 10, 8, 20, 9]
#
def insertItemMinHeap():
    '''
    Insert item in MinHeap
    :return:
    '''

    #list = [10, 9, 3, 1, 2, 7, 8,0,200]
    list = LIST_ORIGIN

    heap = MinHeap()

    for i in range(len(list)):
        #print("c[%d] = %d" % (i,list[i]))
        heap.insert(list[i])
        print("--------------------------")
        print(heap.heapList)

    print("--------------------------")
    print("input <<",list)
    print("output >>",heap.heapList)

#
# output >> [20, 10, 9, 7, 3, 2, 8, 1, 5]
#
def insertItemMaxHeap():
    '''
    Insert item in MaxHeap
    :return:
    '''

    #list = [10, 9, 3, 1, 2, 7, 8,0,200]
    list = LIST_ORIGIN
    
    heap = MaxHeap()

    for i in range(len(list)):
        #print("c[%d] = %d" % (i,list[i]))
        heap.insert(list[i])
        print("--------------------------")
        print(heap.heapList)

    print("--------------------------")
    print("input <<",list)
    print("output >>",heap.heapList)

def exampleMinHeapSortFromArrayUnsorted():
    '''
    Apply heap sort from an array unsorted
    :return:
    '''
    list = [10,3,9,1,2,7,8,12,465,7767,2,45]

    print("====== Array Unsorted =======")
    print(list)

    heap = MinHeap()
    heap.buildHeap(list)

    print("========== Heaps ============")
    print(heap.heapList)

    print("======- Start Sorted ========")
    for i in range(len(heap.heapList)):
        print("--- Extract %d number -----"%(i+1))
        heap.interchangeTopWithBottom()
        print(heap.heapList)

    print("======- Array Sorted ========")
    print(heap.heapList)

def exampleMaxHeapSortFromArrayUnsorted():
    '''
    Apply heap sort from an array unsorted
    :return:
    '''
    list = [10,3,9,1,2,7,8,12,465,7767,2,45]

    print("====== Array Unsorted =======")
    print(list)

    heap = MaxHeap()
    heap.buildHeap(list)

    print("========== Heaps ============")
    print(heap.heapList)

    print("======- Start Sorted ========")
    for i in range(len(heap.heapList)):
        print("--- Extract %d number -----"%(i+1))
        heap.interchangeTopWithBottom()
        print(heap.heapList)

    print("======- Array Sorted ========")
    print(heap.heapList)


if __name__ == '__main__':
    #exampleMinHeapBuild()
    #exampleMaxHeapBuild()
    #deleteTopMinHeap()
    #deleteTopMaxHeap()
    #insertItemMinHeap()
    #insertItemMaxHeap()
    #exampleMinHeapSortFromArrayUnsorted()
    #exampleMaxHeapSortFromArrayUnsorted()
    pass


'''
list = [10,3,9,1,2,7,8,12,465,7767,2,45]

list = [1,3,5,7,2,8]

list = [1,2,3,5,7,8]


'''