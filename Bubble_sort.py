nums = [5, 2, 9, 1, 5, 6]

"""To help us swap our elements"""
def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
  
"""To help us sort our elements"""
def bubble_sort(arr):
  for el in arr:
    for el in range(len(arr) - 1):
        if arr[el] > arr[el + 1]:
          swap(arr, el, el + 1)


"""********TESTING***********"""
print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))