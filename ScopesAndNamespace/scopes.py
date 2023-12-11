global result


# by function
def fact(n):
    """calculate n ! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


# by recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    global result
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus1 + n_minus2
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(12):
    print(i, fib(i), "\t", fibonacci(i))
