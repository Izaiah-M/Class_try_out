
def check_if_sorted(arr):
    isSorted = False
    i = 1

    while i < len(arr):
        if(arr[i] < arr[i - 1]):
            isSorted = True
        i += 1
    
    if not isSorted:
        print("List is sorted!")
    else:
        print("Not Sorted!")


test_list = [1, 4, 5, 8, 10]
check_if_sorted(test_list)