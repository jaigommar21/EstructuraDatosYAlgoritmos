"""

      2
      |
 -----------  
 |    |    | 
 3    4    6    

"""

from util.tree import TreeNode

def findSum(root):
    if(root == None):
        return 0
    return root.data + \
        findSum(root.firstChild) + \
        findSum(root.nextSibling)


if __name__ == '__main__':

    root = TreeNode(2)
    root.nextSibling = TreeNode(3)
    root.nextSibling.nextSibling = TreeNode(4)
    root.nextSibling.nextSibling.nextSibling = TreeNode(6)

    print(findSum(root))
    print(root.findSum(root))

'''

Ejercicio : Calcular la suma del siguiente 
            arbol generico-

           17
       /   |  \
     /     |    \
    3       4     5 
  / | \     |
 3  4  5    10 

'''
