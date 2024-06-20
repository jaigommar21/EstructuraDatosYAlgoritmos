'''
Created on Mar 11, 2019
@version: 1.1
@update: Oct 8, 2021
@author: jgomezm
'''
class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child


"""
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
