'''
Created on Mar 11, 2021
@author: jgomezm
'''
# Node of a Single Linked List
class Node:

    # Constructor
    def __init__(self):
        self.data = None
        self.next = None

    # return true if thenode point to another node
    def hasNext(self):
        return self.next != None

# Stack Linked List
class StackLinkedList:

    # Constructor
    def __init__(self, data=None):
        self.head = None
        if data:
            for d in data:
                self.push(d)

    def push(self, data):
        temp = Node()
        temp.data = data
        temp.next = self.head
        self.head = temp

    def pop(self):
        if self.head is None:  # la lista enlazada es vacia?
            raise IndexError   # throw new Exception()
            #print(" Underflow Stack ...!")
            #return -1
        temp = self.head.data
        self.head =self.head.next
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.data

    def print( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next
        print("NULL")

    # Get length of linked list
    def listLength(self):

        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.next

        return count

x = [1,21]
our_stack = StackLinkedList()

our_stack.push(1)
our_stack.print()

our_stack.push(21)
our_stack.print()

our_stack.push(100)
our_stack.print()

x = our_stack.pop()
our_stack.print()

x = our_stack.pop()
our_stack.print()

x = our_stack.pop()
our_stack.print()

x = our_stack.pop()
our_stack.print()

#x = our_stack.pop()


our_stack = StackLinkedList()
our_stack.push(1)
our_stack.push(21)
our_stack.push(14)
our_stack.push(31)
our_stack.push(19)
our_stack.push(3)
our_stack.push(99)
our_stack.push(9)

our_stack.print()
print("length : " , our_stack.listLength())


our_stack.print()
print(our_stack.pop())
print("length : " , our_stack.listLength())

our_stack.print()
print(our_stack.pop())
print("length : " , our_stack.listLength())


"""
our_list = ["first", "second", "third", "fourth"]
our_stack = StackLinkedList(our_list)
our_stack.print()
print("length : " , our_stack.listLength())


our_stack = StackLinkedList()
our_stack.push(1)
our_stack.push(21)
our_stack.push(14)
our_stack.push(31)
our_stack.push(19)
our_stack.push(3)
our_stack.push(99)
our_stack.push(9)
our_stack.print()
print("length : " , our_stack.listLength())


print("pop : data <- " ,our_stack.pop())
our_stack.print()
print("length : " , our_stack.listLength())

"""

print("pop : data <- " , our_stack.pop())
our_stack.print()
print("length : " , our_stack.listLength())

print("peek : data <- " , our_stack.peek())
print("peek : data <- " , our_stack.peek())
print("peek : data <- " , our_stack.peek())

print("length : " , our_stack.listLength())
