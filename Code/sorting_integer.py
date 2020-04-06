# #!python
# class Node(object):
#
#     def __init__(self, data):
#         """Initialize this node with the given data."""
#         self.data = data
#         self.next = None
#         self.prev = None
#
#     def __repr__(self):
#         """Return a string representation of this node."""
#         return 'Node({!r})'.format(self.data)
#
#
# class LinkedList(object):
#
#     def __init__(self, iterable=None):
#         """Initialize this linked list and append the given items, if any."""
#         self.head = None  # First node
#         self.tail = None  # Last node
#         self.size = 0  # Number of nodes
#         # Append the given items
#         if iterable is not None:
#             for item in iterable:
#                 self.append(item)
#
#     def __str__(self):
#         """Return a formatted string representation of this linked list."""
#         items = ['({!r})'.format(item) for item in self.items()]
#         return '[{}]'.format(' -> '.join(items))
#
#     def __repr__(self):
#         """Return a string representation of this linked list."""
#         return 'LinkedList({!r})'.format(self.items())
#
#     def items(self):
#         """Return a list of all items in this linked list.
#         Best and worst case running time: Theta(n) for n items in the list
#         because we always need to loop through all n nodes."""
#         # Create an empty list of results
#         result = []  # Constant time to create a new list
#         # Start at the head node
#         node = self.head  # Constant time to assign a variable reference
#         # Loop until the node is None, which is one node too far past the tail
#         while node is not None:  # Always n iterations because no early exit
#             # Append this node's data to the results list
#             result.append(node.data)  # Constant time to append to a list
#             # Skip to the next node
#             node = node.next  # Constant time to reassign a variable
#         # Now result contains the data from all nodes
#         return result  # Constant time to return a list
#
#     def is_empty(self):
#         """Return True if this linked list is empty, or False."""
#         return self.head is None
#
#
#     def append(self, item):
#         """Insert the given item at the tail of this linked list.
#         Best and worst case running time: O(1) under what conditions?
#         since we have access to the tail node we don't have to traverse
#         through the linked list to get to the last node"""
#         # Create a new node to hold the given item
#         new_node = Node(item)
#         # Check if this linked list is empty
#         if self.is_empty():
#             # Assign head to new node
#             new_node.prev = None
#             self.head = new_node
#         else:
#             # Otherwise insert new node after tail
#             new_node.prev = self.tail
#             self.tail.next = new_node
#         # Update tail to new node regardless
#         # print("prev", new_node.prev, "item", item)
#         self.tail = new_node
#         self.size += 1
#
#     def prepend(self, item):
#         # Create a new node to hold the given item
#         new_node = Node(item)
#         # Check if this linked list is empty
#         if self.is_empty():
#             # Assign tail to new node
#             self.tail = new_node
#         else:
#             # Otherwise insert new node before head
#             new_node.next = self.head
#         # Update head to new node regardless
#         self.head = new_node
#         self.size += 1
#
#     def get_at_index(self, index):
#
#        # Check if the given index is out of range and if so raise an error
#        if not (0 <= index < self.size):
#            raise ValueError('List index out of range: {}'.format(index))
#        # Find the node at the given index and return its data
#        count = 0
#        # Start at the head node
#        node = self.head  # Constant time to assign a variable reference
#        # Loop until the node is None, which is one node too far past the tail
#        while node is not None:  # Up to n iterations if we don't exit early
#            # Check if this node's data satisfies the given quality function
#            if count == index:  # Constant time to call quality function
#                # We found data satisfying the quality function, so exit early
#                return node.data  # Constant time to return data
#            # Skip to the next node
#            node = node.next  # Constant time to reassign a variable
#            count += 1
#        # We never found data satisfying quality, but have to return something
#        return None  # Constant time to return None
#        # return self.items()[index]
#
#
#     def insert_at_index(self, bucket, data, index):
#         node = Node(data)
#         cur_node = bucket[index]
#         while cur_node.next != None:
#             if cur_node.data < data:
#                 cur_node.next = node
#             elif cur_node.data > data:
#                 prev = cur_node.prev
#                 cur_node.prev = node
#                 node.next = cur_node
#                 node.prev = prev
#                 prev.next = node
#             cur_node = cur_node.next
#
#         cur_node.next = node
#
# # 7
#
# # 3, 6, 8
# def insert_at_index(bucket, data, index):
#     node = Node(data)
#     cur_node = bucket[index]
#     while cur_node.next != None:
#         if cur_node.data < data:
#             cur_node.next = node
#         elif cur_node.data > data:
#             prev = cur_node.prev
#             cur_node.prev = node
#             node.next = cur_node
#             node.prev = prev
#             prev.next = node
#         cur_node = cur_node.next
#
#     cur_node.next = node
#     print("cur_node.next ", cur_node.next )
#
# def counting_sort(numbers):
#     """Sort given numbers (integers) by counting occurrences of each number,
#     then looping over counts and copying that many numbers into output list.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Find range of given numbers (minimum and maximum integer values)
#     maxNum = max(numbers)
#     minNum = min(numbers)
#     # TODO: Create list of counts with a slot for each number in input range
#     listCount = {}
#     for i in range(len(numbers)):
#         if numbers[i] not in listCount:
#             listCount[numbers[i]] = 1
#         else:
#              listCount[numbers[i]] += 1
#     listCountValues = listCount.values()
#     print("listCountValues: ", listCountValues)
#
#     # TODO: Loop over given numbers and increment each number's count
#     # TODO: Loop over counts and append that many numbers into output list
#     outputList = []
#     # FIXME: Improve this to mutate input instead of creating new output list
# counting_sort([47, 3, 47, 47, 75, 84, 41, 10, 90, 63])
#
# def bucket_sort(numbers, num_buckets=10):
#     """Sort given numbers by distributing into buckets representing subranges,
#     then sorting each bucket and concatenating all buckets in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Find range of given numbers (minimum and maximum values)
#     maxNum = max(numbers)
#     minNum = min(numbers)
#     print("maxNum: ", maxNum, "minNum: ", minNum)
#     # TODO: Create list of buckets to store numbers in subranges of input range
#     node = Node(0)
#     bucket = [node for i in range(num_buckets+1)]
#     print("bucket: ", bucket)
#     # TODO: Loop over given numbers and place each item in appropriate bucket
#     # ll = LinkedList()
#     for i in range(num_buckets):
#         index = (numbers[i]*num_buckets)//maxNum
#
#         insert_at_index(bucket, numbers[i], index)
#         # print("index", index, 'bucket', bucket[index])
#     print("bucket: ", bucket)
#     newArray = []
#     for i in range(num_buckets):
#         head_node = bucket[i]
#         print("head_node on", head_node)
#         cur_node = head_node.next
#         print("cur_node ->", cur_node)
#         # cur_node = cur_node.next
#         print("none ", cur_node)
#         while not cur_node == None:
#             # print("not none ", cur_node)
#             newArray.append(cur_node.data)
#             cur_node = cur_node.next
#             # print(" none ", cur_node)
#     print("newArray: ", newArray)
#     # print("ll: ", ll)
#     # TODO: Sort each bucket using any sorting algorithm (recursive or another)
#     # TODO: Loop over buckets and append each bucket's numbers into output list
#     # FIXME: Improve this to mutate input instead of creating new output list
#
# # bucket_sort([29, 3, 11, 47, 75, 84, 41, 10, 90, 63])
