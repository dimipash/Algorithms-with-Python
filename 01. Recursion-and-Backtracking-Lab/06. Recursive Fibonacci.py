def iterative_fib(number):
    fib0 = 1
    fib1 = 1
    result = 0
    for i in range(number - 1):
        result = fib0 + fib1
        fib0 = fib1
        fib1 = result
    return result


n = int(input())
print(iterative_fib(n))
