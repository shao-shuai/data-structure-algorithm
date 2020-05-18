import random

# A list of integers to sort
arr = [2, 38, 42, 81, 69, 98, 86, 92, 59, 43, 4, 11, 34, 65, 71, 9, 24, 97, 58, 78, 74]

def bubbleSort(arr):	
	# Set up upper bound
	upper = len(arr) - 1

	for i in range(upper, 0, -1):
		for j in range(i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

# Selection sort
for outer in range(len(arr) - 1):
	minn = outer
	for i in range(outer + 1, len(arr)):
		if arr[i] < arr[minn]:
			minn = i
	arr[outer], arr[minn] = arr[minn], arr[outer]


# Insert sort

print(help(max))


