class Node:

    def __init__(self, data = None, left = None, right = None):

        self.data = data
        self.left = None
        self.right = None
    
    def insertNode(self, data):
        
        if data != None:
            if data < self.data:

                if self.left == None:

                    self.left = Node(data) 

                else:

                    self.left.insertNode(data)
            elif data > self.data:

                if self.right == None:

                    self.right = Node(data)

                else:

                    self.right.insertNode(data)
        else:

            self.data = data

    def preorder(self, node):

        if node == None:

            return 
        
        else:

            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):

        if node == None:

            return 
        else:

            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    
    def replaceMinNode(self, node):

        while node.left != None:

            node = node.left
        
        return node 

    def deleteNode(self, node, key):

        if node == None:
            return node
         
        if  key < node.data:
            node.left = self.deleteNode(node.left, key)
        elif key > node.data:
            node.right = self.deleteNode(node.right, key)
        
        else:

            if node.left == None:
                
                temp = node.right
                node = None
                return temp

            elif node.right == None:
                
                temp = node.left
                node = None
                return temp

            temp = self.minValueNode(node.right)
            node.key = temp.key
            node.right = self.deleteNode(node.right, temp.key)
        return node

    def postorder(self, node):

        if node == None:

            return
        else:

            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

if __name__ == "__main__":

    root = Node(10)
    root.insertNode(12)
    root.insertNode(8)
    root.insertNode(2)
    root.insertNode(6)
    root.inorder(root)
    root = root.deleteNode(root, 8)
    root.inorder(root)


    

