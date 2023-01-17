"""
A binary search tree (BST) is a type of data structure that allows for efficient insertion, deletion, and searching of elements. Each node in a BST has at most two children and the value of the left child must be less than the value of the parent node, while the value of the right child must be greater than the parent node.

Here's an example of how you can implement a Binary Search Tree in Python:
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data, curr_node.left)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data, curr_node.right)
        else:
            print("Value already in tree!")

    def find(self, data):
        if self.root:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, curr_node):
        if curr_node is None:
            return None
        elif data == curr_node.data:
            return curr_node
        elif data < curr_node.data:
            return self._find(data, curr_node.left)
        else:
            return self._find(data, curr_node.right)

    def delete(self, data):
        if self.root is not None:
            self.root = self._delete(data, self.root)

    def _delete(self, data, curr_node):
        if curr_node is None:
            return None
        elif data < curr_node.data:
            curr_node.left = self._delete(data, curr_node.left)
        elif data > curr_node.data:
            curr_node.right = self._delete(data, curr_node.right)
        else:
            if curr_node.left is None and curr_node.right is None:
                curr_node = None
            elif curr_node.left is None:
                curr_node = curr_node.right
            elif curr_node.right is None:
                curr_node = curr_node.left
            else:
                min_val = self.find_min(curr_node.right)
                curr_node.data = min_val
                curr_node.right = self._delete(min_val, curr_node.right)
        return curr_node

    def find_min(self, curr_node):
        if curr_node.left is not None:
            return self.find_min(curr_node.left)
        return curr_node.data

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, curr_node):
        if curr_node is not None:
            self._inorder_traversal(curr_node.left)
            print(curr_node.data)
            self._inorder_traversal(curr_node.right)

    def preorder_traversal(self):
        if self.root is not None:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, curr_node):
        if curr_node is not None:
            print(curr_node.data)
            self._preorder_traversal(curr_node.left)
            self._preorder_traversal(curr_node.right)

    def postorder_traversal(self):
        if self.root is not None:
            self._postorder_traversal(self.root)

    def _postorder_traversal(self, curr_node):
        if curr_node is not None:
            self._postorder_traversal(curr_node.left)
            self._postorder_traversal(curr_node.right)
            print(curr_node.data)


"""
This will print the elements in the tree in in-order, pre-order and post-order respectively, allowing you to see how the tree is being traversed.
Please note that these traversals are depth-first traversals.
"""
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(8)
print("In-order traversal:")
bst.inorder_traversal()
print("Pre-order traversal:")
bst.preorder_traversal()
print("Post-order traversal:")
bst.postorder_traversal()
