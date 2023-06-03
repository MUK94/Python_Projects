def largest_number(myList):
    num = myList[0]
    for i in myList:
        if i > num:
            num = i
    return num

largest_num = largest_number([1, 4, 6, 9, 900, 0, 89, 44444, 2, 97])
print(largest_num)
   
