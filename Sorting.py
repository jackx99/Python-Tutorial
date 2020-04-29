# Hello Guys
# Today lesson is Sorting a list. We are going to learn Selection Sort.
# How selection sort work? a list is sorted by selecting elements in the list, one at a time, and moving
# them to their proper positions. This algorithm finds the location of the smallest element in the unsorted portion
# of the list and moves it to the top of the unsorted portion of the list. The first time we locate the smallest item
# in the entire list; the second time we locate the smallest item in the list starting from the second
# element in the list; and so on.

# I'm going to show a presentation, How sorting is done.
"""
Redo Programming Exercise of Searching for a sorted list.
"""

# Let's start
def selectionSort(list, list_length):
    temp = 0
    smallestKey = 0
    key = 0
    minKey = 0
    for key, _ in enumerate(list):
        smallestKey = key # we assume that first key is the smallest element
        minKey = key + 1 # we start to look for comparison of the smallest element from key 1 to list length
        while minKey < list_length:
            if list[minKey] < list[smallestKey]: # If evaluates to true,
                smallestKey = minKey # Then the smallestKey value is updated to smaller than smallest
            minKey += 1
        # Swaps these values to implement the selection sort algorithm
        temp = list[smallestKey]
        list[smallestKey] = list[key]
        list[key] = temp 
    return list


list = [71, 29, 67, 18, 92, 4, 49, 48, 86, 40]
print(selectionSort(list, len(list)))