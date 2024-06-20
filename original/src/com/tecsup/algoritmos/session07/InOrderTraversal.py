
from BinaryTreeNode import BinaryTreeNode

# In-order recursive traversal. The
# nodes' values are appended to the
# result list in traversal order
def inOrderRecursive(root, result):

    if not root:
        return

    inOrderRecursive(root.left, result)
    result.append(root.data)
    inOrderRecursive(root.right, result)


# In-order iterative traversal. The nodes'
# values are appended to the result list
# in traversal order
def inOrderIterative(root, result):

    if not root:
        return

    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node. left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

'''
Binary Tree

                  Estudiante
                      |
            ----------------------
            |                     | 
         Aprobado            Desaprobado  
     
'''

childrenLeft = BinaryTreeNode("Aprobado")
childrenRight = BinaryTreeNode("Desaprobado") 
root = BinaryTreeNode("Estudiante",childrenLeft,childrenRight)


result = []
inOrderRecursive(root, result)
print(result)

result = []
inOrderIterative(root, result)
print(result)



'''
Binary Tree : Inorder Traversal

                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7

     --> 4 2 5 1 6 3 7 
'''
