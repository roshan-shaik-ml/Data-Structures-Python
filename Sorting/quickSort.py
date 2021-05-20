def partition(arr, start, end):

	pivot = start
	low = start + 1
	high = end

	while True:

		while low <= high and arr[low] <= arr[pivot]:
			
			low += 1
		while low <= high and arr[high] >= arr[pivot]:

			high -= 1
		
		if low <= high:
			arr[low], arr[high] = arr[high], arr[low]

		else:
			break

	arr[pivot], arr[high] = arr[high], arr[pivot]

	return high

def quicksort(arr, start, end):

	if start >= end:
		return

	else:
		pi = partition(arr, start, end)
		quicksort(arr, start, pi)
		quicksort(arr, pi+1, end)

if __name__ == "__main__":

	arr = [11, 2, 33, 4, 12, 31]
	quicksort(arr, 0, len(arr)-1)
	print(arr)