class Node:

    def __init__(self, data = None, prev = None, next = None ):

        self.data = data
        self.next = None
        self.prev = None
    
class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None
    
    def createLL(self):

        payload = input("Enter payload: ") 
        while payload != '':

            newNode = Node(payload)
            if self.head == None:

                newNode.prev = None
                self.head = self.tail = newNode
                newNode.next = None
            else:

                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = None
                self.tail = newNode
                
            payload = input("Enter payload: ")

    def printLL(self):

        current = self.head
        while current:

            print(current.data, end = "  ")
            current = current.next
        print()

    def insertBegLL(self):

        temp = self.head
        payload = input("Enter payload: ")
        newNode = Node(payload)
        
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        
        
        
    def insertEndLL(self):

        payload = input("Enter payload: ")
        newNode = Node(payload)

        newNode.next = None
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode


    def deleteBegLL(self):

        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        del(temp)

    
    def deleteEndLL(self):

        toDeleteNode = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del(toDeleteNode)


    def insertMiddleLL(self):

        position = int(input("Enter the position: "))
        payload = input("Enter the payload: ")
        newNode = Node(payload)
        current = self.head
        
        for i in range(1, position):

            current = current.next
        
        temp = current.next
        
        current.next = newNode
        newNode.prev = current
        newNode.next = temp
        temp.prev = newNode
    
    def deleteMiddlelLL(self):

        position = int(input("Enter the position: "))

        current = self.head
        for i in range(1, position):

            current = current.next
        

        prevNode = current.prev
        nextNode = current.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        del(current) 

if __name__ == "__main__":

    ll = LinkedList()
    while True:

        print("******Single Linked List******")
        print("\t1. Create Linked List")
        print("\t2. Display")
        print("\t3. Insert Beginning")
        print("\t4. Insert Between")
        print("\t5. Insert End")
        print("\t6. Delete Beginning")
        print("\t7. Delete Between")
        print("\t8. Delete End")
        print("\t9. Exit")

        op = int(input("Insert operation number: "))
        if op == 1:
            ll.createLL()
        elif op == 2:
            ll.printLL()
        elif op == 3:
            ll.insertBegLL()
        elif op == 4:
            ll.insertMiddleLL()
        elif op == 5:
            ll.insertEndLL()
        elif op == 6:
            ll.deleteBegLL()
        elif op == 7:
            ll.deleteMiddlelLL()
        elif op == 8:
            ll.deleteEndLL()
        elif op == 9:
            break
        else:
            print("Option Invalid")


