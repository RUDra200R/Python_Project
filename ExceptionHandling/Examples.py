def factorial(n):
    """calculate  n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("THis program calculate factorial that large")
    print("what are doing dividing by zero")


print("Program terminates")
