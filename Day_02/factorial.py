# 1. Using Recursion
def factorial(n):
    if n < 0:
        print("Factorial of negative numbers do not exist!")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
print(factorial(5))

# 2. Using for loops
def find_factorial(n):
    if n < 0:
        return False
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = i * factorial
        print(factorial)

find_factorial(3)