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

    def getParentIdx(self, child_idx):
        return (child_idx-1) //2

    def getLeftChildIdx(self, child_idx):
        return 2 * child_idx + 1

    def getLeftChildValue(self, index):
        '''
        Get value of left child
        :param index:
        :return:
        '''
        leftIndex = self.getLeftChildIdx(index)
        if leftIndex < self.size:
            return self.heapList[leftIndex]
        return -1

    def getRightChildIdx(self, index):
        return 2 * index + 2

    def getRightChildValue(self, parent_idx):
        '''
        Get value of right child
        :param index:
        :return:
        '''
        right_idx = self.getRightChildIdx(parent_idx)
        if right_idx < self.size:
            return self.heapList[right_idx]
        return -1

    def getMaxChildIdx(self, parent_idx):

        value_left_child = self.getLeftChildValue(parent_idx)
        value_right_child = self.getRightChildValue(parent_idx)

        if value_left_child > value_right_child :
            return self.getLeftChildIdx(parent_idx)
        elif  value_left_child < value_right_child :
            return self.getRightChildIdx(parent_idx)
        else :
            # return any child index
            return self.getLeftChildIdx(parent_idx)

    def getMinChildIdx(self, parent_idx):
        valueLeftChild = self.getLeftChildValue(parent_idx)
        valueRightChild = self.getRightChildValue(parent_idx)

        if valueRightChild == -1 :
            return self.getLeftChildIdx(parent_idx)

        if valueLeftChild > valueRightChild :
            return self.getRightChildIdx(parent_idx)
        elif  valueLeftChild < valueRightChild :
            return self.getLeftChildIdx(parent_idx)
        else :
            # return any child index
            return self.getRightChildIdx(parent_idx)

    def getTop(self):
        '''
        Get root value for Heap
        :return:
        '''
        if self.size == 0:
            return -1
        return self.heapList[0]

if __name__ == "__main__":

    #
    list_of_numbers = [10, 3, 9, 1, 2, 7, 8]
    
    heap = Heap()
    heap.heapList = list_of_numbers
    print("output >>",heap.heapList)

