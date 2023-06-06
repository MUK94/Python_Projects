# Initialize a new list to store unique values
# loop through original list, if element present in list of uniq values, pass
# else, append that element to the new list 

def remove_duplicates(myList):
    unique_list = []
    for i in myList:
        if i in unique_list:
            pass
        else:
            unique_list.append(i)
    return unique_list

list = remove_duplicates([1,3,5,1,4,6,6,9, 90, 0, 12.4, "testing", "testing", "Test"])
print(list)