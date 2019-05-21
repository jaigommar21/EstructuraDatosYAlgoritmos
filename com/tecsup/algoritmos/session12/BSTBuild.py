# BST Node

class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

def insertNode(root, node):
    '''
    Insert a node in BST
    '''
    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

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

def buildManualBST():
    '''
    Build Binary Search Tree
    :return:
    '''
    root = BSTNode(5)
    insertNode(root, BSTNode(7))
    insertNode(root, BSTNode(3))
    insertNode(root, BSTNode(9))
    insertNode(root, BSTNode(1))
    insertNode(root, BSTNode(12))
    insertNode(root, BSTNode(0))
    return root

def buildBSTFromArray(list):
    '''
    Build Binary Search Tree
    from Array
    :return:
    '''
    root = None

    for item in list:
        if list.index(item) == 1:
            root = BSTNode(item)
        else:
            insertNode(root, BSTNode(item))
    return root

#    root = BSTNode(5)
#    insertNode(root, BSTNode(0))
#    return root

if __name__ == '__main__':

    # Get tree
    #root = buildBST()

    # Build manual BST
    root = buildManualBST()

    # Build BST from Array
    list = [5,7,3,9,1,12,0,17,18]
    root = buildBSTFromArray(list)

    # Find min value
    nodeMinValue = findMin(root)
    print("Min value [Recursive mode] : %d" % nodeMinValue.data)

    # Find max value
    nodeMaxValue = findMax(root)
    print("Max value [Recursive mode] : %d" % nodeMaxValue.data)

    # Print In Order Traversal
    print("Print In Order Traversal :")
    inOrderTraversal(root)
