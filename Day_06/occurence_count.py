# Use a dictionary where keys to hold the list elements
# And values are the number of occurence
# Loop through the list, if the element(key) is in the dic, then add 1 to the value

def occurence_count(mylist):
    mydic = {}
    for i in mylist:
        if i in mydic:
            mydic[i] += 1
        else:
            mydic[i] = 1
    return mydic

num_count = occurence_count([1, 3, 1, 4, 5])
print(num_count)

    