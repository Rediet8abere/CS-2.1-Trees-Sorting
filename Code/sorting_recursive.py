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
    index = 0
    left, right = 0, 0
    while left < len(items1) and right < len(items2):
        if items1[left] < items2[right]:
            items[index] = items1[left]
            left+=1
        else:
            items[index] = items2[right]
            right+=1
        index += 1

    # if right is done first
    for item in items1[left:]:
        items[index] = item
        index += 1
    # if left is done first
    for item in items2[right:]:
        items[index] = item
        index += 1


    return items


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.

    Running time: 2*O(n)^2 Why and under what conditions? each sorting methods take
    quadratic time.
    Memory usage: 2*O(n) Why and under what conditions? we are making a copy for items1 and items2"""
    # [1, 4, 6, 7]
    # [1, 4] [6, 7]
    mid = len(items)//2
    items1 = items[:mid]
    items2 = items[mid:]
    selection_sort(items1)
    insertion_sort(items2)
    return merge(items1, items2, items)







# print("split merge: ", split_sort_merge([2, 5, 6, 9, 1, 3, 5, 8, 10]))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.

    Running time: O(1) * n Why and under what conditions? this function runs recursively
    until it hits its base case
    Memory usage: not using any space Why and under what conditions? we are not defining a new
    variable """

    if len(items) <= 1:
        return items

    mid = len(items)//2
    items1 = merge_sort(items[:mid])
    items2 = merge_sort(items[mid:])

    return merge(items1, items2, items)

    # split_sort_merge(items)

# print("Final: ", merge_sort([]))


def partition(items, low, high, pivot):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing the last element as a pivot [ the first item
    can also be chosen, but that might not be a good pivot if the array is nearly
    soreted, we can pick the middle, but that might not be a good choice if the
    array is not sorted. A good pivot would be the median of the first, last, and
    middle that way we have a high probability of choosing the middle element
    from the array ]from that range, moving pivot into index `p`, items
    less than pivot into range `[low...p-1]`, and items greater than pivot
    into range `[p+1...high]`.
    TODO: Running time: for nearly sorted array the time complexity is O(n)^, for
    unsorted list the time complexity is n log(n) Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    print("low: ", items[low], low)
    print("high: ", items[high], high)

    # copied = items.copy() random.randint(0,                  #First: 1, 12, 9, 2, 17, 9, 6 #second: 1, 6, 9, 2, 17, 9, 12
                                            #Third:
                    # 9, 12, 9, 2, 17, 1, 6
    p = pivot
    print("p: ", p, items[p])
    while low <= high:  #9, 12, 9, 2, 17, 1, 6
        while items[low] < items[pivot]:
            low += 1
        while items[high] > items[pivot]:
            high -= 1
        if low <= high:
            temp = items[low]
            items[low] = items[high]
            items[high] = temp
            low += 1
            high -= 1
    return low

        # if items[low] > items[p] and items[high] < items[p]:  #out of order
        #     temp = items[low]  #swap
        #     items[low] = items[high]
        #     items[high] = temp
        #     low += 1
        #     high -= 1
        #
        # elif items[low] < items[p]:
        #     print("items[low]: ", items[low], "items[p]: ", items[p])
        #     low += 1
        # else:   # items[high] > items[p]:
        #     high -= 1




# print("partition: ", partition([9, 12, 9, 2, 17, 1, 6], 0, 5))

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low == None and high == None:
        low = 0
        high = len(items)-1
    print("in qucik sort", "low: ", low, "high: ", high)
    if len(items) <=1: # base case
        return items
    if low >= high:
        return items

    pivot = (low + high)//2
    print("pivot: ", pivot)
    p = partition(items, low, high, pivot)
    quick_sort(items, low, p-1)
    quick_sort(items, p, high)
    print("items: ", items)
print("quick sort: ", quick_sort([9, 12, 9, 2, 17, 1, 6]))
