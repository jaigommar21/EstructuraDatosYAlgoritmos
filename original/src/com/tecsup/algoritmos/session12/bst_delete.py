# BST Node

class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def find(root, data, parent = None, pos = None):
    '''
    Method to find data in BST
    Rparam root:
    :return:
    '''
    currentNode = root

    if currentNode == None:
        return [parent, None, None]
    else:
        if data == currentNode.data:
            return [parent, currentNode , pos]
        if data < currentNode.data:
            return find(currentNode.left, data, parent=currentNode , pos ="left")
        else:
            return find(currentNode.right,data, parent=currentNode, pos ="right")

def findMin(root):
    '''
    Find the minimum value. Recursive mode
    :param root:
    :return:
    '''
    currentNode = root
    if currentNode.left == None:
        return currentNode
    else:
        return findMin(currentNode.left)

def findMin(root, parent):
    if root.left:
	    return findMin(root.left, root)
    else:
	    return parent, root

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

def deleteNode2(root, data):

    parent_node_found, node_found, pos = find(root, data, parent=None, pos=None)

    print(parent_node_found.data)
    print(node_found.data)
    
    if node_found:

        if getNroChildren(node_found) == 0 :
        
            print("dont have children")
            
            if pos == "left": parent_node_found.left = None            
            if pos == "right": parent_node_found.right = None            
        
        elif getNroChildren(node_found) == 1 :
        
            print("have one children")
        
            if node_found.left:
        
                if pos == "left": parent_node_found.left = node_found.left            
                if pos == "right": parent_node_found.right = node_found.left
        
            if node_found.right:
        
                if pos == "left": parent_node_found.left = node_found.right            
                if pos == "right": parent_node_found.right = node_found.right
        
        elif getNroChildren(node_found) == 2 :

            print("have two children")
            print(node_found.data)
            print(pos)
            print(parent_node_found.left)
            print(parent_node_found.right)            
            
            _parent_node_min, _node_min = findMin(node_found.right, node_found)
            _parent_node_min.left = None

            deleteNode2(_parent_node_min, _node_min)

            _node_min.left = node_found.left
            _node_min.right = node_found.right

            if pos == "left": parent_node_found.left = _node_min           
            if pos == "right": parent_node_found.right = _node_min
        
        
        else :
        
            print("Node corrupted")
    else:
        print("Not found data", data)
    
def getNroChildren(node):
    nro = 0 
    if node.left : nro +=1
    if node.right : nro +=1
    return nro

def deleteNode(root, data):
	
    if root.data == data:
	
        if root.right and root.left: 
            # "hard" case --> 3.3
            pass
        else:
			# "easier" case --> 3.1 and 3.2
            if root.left:
                return root.left  
            else:
                return root.right  
    else:
        if root.data > data: 
            if root.left:
                root.left = deleteNode(root.left, data)
        else: 
            if root.right:
                root.right = deleteNode(root.right, data)
    return root


def deleteNodeOrigin(root, data):
	
    if root.data == data:
		# found the node we need to delete
        if root.right and root.left: 
			# get the successor node and its parent 
            [psucc, succ] = findMin(root.right, root)
			# splice out the successor
			# (we need the parent to do this) 
            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right					
			# reset the left and right children of the successor
            succ.left = root.left
            succ.right = root.right
            return succ                
        else:
			# "easier" case
            if root.left:
                return root.left  # promote the left subtree
            else:
                return root.right  # promote the right subtree 
    else:
        if root.data > data:  # data should be in the left subtree
            if root.left:
                root.left = deleteNodeOrigin(root.left, data)
			# else the data is not in the tree 
        else:  # data should be in the right subtree
            if root.right:
                root.right = deleteNodeOrigin(root.right, data)
    return root



def buildBSTFromArray(list):
    '''
    Build Binary Search Tree
    from Array
    :return:
    '''
    root = None

    for item in list:
        if list.index(item) == 0:
            root = BSTNode(item)
        else:
            insertNode(root, BSTNode(item))
    return root


'''
         5
       /  \
      3     7
     / \   / \
    1  2  6   9

'''

import tree as t

if __name__ == '__main__':

    # Get tree
    #root = buildBST()

    # Build BST from Array
    #list = [5,7,3,9,1,12,0,17,18]
    list = [3,5,1,2,4,6]
    root = buildBSTFromArray(list)
    t.printLevelOrder(root)
    print("")

    delete_data = 5
    deleteNode2(root,delete_data )
    t.printLevelOrder(root)
    print("")

    delete_data = 1
    deleteNode2(root,delete_data )
    t.printLevelOrder(root)
    print("")

    delete_data = 6
    deleteNode2(root,delete_data )

    t.printLevelOrder(root)
    print("")

    delete_data = 4
    deleteNode2(root,delete_data )

    t.printLevelOrder(root)
    print("")

