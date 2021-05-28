import sys

class MinHeap:
    
    def __init__(self, size):
        
        self.maxsize = size
        self.size = 0 # current size
        self.heap = [0] * (size + 1)
        self.front = 1
        self.heap[0] = -1 * sys.maxsize
    
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
    
    def minHeapify(self, position):
        
        if not self.isLeaf(position):
            
            left = self.leftChildIndex(position)
            right = self.rightChildIndex(position)
            
            if (self.heap[position] > self.heap[left] or
                self.heap[position] > self.heap[right]):
                    
                if (self.heap[left] < self.heap[right]):
                    
                    self.swap(position, left)
                    self.minHeapify(left)
                
                else:
                    
                    self.swap(position, right)
                    self.minHeapify(right)

    def insert(self, element):
        
        if self.size >= self.maxsize:
            
            return

        self.size += 1 
        self.heap[self.size] = element
        
        current = self.size
        
        while (self.heap[current] < self.heap[self.parent(current)]):
            
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def extractMin(self):
        
        minimum = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1 
        self.minHeapify(self.front)
    
        return minimum