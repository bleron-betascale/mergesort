def merge_sort(arr):
    if len(arr) <= 1:  # Base Case
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursive call on the left half 
    right = merge_sort(arr[mid:])  # Recursive call on the right half

    return merge(left, right)  # Merge the sorted halves


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
