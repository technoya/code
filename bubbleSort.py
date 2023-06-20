def bubbleSort(arr):
	n = len(arr)
	
	swapped = False

	for a in range(n-1):
		
		for j in range(0, n-a-1):

		
			if arr[j] > arr[j + 1]:   
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			
			return

arr = [1,32,435,65,8,5,8,34,74,7]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
