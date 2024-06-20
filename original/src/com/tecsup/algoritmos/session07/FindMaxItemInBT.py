from BinaryTreeNode import BinaryTreeNode

#maxData = float("-infinity")
maxData = -1

def findMaxRecursive(root):

    global maxData

    if not root:
        return maxData

    if root.getData() > maxData:
        maxData = root.getData()

    findMaxRecursive(root.getLeft())
    findMaxRecursive(root.getRight())

    return maxData


'''
Binary Tree

                      1
                      |
            ----------------------
            |                     | 
            2                     3  

'''

childrenLeft = BinaryTreeNode(2)
childrenRight = BinaryTreeNode(3)
root = BinaryTreeNode(1,childrenLeft,childrenRight)

findMaxRecursive(root)
print(maxData)


'''
Binary Tree

                      1
                      |
            ----------------------
            |                     | 
            2                     3  
       ----------             ----------
       |        |             |        | 
       4        7             8        5

'''
children_left_left = BinaryTreeNode(4)
children_left_right = BinaryTreeNode(7)
root_left = BinaryTreeNode(2,children_left_left,
                             children_left_right)

children_right_left = BinaryTreeNode(8)
children_right_right = BinaryTreeNode(5)
root_right = BinaryTreeNode(3,children_right_left,
                             children_right_right)

root = BinaryTreeNode(1,root_left,
                        root_right)

findMaxRecursive(root)
print(maxData)
