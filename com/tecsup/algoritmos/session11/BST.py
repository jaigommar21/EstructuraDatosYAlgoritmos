# BST Node

class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

def find(root, data):
    '''
    Method to find data in BST
    Recursive mode
    :param root:
    :return:
    '''
    currentNode = root

    if currentNode == None:
        return None
    else:
        if data == currentNode.data:
            return currentNode
        if data < currentNode.data:
            return find(currentNode.left,data)
        else:
            return find(currentNode.right,data)

def findIterative(root, data):
    '''
    Method to find data in BST
    Iterative mode
    :param root:
    :return:
    '''
    currentNode = root
    while currentNode:
        if data == currentNode.data:
            return currentNode
        if data < currentNode.data:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

    return None

def findMin(root):
    '''
    Find the minimum value. Recursive mode
    :param root:
    :return:
    '''
    currentNode = root
    if currentNode.left == None:
        return currentNode
    else:
        return findMin(currentNode.left)

def findMinIterative(root):
    '''
    Find the minimum value. Iterative mode
    :param root:
    :return:
    '''
    currentNode = root
    while currentNode.left != None:
        currentNode = currentNode.left
    return currentNode

def findMax(root):
    '''
    Find the maximum value. Recursive mode
    :param root:
    :return:
    '''
    currentNode = root
    if currentNode.right == None:
        return currentNode
    else:
        return findMax(currentNode.right)

def findMaxIterative(root):
    '''
    Find the maximum value. Iterative mode
    :param root:
    :return:
    '''
    currentNode = root
    while currentNode.right != None:
        currentNode = currentNode.right
    return currentNode

def preOrderTraversal(root):
    '''
    Print value in Pre Order Traversal
    :param root:
    :return:
    '''
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def inOrderTraversal(root):
    '''
    Print value In Order Traversal
    :param root:
    :return:
    '''
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)

def postOrderTraversal(root):
    '''
    Print value Post Order Traversal
    :param root:
    :return:
    '''
    if not root:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)


# Binary Search Tree
#
#          5
#        /  \
#       /    \
#     3        7
#    /  \     / \
#   2    4   6   8
#
def buildBST():
    '''
    Build Binary Search Tree
    :return:
    '''
    root = BSTNode(5)
    root.left = BSTNode(3)
    root.left.left = BSTNode(2)
    root.left.right = BSTNode(4)
    root.right = BSTNode(7)
    root.right.left = BSTNode(6)
    root.right.right = BSTNode(8)
    return root;


if __name__ == '__main__':

    # Get tree
    root = buildBST()

    # Find
    nodeFound = find(root, 7)
    print("Node found [Recursive mode] : %d" % nodeFound.data)



if __name__ == '__main2__':

    # Get tree
    root = buildBST()

    # Find
    nodeFound = find(root, 7)
    print("Node found [Recursive mode] : %d" % nodeFound.data)

    # Find
    nodeFoundIte = findIterative(root, 7)
    print("Node found [Iterative mode] : %d" % nodeFoundIte.data)

    # Find min value
    nodeMinValue = findMin(root)
    print("Min value [Recursive mode] : %d" % nodeMinValue.data)

    # Find min value
    nodeMinValueIte = findMinIterative(root)
    print("Min value [Iterative mode] : %d" % nodeMinValueIte.data)

    # Find max value
    nodeMaxValue = findMax(root)
    print("Max value [Recursive mode] : %d" % nodeMaxValue.data)

    # Find max value
    nodeMaxValueIte = findMaxIterative(root)
    print("Max value [Iterative mode] : %d" % nodeMaxValueIte.data)

    # Print Pre Order Traversal
    print("Print Pre Order Traversal :")
    preOrderTraversal(root)

    # Print In Order Traversal
    print("Print In Order Traversal :")
    inOrderTraversal(root)

    # Print Pre Order Traversal
    print("Print Post Order Traversal :")
    postOrderTraversal(root)

