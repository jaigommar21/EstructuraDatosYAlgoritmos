
list0 = [1,2,3,4]


def about():
   print("Acerca del curso")

class Node:

   def __init__(self): # constructor
      self.data = None
      self.next = None

   def about(self):
      print("Acerca del curso : Node ", self.data)

mi_nodo = Node()
#mi_nodo.data = 15
print(mi_nodo)
print(mi_nodo.data)
print(mi_nodo.next)

mi_nodo.about() # llama a un metodo de una clase
about()   # Llamada a una función

# LISTA ENLAZADA = 20,40,60

"""
 
   item_1              item_2           item_3

data |  next
--------------
  20 | item_2       40 | item_3  ---->   60 | ? 

"""
item_1 = Node()
item_1.data = 20  

item_2 = Node()
item_2.data = 40

item_3 = Node()
item_3.data = 60

item_1.next = item_2 
item_2.next = item_3
item_3.next = None    # opcional





print("--")










class Node:

    def __init__(self):
       self.data = None
       self.next = None

    def about(self):
        print("Acerca de -->",self.data)

node = Node()
node.data = 21
node.about()   # metodo de una clase

# LISTA ENLAZADA = 20,40,60

"""
 
   item_1        item_2         item_3

  20 | ?          40 | ?          60 | ? 

"""
item_1 = Node()
item_1.data = 20  
print(item_1.data)
print(item_1.next)

item_2 = Node()
item_2.data = 40

item_3 = Node()
item_3.data = 60




# El atributo next tiene la direccion 
# del objeto item_2
item_1.next = item_2 

# Enlazar el item_2 con el item_3
item_2.next = item_3

# item_3 a donde apunta?
item_3.next = None
