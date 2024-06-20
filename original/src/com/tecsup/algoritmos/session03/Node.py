'''
Created on Mar 11, 2019
@author: jgomezm
'''

# Node of a Single Linked List
class Node:

    # Constructor
    def __init__(self):
        self.data = None
        self.next = None
    
    # Method for setting the data
    def setData(self, data):
        self.data = data
    
    # Method for getting the data
    def getData(self):
        return self.data
    
    # Method for setting the pointer
    def setNext(self, next):
        self.next = next
    
    # Method for getting the pointer
    def getNext(self):
        return self.next
    
    # return true if the node point to another node
    def hasNext(self):
        return self.next != None
