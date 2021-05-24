class MinHeap:


    def __init__(self, maxsize = 1):
    
        self.heap = [None] * (maxsize + 1)
        self.size = maxsize + 1
    
    def insert(self, payload):

        for position in range(1, self.size // 2):

            if self.heap[position] == None:

                self.heap[position] = payload
                return None
            else:   
                leftChildIndex = self.getLeftChild(position)
                rightChildIndex = self.getRightChild(position)
        print(leftChildIndex)
            
                if self.heap[leftChildIndex] == None:

                    self.heap[leftChildIndex] = payload
                    return "insertion done"
                
                elif self.heap[rightChildIndex] == None:

                    self.heap[rightChildIndex] = payload
                    return "insertion done"
    
    def swap(self, index1, index2):

        if self.heap[index1] != None and self.heap[index2] != None:
            
            self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def display(self):

        for i in range(1, self.size // 2):

            print("parent", self.heap[i], "left child", self.heap[2*i], "right child", self.heap[2*i + 1])

    def heapify(self, position = 1):

        leftChildIndex = self.getLeftChild(position)
        rightChildIndex = self.getRightChild(position)

        if (leftChildIndex != None and 
                self.heap[leftChildIndex] != None and self.heap[position] > self.heap[leftChildIndex]):

            self.swap(leftChildIndex, position)
        
        if leftChildIndex != None:
            self.heapify(leftChildIndex)

        if (rightChildIndex != None and 
                self.heap[rightChildIndex] != None and self.heap[position] > self.heap[rightChildIndex]):

            self.swap(rightChildIndex, position)
    
        if rightChildIndex != None:
            self.heapify(rightChildIndex)

    def getMin(self):

        if self.heap[1] != None:
            
            return self.heap[1]
        
        return "heap is empty"
    
    def getLastInserted(self):

        for index in range(self.size - 1, 0, -1):

            if self.heap[index] != None:

                return index

    def extractMin(self):

        minimum = self.getMin()
        lastIndex =  self.getLastInserted()
        
        if lastIndex != 1:

            self.heap[1], self.heap[lastIndex] = self.heap[lastIndex], None

            self.heapify()
        
        return minimum
    
    def parent(self, position):

            return (position - 1) // 2  


    def getLeftChild(self, position):

        if position <= (self.size - 1 ) // 2 :

            return (position * 2)

        return None
    def getRightChild(self, position):

        if position <= (self.size - 1) // 2:
            
            return (position * 2) + 1
        
        return None

if __name__ == "__main__":


    size = 7
    heap = MinHeap(7)
    
    heap.insert(1)
    heap.insert(10)
    heap.insert(7)
    heap.insert(2)
    heap.insert(5)
    heap.insert(3)
    heap.insert(6)

    heap.heapify()
    print(heap.heap[1:])
    minimum = heap.extractMin()
    print(minimum)

    print(heap.heap[1:])
    minimum = heap.extractMin()
    print(minimum)
    heap.display()