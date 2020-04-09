# #!python
import random
from sorting_iterative import selection_sort, insertion_sort

def merge(items1, items2, items):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    Running time: This function is being called recursively and the number of
    times it will be executed is log(n) because we have to split the function log(n)
    times to get to the base case which is 1. After doing so, we need to perform n
    append operation to merge back the items after comparing them. Therefore, the time
    complexity of our function is n*log(n). Adding on that one of for loop runs if either
    items1 or items2 gets done first making the time complexity 2n*log(n) ~ n*log(n)

    Memory usage: no memory usage Why and under what conditions? we are not allocating
    memory instead we are rearranging what's in items"""
    # to keep track of where we are in items list
    print(" ")
    print("In MERGE")
    print("items: ", items)
    print("items1: ", items1)
    print("items2: ", items2)
    print(" ")
    index = 0
    left, right = 0, 0
    merged = []
    # while we have not reached either the end of items1 or items2
    while left < len(items1) and right < len(items2):
        if items1[left] <= items2[right]:
            print("items1[left]: ", items1[left], "items2[right]: ", items2[right])
            merged.append(items1[left])
            # items[index] = items1[left]
            left+=1
        elif items2[right]  < items1[left]:
            merged.append(items2[right])
            # items[index] = items2[right]
            right+=1
        # index += 1


    # print("items after being sorted: ", items, index)
    # print("items at left: ", items1[left:], "items at right: ", items1[right:])
    # print(" ")
    # # if we are done with either items1 or items2 then
    # # we don't need to extend since we are on items itself
    merged.extend(items1[left:])
    merged.extend(items2[right:])
    # return items
    return merged


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.

    Running time: O(n/2)^2 = O(n^2)/4 Why and under what conditions? each sorting methods take
    quadratic time and items is divided into two parts before being sorted.
    Memory usage: 2*O(n) Why and under what conditions? we are making a copy for items1 and items2"""
    print("items: ", items)
    if len(items) <= 1:
        return items

    mid = len(items)//2 #split array in to two parts
    items1 = items[:mid]
    items2 = items[mid:]
    print("items1: ", items1)
    print("items2: ", items2)
    print(" ")
    # sort each half
    selection_sort(items1)
    print("items1: ", items1)

    insertion_sort(items2)
    print("items2: ", items2)

    sorted_items = merge(items1, items2, items)
    # print("sorted_items: ", sorted_items)
    items[:] = sorted_items
    # # print("items: ", items)
    # # for i in range(len(items)):
    # #     items[i] = sorted_items[i]
    return items


# print("split merge: ", split_sort_merge('Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()))
# print("split merge: ", split_sort_merge([3, 3, 5, 5, 5, 7, 7, 7, 7]))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.

    Running time: n log(n) Why and under what conditions? this function runs recursively
    until it hits its base case
    Memory usage: n log n Why and under what conditions? we create n memories for logn iteration"""

    if len(items) <= 1:
        return items

    mid = len(items)//2 #split items to two parts
    items1 = merge_sort(items[:mid])
    items2 = merge_sort(items[mid:])

    sorted_items = merge(items1, items2, items)
    # print("sorted_items: ", sorted_items)
    items[:] = sorted_items

    return items

# print("Final: ", merge_sort('Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()))


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` for simplicity sake I chose the last element as the pivot
    and the first element as the pivot index from that range, moving pivot into
    index `p`, items
    less than pivot into range `[low...p-1]`, and items greater than pivot
    into range `[p+1...high]`.
    TODO: Running time: for nearly sorted array the time complexity is O(n)
    Why and under what conditions? there is only one for loop
    TODO: Memory usage: O(1) Why and under what conditions? in place sorting, not
    allocating memeory """
    # Choose a pivot any way and document your method in docstring above
    divider = low #keeps track of the pivot index used for comparision
    pivot = high #default pivot index
    # Loop through all items in range [low...high]
    for i in range(low, high):
    # Move items less than pivot into front of range [low...p-1]
    # Move items greater than pivot into back of range [p+1...high]
        if items[i] < items[pivot]: #this does the work
            items[i], items[divider] = items[divider], items[i] # by moving the items less than
            divider += 1 # and leaving items greater where they are
    # Move pivot item into final position [p] and return index p
    items[pivot], items[divider] = items[divider], items[pivot]
    return divider


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: n log(n) Why and under what conditions? if we choose a
    pivot that lies in between of max and min value then we do log(n) iteration for
    n elements that are in items
    Worst case running time: n^2 Why and under what conditions? if the pivot
    we choose is the min value or max value we keep iterating without doing any swap
    # 12345 p=1, 2345, 345, 45, 5 #p=3, 12 45, 1 2, 3 4
    Memory usage: O(1) Why and under what conditions? in place sorting
    not allocating new memory"""
    # Check if high and low range bounds have default values (not given)
    if low == None and high == None:
        low = 0
        high = len(items)-1
    # Check if list or range is so small it's already sorted (base case)
    if low >= high:
        return
    # Partition items in-place around a pivot and get index of pivot
    p = partition(items, low, high)
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, p-1)
    quick_sort(items, p+1, high)

    return items
# print("quick sort: ", quick_sort([9, 12, 9, 2, 17, 1, 6], 0, 6))
