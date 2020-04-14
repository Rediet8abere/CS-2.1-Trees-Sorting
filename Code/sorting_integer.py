
from linkedlist import LinkedList
from sorting_iterative import bubble_sort, insertion_sort
from sorting_recursive import merge, quick_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    maxNum = max(numbers)
    # minNum = min(numbers)
    # # TODO: Create list of counts with a slot for each number in input range
    countArr = []
    # initalize array
    for i in range(maxNum+1):
        countArr.append(0)
    print("countArr: ", countArr)
    # count at index
    for i in range(len(numbers)):
        countArr[numbers[i]] += 1
    print("countArr: ", countArr)
    newArr = []
    # sort O(n)*O(f)
    for i in range(len(countArr)):
    # for index, i in enumerate(countArr):
        # print("index: ", index, "i: ", i)
        for j in range(countArr[i]):
            newArr.append(i)

    return newArr




    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # outputList = []
    # FIXME: Improve this to mutate input instead of creating new output list

# counting_sort([17, 3, 17, 17, 1, 10, 10, 13, 1])

def bucket_sort(numbers, num_buckets=3):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    maxNum = max(numbers)
    # minNum = min(numbers)

    # # TODO: Create list of buckets to store numbers in subranges of input range
    bucket_list = [LinkedList() for _ in range(num_buckets)]

    # # TODO: Loop over given numbers and place each item in appropriate bucket
    for i in range(len(numbers)):
        if numbers[i] <= 9:
            bucket_list[0].append(numbers[i])
        elif 9 < numbers[i] <= 19:
            bucket_list[1].append(numbers[i])
        else:
            bucket_list[2].append(numbers[i])
    # Sort each bucket using any sorting algorithm (recursive or another)
    # Loop over buckets and append each bucket's numbers into output list
    new_arr = []
    for i in range(len(bucket_list)):
        new_arr.extend(insertion_sort(bucket_list[i].items()))
    return new_arr
    # FIXME: Improve this to mutate input instead of creating new output list

# print("bucket sort: ", bucket_sort([17, 3, 17, 17, 1, 10, 10, 13, 1, 25, 20, 28, 13, 16, 11, 8, 4]))
