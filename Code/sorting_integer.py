

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # maxNum = max(numbers)
    # minNum = min(numbers)
    # # TODO: Create list of counts with a slot for each number in input range
    # listCount = {}
    # for i in range(len(numbers)):
    #     if numbers[i] not in listCount:
    #         listCount[numbers[i]] = 1
    #     else:
    #          listCount[numbers[i]] += 1
    # listCountValues = listCount.values()
    # print("listCountValues: ", listCountValues)

    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # outputList = []
    # FIXME: Improve this to mutate input instead of creating new output list
counting_sort([47, 3, 47, 47, 75, 84, 41, 10, 90, 63])

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # maxNum = max(numbers)
    # minNum = min(numbers)
    # print("maxNum: ", maxNum, "minNum: ", minNum)
    # # TODO: Create list of buckets to store numbers in subranges of input range
    # node = Node(0)
    # bucket = [node for i in range(num_buckets+1)]
    # print("bucket: ", bucket)
    # # TODO: Loop over given numbers and place each item in appropriate bucket
    # # ll = LinkedList()
    # for i in range(num_buckets):
    #     index = (numbers[i]*num_buckets)//maxNum
    #
    #     insert_at_index(bucket, numbers[i], index)
    #     # print("index", index, 'bucket', bucket[index])
    # print("bucket: ", bucket)
    # newArray = []
    # for i in range(num_buckets):
    #     head_node = bucket[i]
    #     print("head_node on", head_node)
    #     cur_node = head_node.next
    #     print("cur_node ->", cur_node)
    #     # cur_node = cur_node.next
    #     print("none ", cur_node)
    #     while not cur_node == None:
    #         # print("not none ", cur_node)
    #         newArray.append(cur_node.data)
    #         cur_node = cur_node.next
    #         # print(" none ", cur_node)
    # print("newArray: ", newArray)
    # print("ll: ", ll)
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

# bucket_sort([29, 3, 11, 47, 75, 84, 41, 10, 90, 63])
