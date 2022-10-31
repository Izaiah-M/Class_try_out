
def reverse(arr):
    rev = []
    for item in range(len(arr) - 1, -1, -1):
        
        rev.append(arr[item])
    return rev

arr = [2, 6, 9, 10]
print(reverse(arr))