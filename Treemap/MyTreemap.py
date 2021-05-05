'''

'''

class Node:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:

    def __init__(self):

        self.root = None

    def insertNode(self, key, value):

        newNode = Node(key, value)
        
        if self.root == None:

            self.root = newNode
            return self.root
        
        ptr = self.root

        while True:

            if key < ptr.key:

                if ptr.left == None:

                    ptr.left = newNode
                    break
                else:

                    ptr = ptr.left
                    continue
            elif key == ptr.key:

                ptr.value = value
                break

            else:

                if ptr.right == None:

                    ptr.right = newNode
                    break
                else:
                    
                    ptr = ptr.right
                    continue
        return newNode

    def returnNode(self, key):
        
        ptr = self.root

        while ptr != None:

            if key < ptr.key:

                ptr = ptr.left
            elif key == ptr.key:

                print(ptr.key, ": ", ptr.value, "\n")
                return
            else:

                ptr = ptr.right
        
        print("Key not found\n")

    def inorder(self, node):

        if node != None:

            self.inorder(node.left)
            print(node.key, ": ", node.value)
            self.inorder(node.right)

    
class Treemap:

    def __init__(self):

        self.tree = BST()

    def put(self, key, value):

        self.tree.insertNode(key, value)
    
    def get(self, key):

        self.tree.returnNode(key)
    
    def entrySet(self):

        self.tree.inorder(self.tree.root)

