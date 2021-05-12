class Node:

    def __init__(self, key, value, prev = None, next = None):

        self.key = key
        self.value = value
        self.prev = prev 
        self.next = next
    
class DoubleLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def insert(self, key, value, cacheLimit):

        newNode = Node(key, value)

        # insert at head

        if self.head == None:

            self.head = newNode
            self.tail = newNode 
        
        else:

            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        return newNode

    def repositionNode(self, node):
        
        if node.prev != None:
            # Most recent accessed element is towards tail
            previousNode = node.prev
            nextNode = node.next 

            previousNode.next = nextNode 
            nextNode.prev = previousNode

            # Insert at tail
            node.prev = self.tail
            self.tail.next = node
            node.next = None

            self.tail = node
        else:  

            self.head = self.head.next

            node.prev = self.tail
            self.tail.next = node
            node.next = None 
            self.tail = node

    def delete(self):

        if self.head != self.tail:
            
            node = self.head
            self.head = node.next
            self.head.prev = None

        else:
            
            node = self.head
        
        return node.key

    def display(self):

        ptr = self.head
        while ptr != None:

            print("(", ptr.key," : ", ptr.value, ")", end = " ")
            ptr = ptr.next
        print()


    def printHead(self):

        print(self.head.key, self.head.value)