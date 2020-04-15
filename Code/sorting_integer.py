
from linkedlist import LinkedList
from sorting_iterative import bubble_sort, insertion_sort
from sorting_recursive import merge, quick_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(max+1-min) + O(n) + O(max+1-min*freq) where freq is
    frequency of unique elements Why and under what conditions? we loop max+1-min
    times and perform freq opertaions.
    Memory usage: O(max-min) Why and under what conditions? we allocate
    max-min memory to keep track of frequency.
    """
    # Find range of given numbers (minimum and maximum integer values)
    maxNum = max(numbers)
    minNum = min(numbers)
    # Create list of counts with a slot for each number in input range
    count_arr = []
    for i in range(minNum, maxNum+1):
        count_arr.append(0)

    # Loop over given numbers and increment each number's count
    for i in range(len(numbers)):
        index = numbers[i] - minNum
        count_arr[index] += 1

    # Loop over counts and append that many numbers into output list
    i = 0
    for index in range(len(count_arr)):
        for j in range(count_arr[index]):
            numbers[i] = minNum + index # Improve this to mutate input instead of creating new output list
            i += 1

    return numbers
# print("counting sort: ", counting_sort([17, 13, 17, 17, 11, 10, 10, 13, 11]))


def bucket_sort(numbers, num_buckets=3):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: 2*O(num_buckets) + O(n) + running time of sorting algo
    Why and under what conditions? loop num_buckets times to initalize an array
    loop n times to place number in the right bucket loop num_buckets times
    to sort.
    Memory usage: O(num_buckets) Why and under what conditions? we have to
    allocate memory for buckets"""
    # Find range of given numbers (minimum and maximum values)
    maxNum = max(numbers)
    minNum = min(numbers)

    # Create list of buckets to store numbers in subranges of input range
    bucket_list = [LinkedList() for _ in range(num_buckets)]

    # Loop over given numbers and place each item in appropriate bucket
    for i in range(len(numbers)):
        index = numbers[i] - minNum
        index = int(numbers[i]/10)
        bucket_list[index].append(numbers[i])
        # if numbers[i] <= 9:
        #     bucket_list[0].append(numbers[i])
        # elif 9 < numbers[i] <= 19:
        #     bucket_list[1].append(numbers[i])
        # else:
            # bucket_list[2].append(numbers[i])
    # Sort each bucket using any sorting algorithm (recursive or another)
    # Loop over buckets and append each bucket's numbers into output list
    start = 0
    end = 0
    for i in range(len(bucket_list)):
        bucket_len = bucket_list[i].length()
        end += bucket_len
        numbers[start:end] = insertion_sort(bucket_list[i].items())
        start += bucket_len

    return numbers
    # FIXME: Improve this to mutate input instead of creating new output list


print("bucket sort: ", bucket_sort([17, 3, 17, 17, 1, 10, 10, 13, 1, 25, 20, 28, 13, 16, 11, 8, 4]))
