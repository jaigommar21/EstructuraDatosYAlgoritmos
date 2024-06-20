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

print(tree.data)
print(tree.left.data)
print(tree.right.data)

root = BinaryTreeNode("Genero", nodo_masc, nodo_feme)
