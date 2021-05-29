from MinHeap import MinHeap
from MaxHeap import MaxHeap

class solution:

    def __init__(self, array, maxsize, minsize) -> None:
        
        self.maxheap = MaxHeap(maxsize)
        self.minheap = MinHeap(minsize)
        self.array = array

    def insert(self, element):

        if self.maxheap.size == 0 or element < self.maxheap.getMax():

            self.maxheap.insert(element)
        else:

            self.minheap.insert(element)
    
    def rebalance(self):

        if abs(self.minheap.size - self.maxheap.size) >= 2:

            if self.minheap.size < self.maxheap.size:

                element = self.maxheap.extractMax()
                self.minheap.insert(element)
            
            else:

                element = self.minheap.extractMin()
                self.maxheap.insert(element)
        else:
            return 
    
    def getMedian(self):

        if abs(self.minheap.size - self.maxheap.size) == 0:

            element1 = self.maxheap.getMax()
            element2 = self.minheap.getMin()
            return (element1 + element2) / 2
        else:

            element = self.maxheap.getMax()
            return element

    def solve(self):

        for element in self.array:

            self.insert(element)
            self.rebalance()
        
        element = self.getMedian()
        print(element)

if __name__ == "__main__":

    array = [10, 12, 33, 2, 5, 6, 8]
    maxsize = len(array) // 2 if len(array) % 2 == 0 else len(array) // 2 + 1
    minsize = len(array) // 2 
    solve = solution(array, maxsize, minsize)
    solve.solve()