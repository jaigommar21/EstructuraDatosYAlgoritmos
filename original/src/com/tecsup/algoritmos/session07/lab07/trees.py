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

'''
Binary Tree

                  Estudiante
     
'''
node = BinaryTreeNode("Estudiante")
print("fin")


'''
Binary Tree

                  Estudiante
                      |
            ----------------------
            |                     | 
         Aprobado            Desaprobado  
     
'''

left = BinaryTreeNode("Aprobado")
right = BinaryTreeNode("Desaprobado")
tree = BinaryTreeNode("Estudiante", left, right)

'''
print(tree.getData())
print(tree.getLeft().getData())
print(tree.getRight().getData())
'''

print(tree.data)
print(tree.left.data)
print(tree.right.data)


'''
print(tree.data)
print(tree.left.data)
print(tree.right.data)
'''

'''

class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child
'''



'''
                   TECSUP
                      |
            ----------------------
            |                     | 
           PFR                   CPE  
            |                     | 
        --------              ---------     
       |        |             |        |
  Software    Big Data   Informática   Mineria        

'''

'''

                   TECSUP
                      |
            ----------------------
            |                     | 
         TECSUP 2               TECSUP 1 
        (Arequipa)                | 
                              ---------     
                              |        |
                            Lima     Trujillo        

'''

'''
La salida del cable submarino en Lima se realiza a través
de la estación de Lurin Pueblo , de ahi se comunica con las
estaciones de San Isidro y Lince, La estación de San Isidro se
comunica con las estaciones de Miraflores y Surquillo  , desde 
La estación de Lince se comunica con las estaciones del Cercado
y Magdalena, representar en una arbol estas relaciones 

'''
