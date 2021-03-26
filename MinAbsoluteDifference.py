class BST:

    def __init__(self, data = None, left = None, right = None):

        self.data = data
        self.left = None
        self.right = None

    def insertNode(self, key):

        if self.data != None:

            if key < self.data:
                
                if self.left == None:
                    self.left = BST(key)
                else:
                    self.left.insertNode(key)

            elif key > self.data:
                
                if self.right == None:

                    self.right = BST(key)
                else:
                    self.right.insertNode(key)
        else:

            self.data = key

    def inorder(self, node):

        if node != None:

            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    
    def preorder(self, node):

        if node != None:
            
            print(node.data, end = " ")
            self.preorder(node.left)
            self.preorder(node.right)
            

def minDifference(node, key):

    tempPtr = node
    minVal = 0
    print()
    while tempPtr != None:

        if tempPtr.data <= key:

            minVal = tempPtr.data
            tempPtr = tempPtr.right
        else:
            break

    print(minVal)

if __name__ == "__main__":

    root = BST()
    root.insertNode(9)
    root.insertNode(17)
    root.insertNode(4)
    root.insertNode(3)
    root.insertNode(6)
    root.insertNode(5)
    root.insertNode(7)
    root.insertNode(17)
    root.insertNode(22)
    root.insertNode(20)
    root.preorder(root)
    minDifference(root, 18)class BST:

    def __init__(self, data = None, left = None, right = None):

        self.data = data
        self.left = None
        self.right = None

    def insertNode(self, key):

        if self.data != None:

            if key < self.data:
                
                if self.left == None:
                    self.left = BST(key)
                else:
                    self.left.insertNode(key)

            elif key > self.data:
                
                if self.right == None:

                    self.right = BST(key)
                else:
                    self.right.insertNode(key)
        else:

            self.data = key

    def inorder(self, node):

        if node != None:

            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    
    def preorder(self, node):

        if node != None:
            
            print(node.data, end = " ")
            self.preorder(node.left)
            self.preorder(node.right)
            

def minDifference(node, key):

    tempPtr = node
    minVal = 0
    print()
    while tempPtr != None:

        if tempPtr.data <= key:

            minVal = tempPtr.data
            tempPtr = tempPtr.right
        else:
            break

    print(minVal)

if __name__ == "__main__":

    root = BST()
    root.insertNode(9)
    root.insertNode(17)
    root.insertNode(4)
    root.insertNode(3)
    root.insertNode(6)
    root.insertNode(5)
    root.insertNode(7)
    root.insertNode(17)
    root.insertNode(22)
    root.insertNode(20)
    root.preorder(root)
    minDifference(root, 18)
