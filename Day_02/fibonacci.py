def fibo(number):
    series = []
    # num1, num2 = 0, 1    
    num1 = 0
    num2 = 1
    while(len(series) < number):
        series.append(num1)
        # num1, num2 = num2, num1 + num2
        temp = num1
        num1 = num2
        num2 = temp + num1
    return series

num = int(input("Enter a Number: "))
print(fibo(num))
    