# def fibonacci(arr, elements):
#     return [arr[-1] + arr[-2] ]
#
# assert fibonacci([1, 1], 5) == [1, 1, 2, 3, 5]
# assert fibonacci([3, 2], 5) == [3, 2, 5, 7, 12]
# assert fibonacci([1, 1], 1) == [1]
# assert fibonacci([300, 200], 0) == []

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(5)
