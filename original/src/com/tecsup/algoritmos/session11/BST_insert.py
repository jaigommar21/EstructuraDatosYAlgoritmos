# BST Node

import tree as t

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
    
    #return root

if __name__ == "__main__" :
    
    root=BSTNode(5)
    root.left=BSTNode(3)
    root.right=BSTNode(7)
    root.left.left=BSTNode(2)
    root.left.right=BSTNode(4)
    root.right.left=BSTNode(6)
    root.right.right=BSTNode(8)
    
    """
    insertNode(root, BSTNode(3))
    insertNode(root, BSTNode(9))
    insertNode(root, BSTNode(1))
    insertNode(root, BSTNode(12))
    insertNode(root, BSTNode(0))
    insertNode(root, BSTNode(11))
    insertNode(root, BSTNode(20))
    insertNode(root, BSTNode(2))
    """
    buf=[]
    t.printLevelOrder(root, buffer = buf)
    print(buf)