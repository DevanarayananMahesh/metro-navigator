class BSTNode:
    """A single node inside a binary search tree.

    Attributes:
        key: The key used for ordering and searching.
        value: The data attached to the key.
        left: Pointer to the left child node.
        right: Pointer to the right child node.
    """

    def __init__(self, key: int, value=None):
        """Initializes a new tree node.

        Args:
            key: The key for node placement.
            value: Optional data to store in the node.
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    """An iterative binary search tree implementation.

    Attributes:
        root: The top node of the tree.
        _size: Total count of items currently in the tree.
    """

    def __init__(self):
        """Sets up an empty binary search tree."""
        self.root = None
        self._size = 0

    def insert(self, key, value=None):
        """Inserts a key-value pair or updates an existing key.

        Args:
            key: The key to add (int or str).
            value: Optional payload attached to the key.

        Raises:
            TypeError: If the key type is invalid or mismatched.
        """
        if not isinstance(key, (int, str)):
            raise TypeError

        if self.root is None:
            self.root = BSTNode(key, value)
            self._size += 1
            return

        if type(key) is not type(self.root.key):
            raise TypeError

        current = self.root
        while True:
            if key == current.key:
                current.value = value
                return

            elif key < current.key:
                if current.left is None:
                    current.left = BSTNode(key, value)
                    self._size += 1
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = BSTNode(key, value)
                    self._size += 1
                    return
                current = current.right

    def contains(self, key):
        """Checks if a given key exists in the tree.

        Args:
            key: The key we're looking for.

        Returns:
            True if key is found, False otherwise.

        Raises:
            TypeError: If key is not an int or str.
        """
        if not isinstance(key, (int, str)):
            raise TypeError

        if self.root is None:
            return False

        current = self.root
        while True:
            if key == current.key:
                return True

            elif key < current.key:
                if current.left is None:
                    return False
                current = current.left

            else:
                if current.right is None:
                    return False
                current = current.right

    def get(self, key):
        """Fetches the stored value for a given key.

        Args:
            key: The target key to look up.

        Returns:
            The payload stored at the key.

        Raises:
            TypeError: If key is not an int or str.
            KeyError: If key doesn't exist in the tree.
        """
        if not isinstance(key, (int, str)):
            raise TypeError

        if self.root is None:
            return False

        current = self.root
        while True:
            if key == current.key:
                return current.value

            elif key < current.key:
                if current.left is None:
                    raise KeyError
                current = current.left

            else:
                if current.right is None:
                    raise KeyError
                current = current.right

    def delete(self, key):
        """Deletes a key from the tree.

        Args:
            key: The key to remove.

        Returns:
            True if successfully deleted, False if key wasn't found.

        Raises:
            TypeError: If key type is invalid.
        """
        if not isinstance(key, (int, str)):
            raise TypeError

        if self.root is None:
            return False

        parent = None
        current = self.root

        while True:
            if key == current.key:
                if current.left is None and current.right is None:
                    if current == self.root:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None

                elif current.left is not None and current.right is None:
                    if current == self.root:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left

                elif current.left is None and current.right is not None:
                    if current == self.root:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right

                else:
                    succ_parent = current
                    inorder_successor = current.right

                    while inorder_successor.left is not None:
                        succ_parent = inorder_successor
                        inorder_successor = inorder_successor.left

                    current.key = inorder_successor.key
                    current.value = inorder_successor.value

                    if succ_parent.left == inorder_successor:
                        succ_parent.left = inorder_successor.right
                    else:
                        succ_parent.right = inorder_successor.right

                self._size -= 1
                return True

            elif key < current.key:
                if current.left is None:
                    return False
                parent = current
                current = current.left

            else:
                if current.right is None:
                    return False
                parent = current
                current = current.right

    def inorder(self):
        """Gives back all tree keys in sorted order.

        Returns:
            A list of keys visited left to right.
        """
        result = []
        stack = []
        current = self.root

        while current or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.key)

            current = current.right

        return result

    def preorder(self):
        """Performs a preorder traversal.

        Returns:
            A list of tree keys visited in preorder.
        """
        if self.root is None:
            return []

        result = []
        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current.key)

            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

        return result

    def postorder(self):
        """Performs a postorder traversal.

        Returns:
            A list of tree keys visited in postorder.
        """
        if self.root is None:
            return []

        result = []
        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current.key)

            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)

        return result[::-1]

    def level_order(self):
        """Traverses the tree level by level.

        Returns:
            A list of keys ordered by levels.
        """
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.key)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return result

    def height(self):
        """Calculates the total height of the tree.

        Returns:
            Total levels in the tree.
        """
        if self.root is None:
            return 0

        queue = [self.root]
        height = 0

        while len(queue) > 0:
            level_size = len(queue)
            height += 1

            for useless_i in range(level_size):
                current = queue.pop(0)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

        return height

    def min_key(self):
        """Finds the smallest key in the tree.

        Returns:
            The minimum key value.

        Raises:
            ValueError: If the tree is empty.
        """
        if self._size == 0:
            raise ValueError

        current = self.root
        while current.left is not None:
            current = current.left

        return current.key

    def max_key(self):
        """Finds the largest key in the tree.

        Returns:
            The maximum key value.

        Raises:
            ValueError: If the tree is empty.
        """
        if self._size == 0:
            raise ValueError

        current = self.root
        while current.right is not None:
            current = current.right

        return current.key

    def count_leaves(self):
        """Counts how many leaf nodes are in the tree.

        Returns:
            Total count of nodes with no children.
        """
        if self.root is None:
            return 0

        leaf_num = 0
        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)

            if current.left is None and current.right is None:
                leaf_num += 1

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return leaf_num

    def range_query(self, low, high):
        """Finds all keys falling within an inclusive range [low, high].

        Args:
            low: Lower bound of the range.
            high: Upper bound of the range.

        Returns:
            A sorted list of keys within the range.

        Raises:
            TypeError: If bounds aren't integers.
        """
        if type(low) is not int or type(high) is not int:
            raise TypeError

        results = []
        stack = []
        current = self.root

        while current or stack:
            while current is not None:
                stack.append(current)
                if current.key > low:
                    current = current.left
                else:
                    current = None

            current = stack.pop()

            if low <= current.key <= high:
                results.append(current.key)

            if current.key < high:
                current = current.right
            else:
                current = None

        return results

    def is_valid_bst(self):
        """Verifies if the tree maintains true BST ordering invariants.

        Returns:
            True if all left children < node < right children, False otherwise.
        """
        if self.root is None:
            return True

        stack = [(self.root, None, None)]
        while stack:
            node, min_bound, max_bound = stack.pop()

            if min_bound is not None and node.key <= min_bound:
                return False
            if max_bound is not None and node.key >= max_bound:
                return False

            if node.right:
                stack.append((node.right, node.key, max_bound))

            if node.left:
                stack.append((node.left, min_bound, node.key))

        return True

    def is_empty(self):
        """Checks if the tree has no nodes.

        Returns:
            True if tree is empty, False otherwise.
        """
        return self.root is None

    def __len__(self):
        """Returns the number of elements in the tree."""
        return self._size