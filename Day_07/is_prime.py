# A prime number is greater than 1 and only divisible by 1 and itself
# 1. Exclude numbers less than 2 
# 2. Exclude numbers that have more than 2 divisors by checking for all numbers from 2 to its square root

def is_prime(num):
    if num < 2:
        print("The number should be greater or equal to 2")

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")

    print(f"{num} is a prime number")

number = int(input("Enter a number: "))
is_prime(number)