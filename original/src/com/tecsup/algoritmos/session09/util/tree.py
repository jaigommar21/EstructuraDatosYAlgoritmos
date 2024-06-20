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


class TreeNode:

    def __init__(self, data=None):
        self.data = data
        self.firstChild = None
        self.nextSibling = None

    def findSum(self, root):
        if(root == None):
            return 0
        return root.data + \
            self.findSum(root.firstChild) + \
            self.findSum(root.nextSibling)