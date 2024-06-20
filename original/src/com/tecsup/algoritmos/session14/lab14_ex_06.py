'''

'''

# Clase base Heap
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

    def getMaximumChildIndex(self, idx):

        valueLeftChild = self.leftChild(idx)
        valueRightChild = self.rightChild(idx)

        if valueLeftChild > valueRightChild :
            return self.leftChildIndex(idx)
        elif  valueLeftChild < valueRightChild :
            return self.rightChildIndex(idx)
        else :
            # return any child index
            return self.leftChildIndex(idx)

    def getMinimumChildIndex(self, idx):
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

    def getTop(self):
        '''
        Get root value for Heap
        :return:
        '''
        if self.size == 0:
            return -1
        return self.heapList[0]

    '''
    Métodos agregados
    '''

    def buildHeap(self,list):
        '''
        Built heap from array
        :param list:
        :return:
        '''
        i = len(list) // 2   # 9 --> i = 4
        #i = len(list) - 1
        self.size = len(list)  # 9
        self.heapList = list  
        print("")
        while i >= 0:  #  i =  4,3,2,1,0
            tmp = self.heapList[i]
            print("percolate-down ", tmp , " <<", self.heapList)
            self.percolateDown(i)
            print("percolate-down ", tmp , " >>", self.heapList)
            print("")
            i = i - 1

    def swap(self, idx_from, idx_to):
        tmp = self.heapList[idx_to]  
        self.heapList[idx_to] = self.heapList[idx_from] 
        self.heapList[idx_from] = tmp

    def percolateDown(self, i):
        pass


    '''
    Nuevos Métodos agregados
    '''
    def delete(self):
        '''
        Delete an element from top
        of heap and apply percolate doown
        :return:
        '''
        # [1, 3, 2, 5, 7, 10, 8, 20, 9]
        ret = self.heapList[0]  # 1
        self.heapList[0] = self.heapList[self.size-1]
        self.size = self.size-1
        self.heapList.pop()
        self.percolateDown(0)
        return ret

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


# Clase hija que hereda de la clase
# padre Heap
class MinHeap(Heap):
    
    def __init__(self):
        super().__init__()
    

    def percolateDown(self, i):
        '''
        Apply percolate up to heap
        :return:
        '''
        while self.leftChildIndex(i) < self.size:
            minimumChildIndex = self.getMinimumChildIndex(i)
            if self.heapList[i] > self.heapList[minimumChildIndex]:
                self.swap(i,minimumChildIndex)
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

LIST_ORIGIN = [3, 9, 10, 1, 7, 2, 8, 20, 5]

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
