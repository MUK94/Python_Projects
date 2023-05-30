def binary_search(arr, target):
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 
        
        if arr[mid] == target:
            print(f"Target number is {target} and found at index {mid}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

array_list = [100, 10, 11, 15, 2, 5, 8, 200, 12, 16, 23, 38, 56, 72, 91]
target_num = 16
search_value = binary_search(array_list, target_num)

if search_value == -1:
    print("Target not found in this list")

