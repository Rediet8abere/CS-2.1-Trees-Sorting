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
        """Return True if this prefix tree contains the given string.
        Running-Time: O(n) where n is the length of string.
        Space-Complexity: 2*O(1) we instantiate a variable to traverse through prefixtree.
        """
        if string == "":
            return True
        cur_node = self.root
        for s in string:
            # if character is not root's children
            if s not in cur_node.children: #Constant look up
                return False
            cur_node = cur_node.get_child(s)
        return cur_node.terminal == True



    def insert(self, string):
        """Insert the given string into this prefix tree.
        Running-Time: O(n) where n is the length of string.
        Space-Complexity: 3*O(1) we instantiate a variable to traverse through prefixtree.
        """
        cur_node = self.root
        unique = False
        for s in string:
            if s not in cur_node.children:
                unique = True
                cur_node.children[s] = PrefixTreeNode(s)
            cur_node = cur_node.children[s]
        cur_node.terminal = True
        if unique:
            self.size += 1


    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node.
        Running-Time: O(n) where n is the length of string.
        Space-Complexity: 3*O(1) we instantiate a variable to traverse through prefixtree."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0

        # Start with the root node
        node = self.root

        depth = 0
        while node:
            node = node.children
            depth += 1
        return node, depth


    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string.
        Running-Time: O(n) where n is the length of string.
        Space-Complexity: 3*O(1) we instantiate a variable to traverse through prefixtree."""
        # Create a list of completions in prefix tree
        completions = []
        string = prefix
        cur_node = self.root
        preintri = False
        # print("find node", self._find_node(string))
        for p in prefix:
            if p in cur_node.children:
                preintri = True
                cur_node = cur_node.children[p]
            elif p not in cur_node.children:
                return completions

        self._traverse(cur_node, prefix, completions)
        if completions == [] and preintri == True:
            completions.append(prefix)
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree.
        Running-Time: O(n) where n is the length of string.
        Space-Complexity: 3*O(1) we instantiate a variable to traverse through prefixtree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        # TODO
        cur_node = self.root
        for char in cur_node.children.keys():
            all_strings.extend(self.complete(char))
        return all_strings
    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function.
        Running-Time: O(n*m) where n is the number of time we loop through child_node
                    and m is the number of time we make recursive call
        Space-Complexity: 3*O(1) we instantiate a variable to traverse through prefixtree."""


        # node has no children return contorl back to the caller
        if node.num_children() == 0:
            return
        # if this node contains char that ends the word then add to complteions
        if node.terminal:
            visit.append(prefix)
        # string = prefix
        # for char in children keys
        for char in node.children.keys():
            # concatenate prefix with char
            string = prefix + char
            child_node = node.get_child(char)
            if child_node.terminal:
                visit.append(string)
            # otherwise make it a prefix and keep going
            else:
                prefix = string
            # make a recursive call until we reach the end of the trie(with no children)
            self._traverse(child_node, prefix, visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    # tree = PrefixTree()
    # print(f'\ntree: {tree}')
    # print(f'root: {tree.root}')
    # # print(f'strings: {tree.strings()}')
    # print(tree.is_empty())
    # # print(tree.contains('ABC'))
    # print(tree.insert('ABC'))

    tree = PrefixTree(strings)
    tree.strings()
    #Verify completions for all substrings
    tree.complete('ABC') == ['ABC']
    # tree.complete('AB') == ['ABC', 'ABD']
    # tree.complete('A') == ['A', 'ABC', 'ABD']
    # tree.complete('ABD') == ['ABD']


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
