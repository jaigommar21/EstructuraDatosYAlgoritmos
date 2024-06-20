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


# node1.next "es None"
# node2.next "es None"

# node1.next apunte al node2
# node2.next "es None"

# node1 --> node2 --> None o NULL
node1.setNext(node2)

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

#     Ejercicio
# 
#       n1                   n2                  n3                n4
#     -----------        -----------         -----------       ----------- 
#     | 10 | n2 |  --->  | 20 | n3 |   --->  | 30 | n4 |  -->  | 40 |    |
#     -----------        -----------         -----------       ----------- 
#


# Node of a Single Linked List
class LinkedList:
 
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
    def insertAtEnd(self,data) : 
 
       newNode = Node()
       newNode.setData(data)
 
       current = self.head
 
       while current.getNext() != None:
           current = current.getNext()
 
       current.setNext(newNode)
       self.length += 1


    def insertAtPos(self,pos,data) :
        
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

    # Free memory
    def clear( self) :
        self.head = None


                    
print("======================")
ll = LinkedList()
ll.print()
ll.insertAtBegin(10)
ll.print()
ll.insertAtBegin(20)
ll.print()

#  10 => 20 => 30 => 40 => NULL


print("====== Parte 4 ===========")

ll = LinkedList()
ll.print()
ll.insertAtBegin(00)
ll.print()
ll.insertAtEnd(10)
ll.print()
ll.insertAtEnd(20)
ll.print()

# Crear un Linked List con los siguiente datos :   
#                50, 51, 52 , 53, 54

print("====== Parte 4 ===========")

ll = LinkedList()
ll.print()
ll.insertAtPos(0,10)
ll.print()
ll.insertAtPos(1,40)
ll.print()
ll.insertAtPos(0,33)
ll.print()
ll.insertAtPos(1,1000)
ll.print()

#
# Crear un Linked List con los siguiente datos :  
# 10, 20, 30, 40,   ==> insercion al inicio
# 41, 42, 43, 44, 45,  ==> insercion al final
# 50, 51, 52 , 53, 54  ==> insercion en una posicion especifica

# 10, 20, 30, 40, 41, 42, 43, 44, 45,  50, 51, 52 , 53, 54 

print("====== Parte 5 ===========")

ll.print()
print("Nro. items =" , ll.length )
ll.clear()
ll.print()


"""
Tengo 3 tipos de arreglos con 10,000 registros

-Estatico
-Dinámico
-Enlazado

¿ Dondé es más fácil agregar un registro 
al final del arreglo para el programador?
CODIGO : Dinámico

¿ Dondé es más fácil agregar un registro 
al final del arreglo para el sistema operativo?

listado = [ n for n in range(11000)] # Ya tengo un espacio


#       n1                   n2                  n3                n1000000000
#     -----------        -----------         -----------         ----------- 
#     | 10 | n2 |  --->  | 20 | n3 |   --->  | 30 | n4 |  .....  | 40 |    |
#     -----------        -----------         -----------         ----------- 

   n1000000001
----------- 
| 11 | ? |
-----------

"""