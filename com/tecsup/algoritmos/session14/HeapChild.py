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
        return 2*index + 2

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
        '''
        Get maximum value child
        :param idx:
        :return:
        '''
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
        '''
        Get minimum index child
        :param idx:
        :return:
        '''
        valueLeftChild = self.leftChild(idx)
        valueRightChild = self.rightChild(idx)

        if valueLeftChild > valueRightChild :
            return self.rightChildIndex(idx)
        elif  valueLeftChild < valueRightChild :
            return self.leftChildIndex(idx)
        else :
            # return any child index
            return self.rightChildIndex(idx)

#
#
#       10
#     3    9
#    1 2  7 8
#
def searchMinimunChildIndex():
    '''
    Search minimum child of parent
    '''
    heap = Heap()
    heap.heapList = [10,3,9,1,2,7,8]
    #                 0 1 2 3 4 5 6

    # It is important
    heap.size = len(heap.heapList)

    #
    print(heap.heapList)

    # Parent of value 10 ( idx = 0 )
    idxParent = 2
    idxChild = heap.minimumChildIndex(idxParent)
    print('The minimum child of parent '
          'with index = %.f is %.f'
          %(idxParent,idxChild))

    print('---------------- Again ...! ----------------')

    # Only analize the first 3 elements.
    for idxParent in range(3):
        idxChild = heap.minimumChildIndex(idxParent)
        print('The minimum child of parent '
              'with index = %.f is %.f'
              % (idxParent, idxChild))


#
#
#       10
#     3    9
#    1 2  7 8
#
def searchMaximumChildIndex():
    '''
    Search minimum child of parent
    '''
    heap = Heap()
    heap.heapList = [10,3,9,1,2,7,8]
    #                 0 1 2 3 4 5 6

    # It is important
    heap.size = len(heap.heapList)

    #
    print(heap.heapList)

    # Parent of value 10 ( idx = 0 )
    idxParent = 1
    idxChild = heap.maximumChildIndex(idxParent)
    print('The maximum child of parent '
          'with index = %.f is %.f'
          %(idxParent,idxChild))


    print('---------------- Again ...! ----------------')

    # Only analize the first 3 elements.
    for idxParent in range(3):
        idxChild = heap.maximumChildIndex(idxParent)
        print('The maximum child of parent '
              'with index = %.f is %.f'
              % (idxParent, idxChild))


if __name__ == '__main__':
    #test()
    #searchMinimunChildIndex()
    searchMaximumChildIndex()
