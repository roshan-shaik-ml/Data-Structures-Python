def shellSort(arr):

    n = len(arr)

    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i
 
            while j >= gap and arr[j-gap] > temp:

                arr[j] = arr[j-gap]
                j = gap
                arr[j] = temp

        gap = gap // 2
    return arr

if __name__ == "__main__":

    arr = [12, 3, 44, 5, 6, 66, 88, 0]
    arr = shellSort(arr)
    print(arr)