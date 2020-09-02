
arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
# arr2 = [4, 7, 1, 3, 6, 9, 10]


def linear_search(arr, target):
    # Check index = to target
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    new_arr = sorted(arr)
    # variables to track search ranges
    right_side = 0  # starts at 0 index
    left_side = len(new_arr) - 1  # starts at end of arr

    while left_side >= right_side:
        middle_index = (right_side + left_side) // 2
        middle = new_arr[middle_index]
        if target == middle:
            return middle_index
        if target > middle:
            right_side = middle_index + 1
            if target == middle:
                return right_side

        if target < middle:
            left_side = middle_index - 1
            if target == middle:
                return left_side

    return -1


# lin_search = linear_search(arr1, -9)
# print(lin_search)


bin_search = binary_search(arr1, 5)
print(bin_search)
