def heapify(arr, size, index):

    largest = index
    right = 2 * index + 1
    left = 2 * index + 2

    if left < size and arr[largest] < arr[left]:

        largest = left

    if right < size and arr[largest] < arr[right]:

        largest = right
    
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
    
        heapify(arr, size, largest)

def heapsort(arr):
    
    size = len(arr)

    #building a max heap   
    for i in range(size//2 - 1, -1, -1):

        heapify(arr, size, i)

    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
if __name__ == "__main__":

    arr = [12, 3, 1, 2, 22, 88, 11]
    heapsort(arr)

    print(arr)