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

# Node of a Single Linked List
class LinkedList :

    # Constructor
    def __init__(self):
        self.head = None 
        self.length = 0

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

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(newNode)
        self.length += 1

    # Method for inserting a new node at any position in a Linked List
    def insertAtPos(self,pos,data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBegin(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count = 0
                    current = self.head
                    while count< pos-1:
                        count+= 1
                        current = current.getNext()

                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length += 1
    
    def listLength(self):

        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def print( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next
        print("NULL")

    def clear( self) :
        self.head = None


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

'''

node1 = Node()

#     ---------------
#     | None | None | 
#     ---------------

node1.setData(10)

#     ---------------
#     | 10   | None | 
#     ---------------

node2 = Node()

#     ---------------
#     | None | None | 
#     ---------------

node2.setData(20)

#     ---------------
#     | 20   | None | 
#     ---------------

node1.setNext(node2)

#       node1                                      node2
#     --------------------------           ------------------
#     | 10   | Apunta al node2 |  ---->    | 20   | None     |
#     --------------------------           ------------------


print("----------------------")
print("node1.data -->",node1.getData())
print("node1.next -->",node1.getNext())
print("----------------------")
print("node2.data -->",node2.getData())
print("node2.next -->",node2.getNext())

'''
# Node of a Single Linked List
class LinkedList2 :
 
   # Constructor
   def __init__(self):
       self.head = None
       self.length = 0
 
   def print( self ):
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
 
       while current.getNext() != None:
           current = current.getNext()
 
       current.setNext(newNode)
       self.length += 1


'''

ej_lista_enlazada = LinkedList2()
ej_lista_enlazada.print()

node1 = Node()
node1.setData(21)  # 2020
ej_lista_enlazada.head = node1
'''

'''
ej_lista_enlazada.insertAtBegin(21)
ej_lista_enlazada.insertAtBegin(2020)

# 21 --> 2020
# 2020 --> 21  *
ej_lista_enlazada.print()

'''

'''
node1 = Node()
node1.setData(19)
ej_lista_enlazada.head = node1
ej_lista_enlazada.print()

ej_lista_enlazada = LinkedList2()
ej_lista_enlazada.print()
ej_lista_enlazada.insertAtBegin(20)
ej_lista_enlazada.print()
ej_lista_enlazada.insertAtEnd(21)
ej_lista_enlazada.print()
ej_lista_enlazada.insertAtEnd(22)
ej_lista_enlazada.print()

'''

# Lista enlazada, de Nodos
#
#      -----------------------------------------------
#      |  VALOR  | DIRECCION DEL SIGUIENTE ELEMENTO  |
#      -----------------------------------------------
#
#


'''
ll = LinkedList()
ll.insertAtBegin(1)
ll.insertAtBegin(2)
ll.insertAtBegin(3)
ll.insertAtBegin(4)
ll.print()
ll.insertAtEnd(5)
ll.insertAtEnd(7)
ll.print()
ll.insertAtPos(3,10)
ll.print()
print(ll.listLength())
ll.clear()
ll.print()
print(ll.listLength())
'''


#Crear un Linked List con los siguiente datos 
#: 10, 20, 30, 40, 41, 42, 43, 44, 45, 50, 51, 52 , 53, 54,

ll = LinkedList()
ll.insertAtBegin(1)
ll.insertAtBegin(2)
ll.insertAtBegin(3)
ll.insertAtBegin(4)
