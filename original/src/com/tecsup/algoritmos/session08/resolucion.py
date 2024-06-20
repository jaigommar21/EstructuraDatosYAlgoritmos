'''
Created on Mar 11, 2019
@author: jgomezm
'''
class BinaryTreeNode(object):

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child


'''

        1
        |
    -------- 
    |       |
    2       3


'''

left = BinaryTreeNode(2)
right = BinaryTreeNode(3)
tree = BinaryTreeNode(1, left, right)


tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)


'''


                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7

 
'''
