
def countingSort(arr):

    frequency = [0] * 11

    for index in range(0, len(arr)):

        frequency[arr[index]] += 1
    
    index = 0
    index1 = 0
    while index < len(frequency):

        if frequency[index] != 0:
            
            arr[index1] = index    
            index1 += 1
            frequency[index] -= 1

        else:

            index += 1
        
    return arr

if __name__ == "__main__":

    arr = [4, 3, 2, 3, 2, 1, 7, 8, 5, 9]
    
    arr = countingSort(arr)
    print(arr)
