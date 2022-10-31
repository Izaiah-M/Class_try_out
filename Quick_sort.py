def quicksort(arr):
    length = len(arr)

    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    items_greater = []
    items_lesser = []

    for item in arr:
        if item < pivot:
            items_lesser.append(item)
        else:
            items_greater.append(item)
    
    return quicksort(items_lesser) + [pivot] + quicksort(items_greater)

arr =  [25, 29, 30, 35, 42, 47, 50, 52, 60]

print(quicksort(arr))