
from util.tree import BinaryTreeNode

"""
Ejercicio 1 :
            1
            |
       ------------
      |            |
      2            3

"""

nodo_root = BinaryTreeNode(1)  # optional, could call tree
node_left = BinaryTreeNode(2)  
node_right = BinaryTreeNode(3)  

nodo_root.left = node_left
nodo_root.right = node_right

"""
Ejercicio 2:

            +
            |
       ------------
      |            |
      2            3

"""
