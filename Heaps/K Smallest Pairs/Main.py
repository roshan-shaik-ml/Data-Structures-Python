import sys
from MinHeap import MinHeap
from MinHeap import Node

def solution(arr1, arr2, k):

        heap = MinHeap(len(arr1)*len(arr2))
        for index1 in range(0, len(arr1)):

            for index2 in range(0, len(arr2)):

                pairSum = arr1[index1] + arr2[index2]
                heap.insert(Node(pairSum, index1, index2))

        result = []
        for i in range(0, k):

            node = heap.extractMin()
            pair = [arr1[node.index1], arr2[node.index2]]
            result.append(pair)

        print(result)


    print(result)

def testHeap():

    arr = [12, 2, 33, 4, 5, 14, 8]
    heap = MinHeap(7)
    for i in arr:

        heap.insert(i)
    
    print(heap.heap)



if __name__ == "__main__":

    # arr1 = list(map(int, input().split()))
    # arr2 = list(map(int, input().split()))

    arr1 = []
    arr2 = []
    
    k = int(input())
    solution(arr1, arr2, k)
    

    # testHeap()