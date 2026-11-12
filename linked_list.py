class Node:
    """A node inside a singly-linked list.

    Attributes:
        value: The data payload stored in the node.
        next: Pointer to the next list node.
    """

    def __init__(self, value):
        """Initializes a new node with data.

        Args:
            value: Data to put in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """A singly-linked list with head and tail pointers.

    Attributes:
        head: The start node of the list.
        tail: The end node of the list.
        _size: Total count of nodes in the list.
    """

    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        """Appends a value to the back of the list.

        Args:
            value: Data to append.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        """Adds a value to the front of the list.

        Args:
            value: Data to insert at head.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    def insert_at(self, index, value):
        """Inserts a value at a specific 0-based index.

        Args:
            index: Target index position.
            value: Data to insert.

        Raises:
            TypeError: If index is not an integer.
            IndexError: If index is out of bounds.
        """
        if type(index) is not int:
            raise TypeError("Index must be an integer.")

        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds.")

        if index == 0:
            self.prepend(value)
            return

        if index == self._size:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head
        counter = 0

        while counter < index - 1:
            current = current.next
            counter += 1

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def get(self, index):
        """Retrieves data at a given 0-based index.

        Args:
            index: Positional index to fetch.

        Returns:
            Data at the specified position.

        Raises:
            TypeError: If index is not an integer.
            IndexError: If index is out of bounds.
        """
        if type(index) is not int:
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")

        current = self.head
        for useless_i in range(index):
            current = current.next

        return current.value

    def find(self, value):
        """Finds index of the first occurrence of a value.

        Args:
            value: Value to look up.

        Returns:
            0-based index if found, -1 if missing.
        """
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def remove(self, value):
        """Removes the first occurrence of a target value.

        Args:
            value: Value to remove.

        Returns:
            True if item was removed, False if not found.
        """
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            if self.head is None:
                self.tail = None
            return True

        prev = self.head
        current = prev.next

        while current is not None:
            if current.value == value:
                prev.next = current.next

                if current is self.tail:
                    self.tail = prev

                self._size -= 1
                return True

            prev = current
            current = prev.next

        return False

    def remove_at(self, index):
        """Deletes item at a specific 0-based index.

        Args:
            index: Target index to remove.

        Returns:
            The value of the removed node.

        Raises:
            TypeError: If index is not an integer.
            IndexError: If index is out of bounds.
        """
        if type(index) is not int:
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")

        if index == 0:
            removed_value = self.head.value
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            self._size -= 1
            return removed_value

        current = self.head
        for useless_i in range(index - 1):
            current = current.next

        node_to_remove = current.next
        current.next = node_to_remove.next

        if node_to_remove is self.tail:
            self.tail = current

        self._size -= 1
        return node_to_remove.value

    def reverse(self):
        """Reverses the linked list in-place."""
        if self.head is None or self.head.next is None:
            return

        prev = None
        current = self.head
        old_head = self.head

        while current is not None:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next

        self.tail = old_head
        self.head = prev

    def clear(self):
        """Wipes all nodes from the linked list."""
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        """Checks if the list contains any nodes.

        Returns:
            True if empty, False otherwise.
        """
        return self._size == 0

    def to_list(self):
        """Converts linked list nodes to a standard Python list.

        Returns:
            List containing all values in order.
        """
        out = []
        current = self.head
        while current is not None:
            out.append(current.value)
            current = current.next
        return out

    def __len__(self):
        """Returns total node count."""
        return self._size

    def __iter__(self):
        """Yields values sequentially for loop iterations."""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        """Formats the linked list for human-readable output."""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.value))
            current = current.next

        elements.append("None")
        return " -> ".join(elements)