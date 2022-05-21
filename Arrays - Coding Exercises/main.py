
"""
/*
 * Largest Element
 * Implement a function that takes array of integers as input and returns the largest element.
 * Sample Input
 * -3 4 1 2 3
 * -1 -2 -3 -3 8
 * Sample Output
 * 4
 * 8
 * Explanation: for test case one, 4 is the largest integer in the array.
 * Similarly for test case two, 8 is the largest integer in the array.
 */
"""
l = [-1, -2, -3, -3, 8]


def largest_element(l):
    largest = l[0]
    for i in range(1, len(l)):
        largest = max(largest, l[i])

    return largest

print(largest_element(l))


"""
/*
 * Lower Bound
 * Given an array of integers A (sorted) and an integer Val.
 * Implement a function that takes A and Val as input parameters and returns the lower bound of Val.
 * Note: If Val is not present in array, then lower bound of a given integer means integer which is just smaller than given integer.
 * Otherwise Val itself is the answer.
 * If Val is less than smallest element of array A then return '-1' in that case.
 * Example 1:
 * A = [-1, -1, 2, 3, 5]
 * Val= 4
 * Answer: 3
 * Since 3 is just smaller than 4 in the array.
 * Example 2:
 * A = [1, 2, 3, 4, 6]
 * Val= 4
 * Answer: 4
 * Since 4 is equal to 4.
 */
"""
l = [1, 2, 3, 4, 6]
val = 0


def lower_bound(l, val):
    start = 0
    end = len(l) - 1
    lower = -1

    while start <= end:
        mid = (start + end) // 2
        if l[mid] == val:
            return val
        elif l[mid] < val:
            lower = l[mid]
            start = mid + 1
        else:
            end = mid - 1

    return lower

print(lower_bound(l, val))

"""
/*
 * Sorted Pair Sum
 * Given a sorted array and a number x, find a pair in array whose sum is closest to x.
 * Input Format
 * In the function an integer vector and number x is passed.
 * Output Format
 * Return a pair of integers.
 * Sample Input
 * {10, 22, 28, 29, 30, 40}, x = 54
 * Sample Output
 * 22 and 30
 */
"""

l = [10, 22, 28, 29, 30, 40]
x = 54


def closest_pair(l, x):
    start = 0
    end = len(l) - 1
    closest = float('inf')
    p1 = None
    p2 = None

    while start < end:
        abs_diff = abs(l[start] + l[end] - x)
        if abs_diff < closest:
            closest = abs_diff
            p1 = l[start]
            p2 = l[end]

        if l[start] + l[end] > x:
            end -= 1
        else:
            start += 1
    return p1, p2


p1, p2 = closest_pair(l, x)
print(f"{p1} {p2}")

"""
/*
 * K-Rotate
 * Given an integer vector and a value k, your task is to rotate the array k-times clockwise.
 * Input Format
 * In the function an integer vector and number k is passed.
 * Output Format
 * Return an integer vector.
 * Sample Input
 * {1, 3, 5, 7, 9}, k = 2
 * Sample Output
 * {7, 9, 1, 3, 5}
 * Explanation
 * After 1st rotation - {9, 1, 3, 5, 7}
 * After 2nd rotation - {7, 9, 1, 3, 5}
 */
"""

l = [1, 3, 5, 7, 9]
k = 2

def k_rotate(l, k):
    output = list()
    start = len(l) - k

    for i in range(start, len(l)):
        output.append(l[i])
    for i in range(start):
        output.append(l[i])

    return output

print(k_rotate(l, k))