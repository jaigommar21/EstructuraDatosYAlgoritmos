'''
Created on Mar 11, 2019
@author: jgomezm
@version: 1.2    April 29,2020
'''

class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child

'''
Binary Tree

                  Estudiante
                      |
            ----------------------
            |                     | 
         Aprobado            Desaprobado  
     

'''

left = BinaryTreeNode("Aprobado")
right = BinaryTreeNode("Desaprobado")
tree = BinaryTreeNode("Estudiante", left, right)


# Pre-order recursivc traversal.
# The nodes' values are appended to
# the result list in traversal order
#  D – L - R
def preOrderRecursive(root, result):

    if not root:
        return

    result.append(root.data)                  # D : data
    preOrderRecursive(root.left, result)      # L : left
    preOrderRecursive(root.right, result)     # R : right

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
tree = BinaryTreeNode(1,childrenLeft,childrenRight )

# Do traversal
result = []
preOrderRecursive(tree, result) # D – L - R
print(result)
