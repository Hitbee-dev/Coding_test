def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

data = [1,3,2,8,4,6,7,9,5]
print(quicksort(data))
