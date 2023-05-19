# Check weather the reversed number or string is equal to the number
# 1. Get user input 
# 2. Reversed user input
# 3. Compare user input vs reversed user input

user_input = (input("Enter a string or a number: "))

def reverse_input(input1):
    reversed_input1 = input1[::-1]
    return reversed_input1

def check_palyndrome(input2, reversed_input2):   
    if input2 == reversed_input2:
        print("{} is a palyndrome".format(input2))
    else:
        print("{} is not a palyndrome".format(input2))

check_palyndrome(user_input, reverse_input(user_input))

