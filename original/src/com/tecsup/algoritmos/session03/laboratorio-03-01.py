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


mi_nodo = Node()
#       data   next
#     ---------------
#     | None | None | 
#     ---------------
print("data={} ,next={}".format(mi_nodo.getData(), mi_nodo.getNext()))
print(mi_nodo)

mi_nodo.setData(100)
#       data   next
#     ---------------
#     | 100 | None | 
#     ---------------
print("data={} ,next={}".format(mi_nodo.getData(), mi_nodo.getNext()))
print(mi_nodo)


#'''
node1 = Node()

#       data   next
#     ---------------
#     | None | None | 
#     ---------------

node1.setData(10)

#       data   next
#     ---------------
#     |  10  | None | 
#     ---------------


node2 = Node()

#       data   next
#     ---------------
#     | None | None | 
#     ---------------

node2.setData(20)
#       data   next
#     ---------------
#     |  20  | None | 
#     ---------------


# node1 --> None y  node2 --> None
#        node1                        node2
#     ---------------           -----------------
#     | 10   | None |           | 20   | None   |
#     ---------------           -----------------

node1.setNext(node2)
# node1 --> node2 --> None 
#       node1                                      node2
#     --------------------------           -----------------
#     | 10   | Apunta al node2 |  ---->    | 20   | None   |
#     --------------------------           -----------------


print("----------------------")
print("node1.data -->",node1.getData())
print("node1.next -->",node1.getNext())
print("----------------------")
print("node2.data -->",node2.getData())
print("node2.next -->",node2.getNext())
#'''