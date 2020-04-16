#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        # TODO
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        # TODO
        if string == "":
            return True
        cur_node = self.root
        for s in string:
            # if character is not root's children
            if s not in cur_node.children:
                return False
            cur_node = cur_node.children[s]
        return cur_node.terminal == True



    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # TODO
        cur_node = self.root
        print("cur_node: ", cur_node.children)
        unique = False
        for s in string:
            if s not in cur_node.children:
                unique = True
                cur_node.children[s] = PrefixTreeNode(s)
                print("cur_node: ", cur_node)
            cur_node = cur_node.children[s]
        print("cur_node: done", cur_node)
        cur_node.terminal = True
        if unique:
            self.size += 1

        print("cur_node terminal: ", cur_node.terminal)


    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node

        node = self.root
        # TODO
        depth = 0
        while node:
            node = node.children
            depth += 1
        return node, depth


    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        # TODO
        # string = prefix
        # cur_node = self.root
        # for p in prefix:
        #     if p in cur_node.children:
        #         cur_node = cur_node.children[p]
        #     else:
        #         return completions
        # self._traverse(cur_node, prefix, completions)
        # while cur_node:
        #     string += cur_node.character
        #     if cur_node.character in cur_node.children:
        #         cur_node = cur_node.children[cur_node.character]
        #     if cur_node.terminal == True:
        #         completions.append(string)
        #         string = prefix
        # return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        # TODO

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # TODO
        # if node.terminal == True:
        #     visit.append(node)
        # for char in node.children.keys():
        #     self._traverse(node.children.get(char), visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    # tree = PrefixTree()
    # print(f'\ntree: {tree}')
    # print(f'root: {tree.root}')
    # # print(f'strings: {tree.strings()}')
    # print(tree.is_empty())
    # # print(tree.contains('ABC'))
    # print(tree.insert('ABC'))
    tree = PrefixTree(['ABC'])
    # tree.root.character == PrefixTree.START_CHARACTER
    # print(tree.root.is_terminal()) #is False
    # print(tree.root.num_children()) #== 1
    # print(tree.root.has_child('A')) #is True
    #
    # node_A = tree.root.get_child('A')
    # print("node_A: ", node_A)
    # node_A.character == 'A'
    # node_A.is_terminal() is True
    # node_A.num_children() == 0


    # print('\nInserting strings:')
    # for string in strings:
    #     tree.insert(string)
    #     print(f'insert({string!r}), size: {tree.size}')
    #
    # print(f'\ntree: {tree}')
    # print(f'root: {tree.root}')
    #
    # print('\nSearching for strings in tree:')
    # for string in sorted(set(strings)):
    #     result = tree.contains(string)
    #     print(f'contains({string!r}): {result}')

    # print('\nSearching for strings not in tree:')
    # prefixes = sorted(set(string[:len(string)//2] for string in strings))
    # for prefix in prefixes:
    #     if len(prefix) == 0 or prefix in strings:
    #         continue
    #     result = tree.contains(prefix)
    #     print(f'contains({prefix!r}): {result}')
    #
    # print('\nCompleting prefixes in tree:')
    # for prefix in prefixes:
    #     completions = tree.complete(prefix)
    #     print(f'complete({prefix!r}): {completions}')
    #
    # print('\nRetrieving all strings:')
    # retrieved_strings = tree.strings()
    # print(f'strings: {retrieved_strings}')
    # matches = set(retrieved_strings) == set(strings)
    # print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # # Create a dictionary of tongue-twisters with similar words to test with
    # tongue_twisters = {
    #     'Seashells': 'Shelly sells seashells by the sea shore'.split(),
    #     # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
    #     # 'Woodchuck': ('How much wood would a wood chuck chuck'
    #     #                ' if a wood chuck could chuck wood').split()
    # }
    # # Create a prefix tree with the similar words in each tongue-twister
    # for name, strings in tongue_twisters.items():
    #     print(f'{name} tongue-twister:')
    #     create_prefix_tree(strings)
    #     if len(tongue_twisters) > 1:
    #         print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
