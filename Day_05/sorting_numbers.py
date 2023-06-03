# Sorting numbers in Ascending Order
def bubble_sort(num):
    n = len(num)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
                swapped = True
        if not swapped:
            break

# Example usage
num_list = [7, 2, 5, 1, 9, 3, 0, 4]
bubble_sort(num_list)
print(num_list)