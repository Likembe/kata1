def find_smallest_subarray_to_sort(arr):
    n = len(arr)
    
    # Check if the array is already sorted
    if all(arr[i] <= arr[i+1] for i in range(n-1)) or all(arr[i] >= arr[i+1] for i in range(n-1)):
        return [0, 0]

    # Find the first and last positions where the array is unsorted
    start, end = 0, n-1
    while start < n-1 and arr[start] <= arr[start + 1]:
        start += 1
    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    # If the array is completely unsorted
    if start == n-1:
        return [0, n-1]

    # Find the min and max in the unsorted subarray
    subarray_min = min(arr[start:end+1])
    subarray_max = max(arr[start:end+1])

    # Extend the subarray to include elements that are out of place
    while start > 0 and arr[start-1] > subarray_min:
        start -= 1
    while end < n-1 and arr[end+1] < subarray_max:
        end += 1

    return [start, end]

# Example usage
arr1 = [1, 2, 3, 6, 4, 4]
arr2 = [1, 1, 1, 1, 1, 1]
arr3 = [1, 2, 3, 4, 4, 6]
arr4 = [6, 4, 4, 3, 2, 1]


print(find_smallest_subarray_to_sort(arr1))  # Output should be [3, 5]
print(find_smallest_subarray_to_sort(arr2))  # Output should be [3, 5]
print(find_smallest_subarray_to_sort(arr3))  # Output should be [3, 5]
print(find_smallest_subarray_to_sort(arr4))  # Output should be [3, 5]

#string sorted from shortest to longest
def sort_strings_by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: len(x))
    return sorted_arr

input_arr = ["Glasses", "Monocles", "Telescopes", "Eyes", "Non", "Microscope"]
result = sort_strings_by_length(input_arr)

print(result)

#string sorted from longest to shortest
def sort_strings_by_length(arr):
    return sorted(arr, key=len, reverse=True)

input_arr = ["Glasses", "Monocles", "Telescopes", "Eyes", "Non", "Microscope"]
sorted_arr = sort_strings_by_length(input_arr)

print(sorted_arr)
