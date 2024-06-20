
from util.QueueLinkedLists import QueueLinkedListsCircular
from BinaryTreeNode import BinaryTreeNode

#
def findDataRecursive(root, dataSearch, nro_times=0):

    if root == None:
        return nro_times

    tmp_nro_times = nro_times

    if root.data == dataSearch:
        tmp_nro_times +=1
    
    return  tmp_nro_times  +  \
        findDataRecursive(root.left, dataSearch, nro_times)  + \
        findDataRecursive(root.right, dataSearch, nro_times)

#
def findDataUsingLevelOrder(root, dataSearch):

    flag = 0

    if root is None:
        return flag

    q = QueueLinkedListsCircular()
    q.enQueue(root)

    nodeBT = None

    while not q.isEmpty():

        nodeBT = q.deQueue()  # dequeue FIFO

        if dataSearch ==  nodeBT.getData() :
            flag = 1

        if nodeBT.getLeft():
            q.enQueue(nodeBT.getLeft())

        if nodeBT.getRight():
            q.enQueue(nodeBT.getRight())

    return flag


#
# Resolution
#           A
#       B       C
#     D   E   F   G

#
# Resolution
#           1
#       2       3
#     4   5   6   7



root = BinaryTreeNode(77)

root.left = BinaryTreeNode(77)

root.right = BinaryTreeNode(7)

root.left.left = BinaryTreeNode(77)
root.left.right = BinaryTreeNode(77)
root.right.left = BinaryTreeNode(77)
root.right.right = BinaryTreeNode(77)

dataSearch = 7
nro_times = findDataRecursive(root, dataSearch)
print("Se encontro el valor de %d, %d veces" % (dataSearch, nro_times))

#tmp2 = findDataUsingLevelOrder(root, dataSearch)
#print("Se encontro el valor de %d, %d vez" % (dataSearch, tmp2))