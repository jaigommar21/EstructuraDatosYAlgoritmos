'''
Created on Oct 01, 2021
@author: jgomezm
@version: 1.0
'''
#"""
#nros = [21,14,199,23,1]
nros = [x for x in range(1800000,0,-1)]

#print(nros)
print(min(nros))  # BST ==> Binary Search Tree
#print(max(nros))
#"""

class BinaryTreeNode:

    def __init__(self, data, 
                left = None, 
                right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child

"""
Ejemplo :

        "Genero"
            |
     -----------------
     |               |
"Masculino"      "Femenino"

"""

nodo_root = BinaryTreeNode("Genero")
nodo_left = BinaryTreeNode("Masculino")
nodo_right = BinaryTreeNode("Femenino")

# Una solución 1
nodo_left = BinaryTreeNode("Masculino")
nodo_right = BinaryTreeNode("Femenino")
nodo_root = BinaryTreeNode("Genero", nodo_left, nodo_right)

# Una solución 2
nodo_root=BinaryTreeNode("Genero")
nodo_left=BinaryTreeNode("Masculino")
nodo_right=BinaryTreeNode("Femenino")

nodo_root.left=nodo_left
nodo_root.right=nodo_right




nodo1 = NodoLE("4")

nodo2 = NodoLE("5")

nodo1.next = nodo2
