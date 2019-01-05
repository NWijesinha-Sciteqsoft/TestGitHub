'''
Created on Jan 3, 2019

@author: nwijesinha

This exercise is to learn to traverse a tree
Traversal is a process to visit all the nodes of a tree and may print their values too.
There are three ways which we use to traverse a tree
- In-order Traversal
- Pre-order Traversal
- Post-order Traversal
This exercise is to learn about Post-Order Traversal
In this traversal method, the root node is visited last, hence the name. 
First we traverse the left subtree, then the right subtree and finally the root node.
We should always remember that every node may represent a subtree itself.

'''


# create constructor for class
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Define insert function for the tree
    def insert(self, data):
        if self.data:
            # Node has a data element
            if data < self.data:
                # check if data value passed is less than node data element
                if self.left is None:
                    # check if node left value is empty then create new node and add the pointer to the new node to left value
                    self.left = Node(data)
                else:
                    # node left value is not empty then call the insert function by passing the data for the left side of the tree
                    self.left.insert(data)
            elif data > self.data:
                # check if data value is greater than the node data element
                if self.right is None:
                    # check if node right value is empty then create a new node and add pointer to the new node to right value
                    self.right = Node(data)
                else:
                    # node right value is not empty then call the insert function by passing the data for the right side of the tree
                    self.right.insert(data)
        else:
            # Node does not have data then assign the passed data element to the Node data element
            self.data = data
        
    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()
            
    # Postorder traversal
    # Left -> Right -> Root
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.postorderTraversal(root))
