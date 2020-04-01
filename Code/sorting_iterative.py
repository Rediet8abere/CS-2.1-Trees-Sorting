#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions? we have to loop
    through the items and check items next to each other.
    TODO: Memory usage: We are not allocating memory to run this function"""

    for i in range(1, len(items)):
        if items[i] < items[i-1]:
            return False
    return True

# print("is it sorted: ", is_sorted([1, 2, 4, 7, 9]))

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n)^2 Why and under what conditions? we have 2 for loops
    that iterates through the given list and swap every item unitl every element in
    the loop is sorted
    TODO: Memory usage: O(1) Why and under what conditions? the only memory we need
    to allocate is for temp"""
    # to keep track of iteration not useful for the algorithm itself
    count = 0
    n = len(items)
    # to get out early if the items are sorted
    sorted = False
    while not sorted:
        sorted = True
        for j in range(1, n):
            if items[j] < items[j-1]:
                sorted = False
                temp = items[j-1]
                items[j-1] = items[j]
                items[j] = temp
            count += 1
        # so that we don't compare the item in the end of list that are already sorted
        n -= 1
    print(count, items)
# bubble_sort([1, 2, 4, 7, 9])
def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n)^2 Why and under what conditions? we have to loop
    through the items twice to to compare and rearrange item
    TODO: Memory usage: O(1) Why and under what conditions? we are allocating memory
    for only temp"""
    # to keep track of iteration not useful for the algorithm itself
    count = 0

    for i in range(len(items)):
        min = i
        for j in range(i+1, len(items)):
            if items[j] < items[min]:
                # print(items[j], items[min])
                min = j
            count += 1
        temp = items[i]
        items[i] = items[min]
        items[min] = temp

    print("items", items, count)

# [1, 7, 4, 9, 2]
# selection_sort([9, 7, 4, 1, 2])

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for i in range(len(items)):
        key = items[i] 
        j=i-1
        while j>=0 and key<items[j]:
            items[j+1]=items[j]
            j-=1
        items[j+1]=key

    print("items: ", items)

insertion_sort([9, 7, 4, 1, 2])
