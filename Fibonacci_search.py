
def FibonacciGen(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGen(n-1) + FibonacciGen(n + 1)

def fibonnaci_search(arr, x):

    n = 0
    while FibonacciGen(n) < len(arr):
        n = n + 1

        offset = -1

        while(FibonacciGen(n) > 1):
            i = min(offset + FibonacciGen(n-2), len(arr) - 1)

            if (x > arr[i]):
                n = n - 1
                offset = i
            elif (x < arr[i]):
                n = n -2
            else:
                return i
        
        if (FibonacciGen(n - 1) and arr[offset + 1] == x):
            return offset + 1
        
        return -1

arr = [22, 24, 25, 30, 50, 10]
x = 25

print(fibonnaci_search(arr, x))


