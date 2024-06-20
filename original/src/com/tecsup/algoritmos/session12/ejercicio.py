# BST Node

class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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


def insertNode2(root, node):

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
    return root

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


def findIterative(root, data):
    '''
    Method to find data in BST
    Iterative mode
    :param root:
    :return:
    '''
    currentNode = root
    parent = None
    while currentNode:
        if data == currentNode.data:
            return [parent, currentNode]
        if data < currentNode.data:
            parent = currentNode
            currentNode = currentNode.left
        else:
            parent = currentNode
            currentNode = currentNode.right

    return [None,None]


'''


          
0
1
3
5
7
9
12

'''


'''
# Siempre se inicialice el root con un nodo
root = BSTNode(5)
insertNode(root, BSTNode(7))
insertNode(root, BSTNode(3))
insertNode(root, BSTNode(9))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(12))
insertNode(root, BSTNode(0))

inOrderTraversal(root)

'''
# No es necesario que se inicialize el root
root2 = None
root2 = insertNode2(root2, BSTNode(5))
root2 = insertNode2(root2, BSTNode(7))
root2 = insertNode2(root2, BSTNode(3))
root2 = insertNode2(root2, BSTNode(9))
root2 = insertNode2(root2, BSTNode(1))
root2 = insertNode2(root2, BSTNode(12))
root2 = insertNode2(root2, BSTNode(0))

inOrderTraversal(root2)

f = findIterative(root2, 12)
print(f[0].data)
print(f[1].data)
'''
root = None
insertNode(root, BSTNode(5))
insertNode(root, BSTNode(7))
insertNode(root, BSTNode(3))
insertNode(root, BSTNode(9))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(12))
insertNode(root, BSTNode(0))
'''



'''
             15
          /      \    
         /         \
       11           18
     /   \         /   \
    9     13     17     19
   / \   /  \   /         \
 4   10 12  14 16         20

'''

def insertNode(root, node):

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
