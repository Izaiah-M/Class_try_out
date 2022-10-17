def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n-1): 
    
        for j in range(0, n-i-1): 
  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                print("Rounds " + str(arr))
  

arr = [4, 1, 3, 9, 20, 21, 6, 21, 14, 25] 
  
bubbleSort(arr)