from MaxHeap import MaxHeap
from MinHeap import MinHeap

def solution(arr):

    maxheap = MaxHeap(len(arr))
    minheap = MinHeap(len(arr))

    for element in arr:

        maxheap.insert(element)
        minheap.insert(element)
    
    minimum = minheap.extractMin()
    while minimum % 2 != 0:

        minimum *= 2
        minheap.insert(minimum)
        minimum = minheap.extractMin()
    
    maximum = maxheap.extractMax()
    while maximum % 2 == 0:
        
        maximum //= 2
        maxheap.insert(maximum)
        maximum = maxheap.extractMax()

    return (maximum - minimum)

if __name__ == "__main__":

    # arr = list(map(int, input().split()))
    arr = [2,10,8]
    solution(arr)