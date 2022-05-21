# Linear Search - O(n)
def linear_search(arr, key):
    for index, element in enumerate(arr):
        if arr[index] == key:
            return index
    return -1


elements = list(range(10))
print(linear_search(elements, key=5))


# Binary Search - O(logn)
def binary_search(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key: return mid
        elif arr[mid] > key: end = mid - 1
        else: start = mid + 1

    return -1


elements = list(range(10))
print(binary_search(elements, key=5))


# Reverse Array - O(n)
def reverse_array(arr):
    for i in range(len(arr) // 2):
        # Swapping
        temp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = temp

    return arr


elements = list(range(10))
print(elements)
elements = reverse_array(elements)
print(elements)


# Print Pairs - O(n^2)
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print(f"({arr[i]}, {arr[j]})")


elements = list(range(10))
print_pairs(elements)


# Print Subarrays - O(n^3)
def print_subarrays(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j+1):
                print(k, end=" ")
            print()


elements = list(range(10))
print_subarrays(elements)


# Maximum Subarray Sum - Brute Force Approach - O(n^3)
def maximum_subarray_sum_brute_force(arr):
    max_sum = arr[0]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray_sum = 0
            for k in range(i, j+1):
                subarray_sum += arr[k]
            if subarray_sum > max_sum:
                max_sum = subarray_sum

    return max_sum


elements = [1, 2, 3, -5, 7, -7, 3, -1, 4]
print(maximum_subarray_sum_brute_force(elements))


# Maximum Subarray Sum - Prefix Sum Approach - O(n^2)
def max_subarray_sum_prefix_sum(arr):
    prefix_sums = list()
    prefix_sums.append(arr[0])
    for i in range(1, len(arr)):
        prefix_sums.append(prefix_sums[i-1] + arr[i])

    largest_sum = arr[0]

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            subarray_sum = prefix_sums[j] - prefix_sums[i-1] if i != 0 else prefix_sums[j];
            largest_sum = max(largest_sum, subarray_sum)

    return largest_sum


elements = [1, 2, 3, -5, 7, -7, 3, -1, 4]
print(max_subarray_sum_prefix_sum(elements))


# Maximum Subarray Sum - Kadane's Algorithm - O(n)
def max_subarray_sum_kadane_algorithm(arr):
    # Find if we have positive number or not
    # and compute the maximum number
    max_number = arr[0]
    positive_found = False
    for i in range(len(arr)):
        if arr[i] > 0:
            positive_found = True
        if arr[i] > max_number:
            max_number = arr[i]

    # If no positive numbers found, return max negative number
    if not positive_found:
        return max_number

    current_sum = 0
    largest_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum < 0:
            current_sum = 0
        largest_sum = max(largest_sum, current_sum)

    return largest_sum


elements = [1, 2, 3, -5, 7, -7, 3, -1, 4]
print(max_subarray_sum_kadane_algorithm(elements))

# Lists
elements = [1, 2, 3, 4, 5]
print(elements, "of length {}".format(len(elements)))
elements.append(6)
print(elements, "of length {}".format(len(elements)))
elements.pop()
print(elements, "of length {}".format(len(elements)))
index = 0
element = 0
elements.insert(index, element)
print(elements, "of length {}".format(len(elements)))
elements.pop(0)
print(elements, "of length {}".format(len(elements)))
elements.remove(2) # Remove first occurrence of 2
print(elements, "of length {}".format(len(elements)))
elements.reverse() # inplace
print(elements, "of length {}".format(len(elements)))
elements.sort() # inplace
print(elements, "of length {}".format(len(elements)))
print("Index of 3 in array {} is {}".format(elements, elements.index(3)))
print("Count of occurrences of 3 in array {} is {}".format(elements, elements.count(3)))
elements.extend(range(10)) # inplace
print(elements, "of length {}".format(len(elements)))
elements_copy = elements.copy() # shallow copy
print(f"ID of elements array is {id(elements)} and ID of elements copy array is {id(elements_copy)}")
elements.clear() # inplace
print(elements, "of length {}".format(len(elements)))
