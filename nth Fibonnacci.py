n = int(input("Enter the nth value:"))

def fib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    else:
        return fib(n-1) + fib(n-2)

print(fib(n))

