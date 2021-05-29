import sys
class Stack:

    def __init__(self, size = sys.maxsize ) -> None:
        
        self.stack = []
        self.size = size
        self.top = -1
    
    def push(self, element):

        self.top += 1
        if self.top < self.size:

            self.stack.append(element)
        else:

            print("Stack Overflow")

    def pop(self):

        if self.isEmpty():

            print("Stack Underflow")
        else:
            element = self.stack[self.top]
            self.top -= 1
            self.stack.pop()
            return element
    
    def peek(self):

        if not self.isEmpty():
            return self.stack[self.top]

        else:

            print("Stack is Empty")
    
    def isEmpty(self):

        if self.top == -1:

            return True
        else:

            return False