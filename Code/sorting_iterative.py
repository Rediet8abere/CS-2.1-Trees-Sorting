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
    # [9, 7, 4, 1, 2]

# print("is it sorted: ", is_sorted([1, 2, 4, 7, 9]))

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: WORST CASE: O(n)^2 Why and under what conditions? we have 2
    for loops that iterates through the given list and swap every item unitl every
    element in the loop is sorted
    BEST CASE: O(n) If we get an almost sorted list then we would have to loop atleast
    n times and get out early.
    TODO: Memory usage: O(1) Why and under what conditions? the only memory we need
    to allocate is for temp"""
    # to keep track of iteration not useful for the algorithm itself
    count = 0
    n = len(items)
    # to get out early if the items are sorted
    # checks if there is a swap
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
    return items

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: WORST CASE & BEST CASE: O(n)^2 Why and under what conditions?
    we have to loop through the items twice to compare and rearrange item
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

    return items



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: WORST CASE: O(n)^2 Why and under what conditions? we have two loops
    that keeps track of where we are in the loop and anothor loop to compare and shift.
    BEST CASE: O(n) same as bubble sort if we get an almost sorted list then we can get
    out early.
    TODO: Memory usage: 4*O(1)~O(1) Why and under what conditions? we are allocating
    memory for key and j"""
    for i in range(len(items)):
        key = items[i]
        j=i-1
        while j>=0 and key<items[j]:
            items[j+1]=items[j]
            j-=1
        items[j+1]=key
    return items
    # print("items: ", items)

insertion_sort([9, 7, 4, 1, 2])
