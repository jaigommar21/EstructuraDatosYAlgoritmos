'''
Created on Mar 10, 2019

@author: jgomezm
@version: 1.3 27/09/2021

'''

# Node of a Single Linked List
class Node:

    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None  

    # return true if thenode point to another node
    def hasNext(self):
        return self.next != None

#
class QueueLinkedLists(object):

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def enQueue(self, data):

        self.tmp = self.rear # apunta al ultimo 
                                  # nodo ingresado

        self.rear = Node(data)    # creo el nodo

        if self.tmp:
            self.tmp.next = self.rear

        if self.front is None:
            self.front = self.rear

        self.size +=1



    def deQueue(self):

        if self.front is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        result = self.front.data
        
        self.front = self.front.next # mueve la referencia del front        
        self.size -=1
        return result

    def queueRear(self):
        if self.rear is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        return self.rear.data

    def queueFront(self):
        if self.front is None:
            print('Sorry, the queue is empty')
            raise IndexError
        return self.front.data

    def getSize(self):
        return self.size

    def print( self ):
        node = self.front
        print("QUEUE :")
        while node != None:
            print(node.data, end =" => ")
            node = node.next
        print("NULL")

if  __name__ == "__main__":

    # Execution
    que = QueueLinkedLists()

    #que.enQueue("Jaime")
    #que.enQueue("Gomez")

#    data = ["first","second","third","fourth",
#            "fifth","sixth","seventh","eighth"]

    data = ["Jaime","Marisol","Juan","Silvia"]

    for item in data:
        print("--------------------------------")
        que.enQueue(item)
        
        #print("Que    --> " , que.getQue())
        # Que  --> third => fourth => fifth => sixth => seventh => eighth => NULL

        que.print() 
        # third => fourth => fifth => sixth => seventh => eighth => NULL
                    
        print("Front  --> " , que.queueFront())
        print("Rear   --> " , que.queueRear())
        print("Size   --> " , que.getSize())

    print("--------------------------------")
    que.deQueue()
    #print("Que    --> " , que.getQue())
    que.print()
    print("Front  --> " , que.queueFront())
    print("Rear   --> " , que.queueRear())
    print("Size   --> " , que.getSize())

    print("--------------------------------")
    que.deQueue()
    #print("Que    --> " , que.getQue())
    que.print()
    print("Front  --> " , que.queueFront())
    print("Rear   --> " , que.queueRear())
    print("Size   --> " , que.getSize())


'''
 Ejercicio  - Crear un cola con una lista enlazada , donde :

 ingresar 5 valores en forma secuencial : "A","E","I","O","U"
             ["A","E","I","O","U"]
 recuperar 2 valores de la cola 
             ["I","O","U"]
 ingresar 3 valores : "1","2","3"
             ["I","O","U","1","2","3"]
 recuperar 1 valor de la cola 
             ["O","U","1","2","3"]

'''

'''
 Ejercicio: Verificar si se requiere hacer modificaciones
 en el método deQueue() en la clase QueueLinkedListsCircular
 para poder obtener el valor desencolado.

 rd = que.deQueue()

 rd deberia almacenar el valor desencolado
'''


'''
- Verificar que al desencolar una cola vacia sale 
  un error....!

- Verificar que al momento de encolar una cola llena NO sale 
  un error al momento de incrementar los datos en la cola !

'''
