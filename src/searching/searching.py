def linear_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    for i in range(n):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    n = len(arr)

    left = 0
    right = n - 1

    while left <= right:
        # find the midpoint
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # check whether element should be on left or right side of mid
        if arr[mid] < target:
            # toss out left side of the array
            # update our 'left' index
            left = mid + 1
        else:
            # toss out right side of the array
            # update our 'right' index
            right = mid - 1

    return -1  # not found
