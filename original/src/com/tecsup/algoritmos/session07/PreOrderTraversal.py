
# from BinaryTreeNode import BinaryTreeNode


# Pre-order iterative traversal. The nodes'
# values arc appended to the result list
# in traversal order
def preOrderIterative(root, result):

    if not root:
        return

    stack = []
    stack.append(root)

    while stack:

        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


##

class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child


#  Preorder Traversal : DATA - LEFT  - RIGHT
def preOrderRecursive(root, result):

    if not root:                          # BASE CASE
        return

    result.append(root.data)               # D ATA
    preOrderRecursive(root.left, result)   # L EFT 
    preOrderRecursive(root.right, result)  # R IGHT

#  Inorder Traversal : LEFT - DATA - RIGHT
def inOrderRecursive(root, result):

    if not root:                          # BASE CASE
        return

    inOrderRecursive(root.left, result)   # L EFT 
    result.append(root.data)              # D ATA
    inOrderRecursive(root.right, result)  # R IGHT

#  Postorder Traversal : LEFT  - RIGHT - DATA
def postOrderRecursive(root, result):

    if not root:                          # BASE CASE
        return

    postOrderRecursive(root.left, result)   # L EFT 
    postOrderRecursive(root.right, result)  # R IGHT
    result.append(root.data)                # D ATA


'''
Binary Tree

                  Estudiante
                      |
            ----------------------
            |                     | 
         Aprobado            Desaprobado  
                

'''

if __name__ == '__main__':

    childrenLeft = BinaryTreeNode("Aprobado")
    childrenRight = BinaryTreeNode("Desaprobado")
    root = BinaryTreeNode("Estudiante",childrenLeft,childrenRight)

    result = []                      # Store result
    #preOrderRecursive(root, result)
    #inOrderRecursive(root, result)
    postOrderRecursive(root, result)
    print(result)



'''
Binary Tree

                      1
                      |
            ----------------------
            |                     | 
            2                     3  
                
     --> 1 2 3
'''


'''
Binary Tree : Preorder Traversal

                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7

     --> 1 2 4 5 3 6 7
'''



#result = []
#preOrderIterative(root, result)
#print(result)