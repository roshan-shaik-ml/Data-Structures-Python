def solve(heap, size):

    for i in range(1, heap.maxsize-1):

        weight1 = heap.extractMax()
        weight2 = heap.extractMax()

        weight = abs(weight1 - weight2)

        heap.insert(weight)
        heap.maxHeapify(1)

    return heap.heap[1]

def printHeap(heap):

    for i in range(0, heap.size):
        print(heap.heap[i])
    
if __name__ == "__main__":

    size = 6
    heap = MaxHeap(size)
    arr = [2,7,4,1,8,1]

    for element in arr:

        heap.insert(element)
    
    print(heap.heap)
    solve(heap, size)
    print(heap.heap)