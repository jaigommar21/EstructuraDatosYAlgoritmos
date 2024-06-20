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

    # Method for setting the data
    def setData(self, data):
        self.data = data

    # Method for getting the data
    def getData(self):
        return self.data

    # Get left child of a node
    def getLeft(self):
        return self.left

    # Get right child of a node
    def getRight(self):
        return self.right


def mi_suma(a, b):
    return a+b


if __name__ == "__main__":
    
    print(mi_suma(3,4))






'''
if __name__ == "__main__":

    print("Estoy en mi_libreria.py")
'''
