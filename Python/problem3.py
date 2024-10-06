# Write a program to find the largest and smallest number in an array.

def find_largest_and_smallest(arr):
    if not arr:
        return None, None
    largest = smallest = arr[0]
    for num in arr[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

# Example usage
array = [3, 5, 1, 2, 4, 8]
largest, smallest = find_largest_and_smallest(array)
print(f"Largest: {largest}, Smallest: {smallest}")