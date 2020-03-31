#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions? we have to loop
    through the items and check items next to each other.
    TODO: Memory usage: 0(1) Why and under what conditions? we are not
    allocating memory to run this program """
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items)):
        if i+1 < len(items):
            if items[i] > items[i+1]:
                # print(items[i], items[i+1])
                return False
    return True

# print("is it sorted: ", is_sorted([2, 4, 8, 10, 12, 19, 29]))

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n)^2 Why and under what conditions? we have 2 for loops
    that iterates through the given list and swap every item unitl every element in
    the loop is sorted
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
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
bubble_sort([1, 2, 4, 7, 9])
# def selection_sort(items):
#     """Sort given items by finding minimum item, swapping it with first
#     unsorted item, and repeating until all items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Find minimum item in unsorted items
#     # TODO: Swap it with first unsorted item
#
#
# def insertion_sort(items):
#     """Sort given items by taking first unsorted item, inserting it in sorted
#     order in front of items, and repeating until all items are in order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Take first unsorted item
#     # TODO: Insert it in sorted order in front of items
