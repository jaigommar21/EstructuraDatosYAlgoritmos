'''
   Represent Node and Queue
'''
# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.last = None
        self.next = next

    # method for setting the data field of the node
    def set_data(self, data):
        self.data = data

    # method for getting the data field of the node
    def get_data(self):
        return self.data

    # method for setting the next field of the node
    def set_next(self, next):
        self.next = next

    # method for getting the next field of the node
    def get_next(self):
        return self.next

    # method for setting the last field of the node
    def setLast(self, last):
        self.last = last

    # method for getting the last field of the node
    def getLast(self):
        return self.last

    # returns true if the node points to another node
    def has_next(self):
        return self.next != None


class Queue(object):
    def __init__(self, data=None):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        self.lastNode = self.front
        self.front = Node(data, self.front)
        if self.lastNode:
            self.lastNode.setLast(self.front)
        if self.rear is None:
            self.rear = self.front
        self.size += 1

    def queueRear(self):
        if self.rear is None:
            print
            "Sorry, the queue is empty!"
            raise IndexError
        return self.rear.get_data()

    def queueFront(self):
        if self.front is None:
            print
            "Sorry, the queue is empty!"
            raise IndexError
        return self.front.get_data()

    def deQueue(self):
        if self.rear is None:
            print
            "Sorry, the queue is empty!"
            raise IndexError
        result = self.rear.get_data()
        self.rear = self.rear.last
        self.size -= 1
        return result

    def size(self):
        return self.size
