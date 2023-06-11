# find the second lowest number in a list

def second_lowest_number(mylist):
    # Initialize these variables with the largest possible numbers
    lowest = float('inf') # Used to represent positive infinity in python
    second_lowest = float('inf') + 1
    for i in mylist:
        if i < lowest:
            # swap the values
            second_lowest, lowest = lowest, i
        if i > lowest and i < second_lowest:
            second_lowest = i
    return second_lowest
print(second_lowest_number([1, 3, -3, -5, 0, 43, 3, -2, -1000, -100]))