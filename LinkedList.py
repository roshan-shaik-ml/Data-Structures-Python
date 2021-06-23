class Node:

    def __init__(self, data = None, next = None):

        self.data = data
        self.next = next
    
class LinkedList:

    def __init__(self):

        self.head = None
    
    def createLL(self):

        payload = input("Enter payload: ") 
        while payload != '':

            newNode = Node(payload)
            if self.head == None:

                self.head = newNode
                newNode.next = None
            else:

                current = self.head
                while current.next != None:
                    current = current.next
                
                current.next = newNode
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
        newNode.next = temp
        self.head = newNode
        
    def insertEndLL(self):

        current = self.head
        payload = input("Enter payload: ")
        newNode = Node(payload)

        while(current.next != None):

            current = current.next
        current.next = newNode
    def deleteBegLL(self):

        self.head = self.head.next
        # in progress
    
    def deleteEndLL(self):

        current = self.head
        while(current.next.next != None):

            current = current.next
        
        current.next = None

    def insertMiddleLL(self):

        position = int(input("Enter the position: "))
        payload = input("Enter the payload: ")
        newNode = Node(payload)
        current = self.head
        
        for i in range(1, position-1):

            current = current.next
        
        temp = current.next
        current.next = newNode
        newNode.next = temp
    
    def deleteMiddlelLL(self):

        position = int(input("Enter the position: "))

        current = self.head
        for i in range(1, position-1):

            current = current.next
        frontPtr = current.next.next

        current.next = frontPtr

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