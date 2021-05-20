
def preprocess(arr, maximumBits):

    for index in range(0, len(arr)):

        arr[index] = "0" * (maximumBits - len(str(arr[index]))) + str(arr[index])

    return arr
    
def radixSort(arr):

    bucket = [[None]] * 10
    maximumBits = len(str(max(arr)))

    arr = preprocess(arr, maximumBits)
    
    print(arr)
    for bit in range(1, maximumBits):

        for index in range(0, len(arr)):

            bucket[int(arr[index][-(bit)])].append(arr[index])
            print(int(arr[index][-(bit)]))
            


if __name__ == "__main__":

    arr = [829, 1111, 280, 421, 994, 325, 682]

    arr = radixSort(arr)