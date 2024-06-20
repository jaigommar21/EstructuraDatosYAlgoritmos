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


    '''
    Métodos agregados
    '''

    def buildHeap(self,raw_list):
        '''
        Built heap from array
        :param list:
        :return:
        '''  
        #i = len(list) // 2   # 1 2 3 4 5 6 7 8 9
        #i = len(list) - 1
        idxs = range(len(raw_list)//2, -1, -1)
        print(idxs)
        self.size = len(list)  # 9
        self.heapList = list  
        print("")
        for i in idxs :  #  i =  4,3,2,1,0
            tmp = self.heapList[i]
            print(f"percolate-down  {tmp}  <<  {self.heapList}")
            self.percolateDown(i)
            print(f"percolate-down  {tmp}  <<  {self.heapList}")
            print("")
            
    def swap(self, idx_from, idx_to):
        tmp = self.heapList[idx_to]  
        self.heapList[idx_to] = self.heapList[idx_from] 
        self.heapList[idx_from] = tmp

    def percolateDown(self, i):
        pass

# Clase hija que hereda de la clase
# padre Heap
class MinHeap(Heap):
    
    def __init__(self):
        super().__init__()
    

    def percolateDown(self, i):
        '''
        Apply percolate down to heap
        :return:
        '''
        while self.getLeftChildIdx(i) < self.size:
            idx_min_child = self.getMinChildIdx(i)
            if self.heapList[i] > self.heapList[idx_min_child]:
                self.swap(i,idx_min_child)
            i = idx_min_child



# Clase hija que hereda de la clase
# padre Heap
class MaxHeap(Heap):
    
    def __init__(self):
        super().__init__()
    

    def percolateDown(self, i):
        '''
        Apply percolate down to heap
        :return:
        '''
        while self.getLeftChildIdx(i) < self.size:
            idx_max_child = self.getMaxChildIdx(i)
            if self.heapList[i] < self.heapList[idx_max_child]:
                self.swap(i,idx_max_child)
            i = idx_max_child

# output >> [1, 3, 2, 5, 7, 10, 8, 20, 9]

# Código a ejecutarse
LIST_ORIGIN = [3, 9, 10, 1, 7, 2, 8, 20, 5]
list = LIST_ORIGIN
print("input <<",list)
heap = MinHeap()
heap.buildHeap(list)
print("output >>",heap.heapList)

#
#          1
#
#
#           1
#         2   3
#
#             1
#         2      3
#       4  5    6  7
#
#                 1
#          2            3
#       4     5      6      7
#      8 9  10 11  12 13  14 15
#
#                               1
#                2                          3
#          4            5             6            7
#      8      9      10    11     12     13     14     15
#    16 17  18 19  20 21  22 23  24 25  26 27  28 29  30 31