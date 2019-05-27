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
        if 2 * index + 1 < self.size:
            return self.heapList[self.leftChildIndex(index)]
        return -1

    def rightChild(self, index):
        if 2 * index + 2 < self.size:
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

    def deleteTop(self):
        self.heapList[0] = self.heapList[self.size-1]
        self.size = self.size-1
        self.heapList.pop()
        self.percolateDown(0)


    def buildHeap(self,list):
        i = len(list) // 2
        self.size = len(list)
        self.heapList = list
        while i >= 0:
            self.percolateDown(i)
            i = i - 1


#
#
#       10
#     3    9
#    1 2  7 8
#
def exampleHeapBuild():

    list = [10,3,9,1,2,7,8]
    print(list)
    heap = Heap()
    heap.buildHeap(list)
    print(heap.heapList)


if __name__ == '__main__':

    exampleHeapBuild()