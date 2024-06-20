from util.tree import BinaryTreeNode


def findMaxRecursive(tree): 
      
    # Base case  
    if tree is None:  
        return float('-inf')  # Mininum value

    data = tree.data 
    left_max = findMaxRecursive(tree.left)  
    right_max = findMaxRecursive(tree.right)  
        
    return max([data, left_max, right_max])




root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)


#print("findMaxRecursive  ",findMaxRecursive(root))


max_data = findMaxRecursive(root)
print(max_data)

