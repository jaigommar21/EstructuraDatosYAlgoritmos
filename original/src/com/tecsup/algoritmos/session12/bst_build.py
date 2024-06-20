# BST Node

class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insertNode(root, node):

    '''
    Insert a node in BST
    '''
    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)
    
    return root

'''
         5
       /  \
      3     7
     / \   / \
    1  2  6   9

1
2
3
5
6
7
9
'''

#'''
# Insercion de código
root = None
node_0 = BSTNode(5)
node_1 = BSTNode(7)
node_2 = BSTNode(3)
node_3 = BSTNode(1)
node_4 = BSTNode(2)
node_5 = BSTNode(6)
node_6 = BSTNode(9)

#root = insertNode(root,node_0)
root = node_0
insertNode(root,node_1)
insertNode(root,node_2)

print("root.data =",root.data)
print("root.left.data =",root.left.data)
print("root.right.data =",root.right.data)

import tree as t
t.printLevelOrder(root)


# Ejercicio 1 : 
#     crear un árbol con estos datos : 15, 12, 1, 10, 9, 7

print("-"*40)
#'''
# Insercion de código
root = None
node_0 = BSTNode(15)
node_1 = BSTNode(12)
node_2 = BSTNode(1)
node_3 = BSTNode(10)
node_4 = BSTNode(9)
node_5 = BSTNode(7)
#root = insertNode(root,node_0)
root = node_0
insertNode(root,node_1)
insertNode(root,node_2)
insertNode(root,node_3)
insertNode(root,node_4)
insertNode(root,node_5)

import tree as t
t.printLevelOrder(root)
print("")

print("-"*40)

node_0 = BSTNode(10)
node_1 = BSTNode(7)
node_2 = BSTNode(15)
node_3 = BSTNode(1)
node_4 = BSTNode(9)
node_5 = BSTNode(12)
root = node_0
insertNode(root,node_1)
insertNode(root,node_2)
insertNode(root,node_3)
insertNode(root,node_4)
insertNode(root,node_5)
t.printLevelOrder(root)
print("")


print("-"*40)

root = None
node_0 = BSTNode(12)
node_1 = BSTNode(15)
node_2 = BSTNode(9)
node_3 = BSTNode(1)
node_4 = BSTNode(10)
node_5 = BSTNode(7)
#root = insertNode(root,node_0)
root = node_0
insertNode(root,node_1)
insertNode(root,node_2)
insertNode(root,node_3)
insertNode(root,node_4)
insertNode(root,node_5)
import tree as t
t.printLevelOrder(root)
print("")
# TIP : Usar un arreglo para almacenar los números
print("*"*40)
Arreglo=[10,7,15,1,9,12]
ArregloNodo=[]
for i in Arreglo:
  ArregloNodo.append(BSTNode(i))
for x in ArregloNodo:
    if x!= ArregloNodo[0]:
        insertNode(ArregloNodo[0],x)
t.printLevelOrder(ArregloNodo[0])
print("")



# Ejercicio 2 : 
#     crear un arbol con 5 números aleatorios en 0 y 100


