import concurrent.futures
import random
import os

# Basic function to find maximum element in an array
def find_max(arr):
    if not arr or not isinstance(arr, list):  # Handle empty or invalid input
        return "Invalid input"
    
    try:
        max_element = arr[0]
        for num in arr:
            if num > max_element:
                max_element = num
        return max_element
    except TypeError:
        return "Array contains non-numeric values"

# Function to find max element and its index
def find_max_with_index(arr):
    if not arr or not isinstance(arr, list):
        return "Invalid input"
    
    max_element = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i
    return max_element, max_index

# Recursive function to find the maximum element
def find_max_recursive(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], find_max_recursive(arr, n-1))

# Optimized function for sorted arrays
def find_max_optimized(arr):
    if not arr or not isinstance(arr, list):
        return "Invalid input"
    
    if arr == sorted(arr, reverse=True):  # If sorted in descending order
        return arr[0]
    
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Parallel computation for large arrays
def find_max_parallel(arr):
    def chunked_max(sub_array):
        return max(sub_array)
    
    num_workers = 4  # Adjust this based on the number of CPU cores
    chunk_size = len(arr) // num_workers

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(chunked_max, arr[i:i + chunk_size]) for i in range(0, len(arr), chunk_size)]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    
    return max(results)

# Custom comparison function for complex objects
def find_max_custom(arr, key_func):
    if not arr or not isinstance(arr, list):
        return "Invalid input"
    
    max_element = arr[0]
    for item in arr:
        if key_func(item) > key_func(max_element):
            max_element = item
    return max_element

# Test data for the functions
if __name__ == "__main__":
    # Basic test array
    arr = [10, 24, 3, 50, 7]

    # 1. Basic maximum element
    print("Basic max:", find_max(arr))

    # 2. Maximum element with index
    max_element, max_index = find_max_with_index(arr)
    print(f"Max element with index: {max_element} at index {max_index}")

    # 3. Recursive approach
    print("Recursive max:", find_max_recursive(arr, len(arr)))

    # 4. Optimized approach for sorted array
    sorted_arr = [50, 24, 10, 7, 3]
    print("Optimized max:", find_max_optimized(sorted_arr))

    # 5. Parallel computation for large array
    large_arr = [random.randint(1, 1000) for _ in range(1000000)]  # 1 million elements
    print("Parallel max:", find_max_parallel(large_arr))

    # 6. Custom comparison function for complex objects
    people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
    max_person = find_max_custom(people, key_func=lambda x: x['age'])
    print("Person with max age:", max_person)
