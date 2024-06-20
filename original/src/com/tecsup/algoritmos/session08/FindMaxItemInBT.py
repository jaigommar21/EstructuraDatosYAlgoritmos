
from util.QueueLinkedLists import QueueLinkedListsCircular
#from BinaryTreeNode import BinaryTreeNode
from util.tree import BinaryTreeNode


def findMaxRecursive(tree): 
      
    # Base case  
    if tree is None:  
        return float('-inf')  # Mininum value

    data = tree.data 
    left_max = findMaxRecursive(tree.left)  
    right_max = findMaxRecursive(tree.right)  
        
    return max([data, left_max, right_max])

'''
Binary Tree

                      1
                      |
            ----------------------
            |                     | 
            2                     3  

'''




def findMaxUsingLevelOrder(root):

    maxElement = 0

    if root is None:
        return maxElement

    q = QueueLinkedListsCircular()
    q.enQueue(root)

    nodeBT = None

    while not q.isEmpty():

        nodeBT = q.deQueue()  # dequeue FIFO

        if maxElement <=  nodeBT.getData() :
            maxElement = nodeBT.getData()

        if nodeBT.getLeft():
            q.enQueue(nodeBT.getLeft())

        if nodeBT.getRight():
            q.enQueue(nodeBT.getRight())

    return maxElement


#
# Resolution
#           A
#       B       C
#     D   E   F   G

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

#
#findMaxRecursive(root)
#print("findMaxRecursive: " + str(maxData))
#

#

print("findMaxRecursive  ",findMaxRecursive(root))
#

#max = findMaxUsingLevelOrder(root)
#print("findMaxUsingLevelOrder : " + str(max))