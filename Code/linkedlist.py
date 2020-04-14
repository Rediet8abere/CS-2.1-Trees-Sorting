class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: O(n) under what conditions? we have to
        traverse through the linkedlist to increment the node count by one until
        we reach to null"""
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        node = self.head

        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            node = node.next
        # Now node_count contains the number of nodes
        return node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) under what conditions? if index is out of range
        Worst case running time: O(n) under what conditions? we retrive the item by accessing it's index
        from a list built by traversing the LinkedList"""

        # If you use self.items()[index] in get_index_at() function, the run time will always be as self.items()
        # which is O(n). but you can reduce it to O(k) where k is the given index. instead of calling the items
        # function in the get_index_at() function iterate the linked list until given index and return node.
        # data at that position

        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # Find the node at the given index and return its data
        # print('index', index, self.items()[index])
        count = 0
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if count == index:  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
            count += 1
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None
        # return self.items()[index]

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) under what conditions? if index is refering
        to head node or node near head
        Worst case running time: O(n) under what conditions? if index refers to a
        node that is located by traversing through the linkedlist"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it
        new_node = Node(item)
        cur_node = self.head
        if index == 0:
            self.prepend(item)
            return self
        if index == self.size:
            self.append(item)
            return self

        while self.get_at_index(index) != cur_node.data:
            cur_node = cur_node.next
        prev =  cur_node.prev
        cur_node.prev = new_node
        new_node.next = cur_node
        new_node.prev = prev
        prev.next = new_node
        self.size += 1
        return self


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) under what conditions?
        since we have access to the tail node we don't have to traverse
        through the linked list to get to the last node"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            new_node.prev = None
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            new_node.prev = self.tail
            self.tail.next = new_node
        # Update tail to new node regardless
        # print("prev", new_node.prev, "item", item)
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) under what conditions?
        No matter how long our linkedlist is because there is no traversing required"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) under what conditions? if old item is the head node or near the head node
        Worst case running time: O(n) under what conditions? we need to traverse through
        the list to find the old item"""
        # TODO: Find the node containing the given old_item and replace its
        # data with new_item, without creating a new node object
        cur_node = self.head
        while cur_node.data != old_item:
            cur_node = cur_node.next
            if cur_node == None:
                raise ValueError('"Item Not Found": {}'.format(old_item))
                # return "Item Not found"
        cur_node.data = new_item
        return self

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) under what conditions? if item is in head node or near head node
        Worst case running time: O(n) under what conditions? if we have to traverse through nodes to find the item """
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                # Update tail to the previous node regardless
                self.tail = previous
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    # print(ll)
    #
    # # print('Appending items:')
    ll.append('A')
    # # print(ll)
    ll.append('B')
    # # print(ll)
    # ll.append('C')
    # print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('item', item)
        # print('get_at_index({}): {!r}'.format(index, item))
    # print(ll.insert_at_index(2,'D'))
    # print(ll.replace('L','K'))

    # print('Deleting items:')
    # ll.delete('B')
    # print(ll)
    # ll.delete('C')
    # print(ll)
    # ll.delete('A')
    # print(ll)
    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('size: {}'.format(ll.size))
    # print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()