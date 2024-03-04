
# Merge Sort Algorithm

Merge Sort is a divide-and-conquer algorithm that sorts an array by dividing it into halves, sorting the halves, and then merging them back together. This README provides an overview of how Merge Sort works and includes a Python implementation.

## Overview

Merge Sort follows a divide-and-conquer strategy:

1. **Divide**: The array is divided into two halves.
2. **Conquer**: Each half is recursively sorted.
3. **Combine**: The sorted halves are merged together to produce a single sorted array.

This process continues recursively until the base case is reached, where the array to be sorted is of length 1 (or empty), at which point it is considered sorted.

## Algorithm

The Merge Sort algorithm can be broken down into two main functions:

- `merge_sort(arr)`: The main function that sorts an array.
- `merge(left, right)`: A helper function that merges two sorted arrays into a single sorted array.

### `merge_sort(arr)`

```python
def merge_sort(arr):
    if len(arr) <= 1:  # Base Case
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursive call on the left half 
    right = merge_sort(arr[mid:])  # Recursive call on the right half

    return merge(left, right)  # Merge the sorted halves
