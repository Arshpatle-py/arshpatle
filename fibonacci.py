# Fibonacci using Recursion
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Fibonacci using Dynamic Approach (Iterative)
def fib_dynamic(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Main Program
n = int(input("Enter the value of n: "))

print("Fibonacci using Recursion :", fib_recursive(n))
print("Fibonacci using Dynamic Approach :", fib_dynamic(n))
