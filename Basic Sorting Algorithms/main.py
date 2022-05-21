# Bubble Sort
"""
Bubble Sort - Take larger element to the end by repeatedly swapping the adjacent elements.
"""


l = [2, 3, 5, 3, 7, 8, 4]


def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(0, len(l)-1-i):
            if l[j] > l[j+1]:
                # swapping
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l


print(bubble_sort(l))


# Insertion Sort
"""
Insertion Sort - Insertion sort is similar to playing cards in our hands. Insert the card in its correct position in a sorted part.
"""


l = [2, 3, 5, 3, 7, 8, 4]


def insertion_sort(l):
    for i in range(1, len(l)):
        current = l[i]
        prev = i - 1
        while prev >= 0 and l[prev] > current:
            l[prev+1] = l[prev]
            prev -= 1
        l[prev+1] = current
    return l


print(insertion_sort(l))

# Selection Sort

l = [2, 3, 5, 3, 7, 8, 4]


def selection_sort(l):
    for i in range(len(l) - 1):
        min = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min]:
                min = j
        # swap min and i
        temp = l[min]
        l[min] = l[i]
        l[i] = temp

    return l


print(selection_sort(l))

# Inbuilt Sort

l = [2, 3, 5, 3, 7, 8, 4]
print(l)
l.sort(reverse=True)
print(l)


# Counting Sort
l = [2, 3, 5, 3, 7, 8, 4]


def counting_sort(l):
    # calculate max value
    max = 0
    for element in l:
        if element > max:
            max = element

    # create frequency array
    freq = [0] * (max + 1)
    for i in range(len(l)):
        freq[l[i]] += 1

    # put back the elements in the original array
    j = 0
    for i in range(len(freq)):
        while freq[i]:
            l[j] = i
            freq[i] -= 1
            j += 1

    return l


counting_sort(l)
print(l)