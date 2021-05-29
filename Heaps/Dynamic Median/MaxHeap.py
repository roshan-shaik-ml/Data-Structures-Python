import sys

class MaxHeap:
    
    def __init__(self, size):
        
        self.maxsize = size
        self.size = 0 # current size
        self.heap = [0] * (size + 1)
        self.front = 1
        self.heap[0] = sys.maxsize
    
    def parent(self, position):
        
        return position // 2
    
    def leftChildIndex(self, position):
        
        return position * 2
    
    def rightChildIndex(self, position):
        
        return (position * 2) + 1
    
    def isLeaf(self, position):
        
        if position >= self.maxsize // 2 and position <= self.size:
            
            return True
            
        return False
        
    def swap(self, position1, position2):
        
        self.heap[position1], self.heap[position2] = self.heap[position2], self.heap[position1]
    
    def maxHeapify(self, position):
        
        if not self.isLeaf(position):
            
            left = self.leftChildIndex(position)
            right = self.rightChildIndex(position)
            
            if (self.heap[position] < self.heap[left] or
                self.heap[position] < self.heap[right]):
                    
                if (self.heap[left] > self.heap[right]):
                    
                    self.swap(position, left)
                    self.maxHeapify(left)
                
                else:
                    
                    self.swap(position, right)
                    self.maxHeapify(right)
    def insert(self, element):
        
        if self.size >= self.maxsize:
            
            return

        self.size += 1 
        self.heap[self.size] = element
        
        current = self.size
        
        while (self.heap[current] > self.heap[self.parent(current)]):
            
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def extractMax(self):
        
        maximum = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1 
        self.maxHeapify(self.front)
    
        return maximum

    def getMax(self):

        maximum = self.heap[self.front]
        return maximum