
from MinHeap import MinHeap

class Node:

    def __init__(self, key, value, count) -> None:
        
        self.key = key
        self.value = value
        self.count = count

class LFU:

    def __init__(self, cacheLimit) -> None:
        
        self.hashmap = {}
        self.cacheLimit = cacheLimit
        self.heap = heap(cacheLimit)

    def get(self, key):

        if self.hashmap.get(key) != None:

            pair = self.hashmap[key]
            value = pair[1].value
            pair[1].count += 1
            print(key, value)

            self.heap.heapify()

        else:

            print(-1)

    def removeLFU(self):

        value = self.heap.extractMin()
        print(value)


    def put(self, key, value):

        if len(self.hashmap) <= self.cacheLimit:

            if self.hashmap.get(key) != None:

                self.hashmap[key] = [key, Node(key, value, 1)]
                # intialize the count to one at insertion 
                
            else:

                self.hashmap[key].value = value
                
        else:

            self.removeLFU()
