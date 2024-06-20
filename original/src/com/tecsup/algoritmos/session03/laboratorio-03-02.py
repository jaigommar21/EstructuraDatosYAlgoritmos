# Node of a Single Linked List
class Node:

   # Constructor
   def __init__(self):
       self.data = None
       self.next = None

   def setData(self, data):
       self.data = data
  
   def getData(self):
       return self.data
  
   def setNext(self, next):
       self.next = next
  
   def getNext(self):
       return self.next

'''
Node4
---------
| 40 |   |
---------

    NodeX       N0            N1              N2              N3
  ------     ---------      ---------      ---------       --------- 
  | 3 |N0|   | 0 | N1|     | 10 | N2|     | 20 | N3 |      | 30 | None   |   
  -------   ---------      ---------      ---------       --------- 
    ^ 
    |
    head 
    ------------   length  ------------------------------------------

Features:
 head --> Address of first element
 length --> Numbers of element

'''



# Node of a Single Linked List
class LinkedList :

   # Constructor
   def __init__(self):
       self.head = None
       self.length = 0

   def print(self):
       node = self.head
       while node != None:
           print(node.data, end =" => ")
           node = node.next
       print("NULL")

   # Insert an item at the begin
   def insertAtBegin(self,data):

       newNode = Node()
       newNode.setData(data)

       if self.length == 0:
           self.head = newNode
       else:
           newNode.setNext(self.head)
           self.head = newNode

       self.length += 1

   # Method for inserting a new node at
   # the end of a Linked List
   def insertAtEnd(self,data):

       newNode = Node()
       newNode.setData(data)

       current = self.head

       # Looking the end element
       while current.getNext() != None:
           current = current.getNext()

       current.setNext(newNode)
       self.length += 1



# Creacion de lista enlazada
ll =  LinkedList()
ll.print()

# Agrego al inicio el valor de 10
ll.insertAtBegin(10)
ll.print()

# Agrego al inicio el valor de 20
ll.insertAtBegin(20)
ll.print()

# Agrego el final valor de 30
ll.insertAtEnd(30)
ll.print()

# Agrego el final valor de 40
ll.insertAtEnd(40)
ll.print()

# Agrego al inicio el valor de 50
ll.insertAtBegin(50)
ll.print()


