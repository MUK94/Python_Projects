# Function for adding the sum of all element in a list
# It must receive a list
# Initialize result variable to 0
# Loop through the list 
# Add element to result in each iteration
 
def sum_list_numbers(mylist):
    result = 0
    for i in mylist:
        result += i
    return result 

sum = sum_list_numbers((1, 3, 5, 6, 8))
print(sum)