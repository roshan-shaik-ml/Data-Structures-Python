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
        self.heap = MinHeap(cacheLimit)

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

        node = self.heap.extractMin()
        print(node.key, ":", node.value, node.count)
        self.heap.heapify()


    def put(self, key, value):

        if len(self.hashmap) + 1 <= self.cacheLimit:

            if self.hashmap.get(key) == None:

                node = Node(key, value, 1)
                self.hashmap[key] = [key, node]
                self.heap.insert(node)
                # intialize the count to one at insertion 
                
            else:

                self.hashmap[key].value = value
     
        else:

            self.removeLFU()
            node = Node(key, value, 1)
            self.hashmap[key] = [key, node]
            self.heap.insert(node)

    def displayHeap(self):

        self.heap.display()
