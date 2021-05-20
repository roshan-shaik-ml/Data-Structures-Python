def insertionSort(arr):

    size = len(arr)
    for i in range(1, size):

        key = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] >= key:

            arr[j+1] = arr[j]
            j -= 1
            print(arr)

        arr[j+1] = key

if __name__ == "__main__":

    arr = [21, 3, 12, 1, 33, 2, 44]
    insertionSort(arr)
    print(arr)

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j > 0  and arr[j] > key:
        
            arr[j+1] = arr[j]
            j -= 1
            print(arr)
        arr[j+1] = key
        print(arr)
    
    print(arr)
if __name__ == "__main__":

    arr = [2, 21, 7, 14, 5, 6, 77]
    insertionSort(arr)