def fibonacci(index):

    if index== 1 or index == 2:
        value = 1
    else:
        value = fibonacci(index-1) + fibonacci(index-2)
    return value

print(fibonacci(6))