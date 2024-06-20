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
    
    return root

'''
         5
       /  \
      3     7
     / \   / \
    1  2  6   9

1
2
3
5
6
7
9
'''

#'''
# Insercion de código
root = None
node_0 = BSTNode(5)
node_1 = BSTNode(7)
node_2 = BSTNode(3)
node_3 = BSTNode(1)
node_4 = BSTNode(2)
node_5 = BSTNode(6)
node_6 = BSTNode(9)

#root = insertNode(root,node_0)
root = node_0
insertNode(root,node_1)
insertNode(root,node_2)

print("root.data =",root.data)
print("root.left.data =",root.left.data)
print("root.right.data =",root.right.data)

import tree as t
t.printLevelOrder(root)

# root = insertNode(root,node_0)
# root = insertNode(root,node_1)
# root = insertNode(root,node_2)
# root = insertNode(root,node_3)
# root = insertNode(root,node_4)
# root = insertNode(root,node_5)
# root = insertNode(root,node_6)

listado = [12,3,4,1,8,-9,5,20]


#inOrderTraversal(root)
print("fin")


def hola(cont=0): 
    if cont==10: 
        return "fin" 
    else: 
        cont = cont+1 
        print("prueba antes de poner a la pila", cont)
        hola(cont) 
        print("prueba despues de sacarlo de la pila", cont)

#hola(3)
#'''


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
    
    return root

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
    return root

def buildBSTFromArray(list):
    '''
    Build Binary Search Tree
    from Array
    :return:
    '''
    root = None

    for item in list:
        if list.index(item) == 0:
            root = BSTNode(item)
        else:
            insertNode(root, BSTNode(item))
    return root

#    root = BSTNode(5)
#    insertNode(root, BSTNode(0))
#    return root


import tree as t

'''
if __name__ == '__main__':

    # Get tree
    #root = buildBST()

    # Build manual BST
    root = buildManualBST()

    # Build BST from Array
    # list = [5,7,3,9,1,12,0,17,18]
    #list = [4,17,12,8,100]
    #root = buildBSTFromArray(list)
    
    # Find min value
    # nodeMinValue = findMin(root)
    # print("Min value [Recursive mode] : %d" % nodeMinValue.data)

    # Find max value
    # nodeMaxValue = findMax(root)
    # print("Max value [Recursive mode] : %d" % nodeMaxValue.data)
 
    # Print In Order Traversal
    #print("Print In Order Traversal :")
    #inOrderTraversal(root)

    t.printLevelOrder(root)

#'''
