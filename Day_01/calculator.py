'''
1. Define Operators handled by the Calculator
    Addition, Soustraction, Multiplication, Division, Square root
2. Display Options to the user to select one Operator
    (A) - Addition
    (B) - Soustraction
    (C) - Multiplication
    (D) - Division
    (E) - Square Root
    
    
3. Implement each Function 
    Number of inputs/ two or args
    Validate user input
    User to enter the numbers
    Print output

4. Implement a function to restart or exit the program
    Enter 0 to restart the program
    Enter something else to exit
''' 
# --------- Implementation ----------
from math import sqrt

# Implement Functions
def add_num(num1, num2):
    result = num1 + num2
    print("{} plus {} is equal to {}".format(num1, num2, result))

def sub_num(num1, num2):
    result = num1 - num2
    print("{} minus {} is equal to {}".format(num1, num2, result))
    
def mul_num(num1, num2):
    result = num1 * num2
    print("{} multiplied {} is equal to {}".format(num1, num2, result))
    
def div_num(num1, num2):
    if num2 == 0:
        print("Cannot divide by O")
    else:
        result = num1 / num2
        print("{} divided by {} is equal to {}".format(num1, num2, result))

def squareRoot_num(num):
    if num < 0:
        print("Please enter a positive number")
    else:
        result = round(sqrt(num), 2)
        print("Square root of {} is equal to {}".format(num, result))

# User interaction start Here
def show_operators():
    print("---------////// CALCULATOR //////----------")
    print("What do you want to perform? Choose a letter")
    print("============== ============ ============== ")
    print("A: Addition (+)")
    print("B: Soustraction (-)")
    print("C: Multiplication (*)")
    print("D: division (/)")
    print("E: Squart Root (√)")
    user_choice = str(input("Choose a  letter: "))
    return user_choice

choice = show_operators()

# Handle User Input
def user_input():
    if choice == "a" or choice == "A":
        num1 = int(input("Enter num1:"))
        num2 = int(input("Enter num2:"))
        add_num(num1, num2)
    elif choice == "b" or choice == "B":
        num1 = int(input("Enter num1:"))
        num2 = int(input("Enter num2:"))
        sub_num(num1, num2)
    elif choice == "c" or choice == "C":
        num1 = int(input("Enter num1:"))
        num2 = int(input("Enter num2:"))
        mul_num(num1, num2)
    elif choice == "d" or choice == "D":
        div_num(num1, num2)
    elif choice == "e" or choice == "E":
        num = int(input("Enter a number: "))
        squareRoot_num(num)
    else:
        exit()

user_input() 
  