'''
Definition constant
'''
ID_FIRST_ELEMENT = 0

class Heap:
    '''
    Heap class
    '''
    def __init__(self):
        self.heapList = [0]
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

    def percolateDown(self, i):
        while (i * 2) <= self.size:
            minimumChild = self.minimumChild(i)
            if self.heapList[i] > self.heapList[minimumChild]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minimumChild]
                self.heapList[minimumChild] = tmp
            i = minimumChild

    def minimumChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolateUp(self, i):
        while(i // 2 > 0):
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def deleteMin(self):
       retval = self.heapList[1]
       self.heapList[1] = self.heapList[self.size]
       self.size = self.size - 1
       self.heapList.pop()
       self.percolateDown(1)
       return retval

    def insert(self, k):
        self.heapList.append(k)
        self.size = self.size + 1
        self.percolateUp(self.size)

    def printHeap(self):
        print(self.heapList[1:])

def FindKthLargestEle(HOrig, k):
    count = 1
    HAux = Heap()
    itm = HOrig.getMinimum()
    HAux.insert(itm)
    if count == k:
        return itm
    while (HAux.size >= 1):
        itm = HAux.deleteMin()
        count += 1
        if count == k:
            return itm
        else:
            if HOrig.rightChild(HOrig.searchElement(itm)) != -1:
                HAux.insert(HOrig.rightChild(HOrig.searchElement(itm)))
            if HOrig.leftChild(HOrig.searchElement(itm)) != -1:
                HAux.insert(HOrig.leftChild(HOrig.searchElement(itm)))

#
#
#
#
def test():
    HOrig = Heap()
    # add some nonsense:
    HOrig.insert(1)
    HOrig.insert(20)
    HOrig.insert(5)
    HOrig.insert(100)
    HOrig.insert(1000)
    HOrig.insert(12)
    HOrig.insert(18)
    HOrig.insert(16)

    print(HOrig.heapList)
    print(FindKthLargestEle(HOrig, 6))
    print(FindKthLargestEle(HOrig, 3))


#
#       10
#     3    9
#    1 2  7 8
#
def searchMinimunChildIndex():
    '''
    Search index of parent
    '''
    heap = Heap()
    heap.heapList = [10, 3, 9, 1, 2, 7, 8]
    #                 0 1 2 3 4 5 6
    print(heap.heapList)




if __name__ == '__main__':
    #test()
    searchMinimunChildIndex()
