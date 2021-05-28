import sys
from MinHeap import MinHeap

def getMinMax(arr):

    i = 0
    minimum, maximum = sys.maxsize, -1

    while i < len(arr) - 1:

        if arr[i] < arr[i+1]:

            if arr[i] < minimum:

                minimum = arr[i]
            
            if arr[i+1] > maximum:

                maximum = arr[i+1]
        else:

            if arr[i+1] < minimum:

                minimum = arr[i+1]

            if arr[i] > maximum:

                maximum > arr[i]


        i = i + 2

    return minimum, maximum

def solution(arr1, arr2, upperbound):

    size1 = len(arr1)
    size2 = len(arr2)

    heap1 = MinHeap(size1)
    heap2 = MinHeap(size2)

    for index in range(0, size1):

        heap1.insert(arr1[index])

    for index in range(0, size2):

        heap2.insert(arr2[index])
    
    
    pairs = []
    



def testHeap():

    arr = [12, 2, 33, 4, 5, 14, 8]
    heap = MinHeap(7)
    for i in arr:

        heap.insert(i)
    
    print(heap.heap)



if __name__ == "__main__":

    # arr1 = list(map(int, input().split()))
    # arr2 = list(map(int, input().split()))

    arr1 = [2, 21, 23, 4, 5, 6]
    arr2 = [31, 33, 22, 11, 28]
    minimum1, maximum1 = getMinMax(arr1)
    minimum2, maximum2 = getMinMax(arr2)

    upperbound = min(minimum1, minimum2) + max(maximum1, maximum2)
    solution(arr1, arr2, upperbound)
    # testHeap()