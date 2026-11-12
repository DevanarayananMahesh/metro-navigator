from linked_list import LinkedList


class Stack:
    """A LIFO (Last-In-First-Out) stack backed by a LinkedList.

    Attributes:
        _list: The internal LinkedList storing stack elements.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self._list = LinkedList()

    def push(self, item):
        """Pushes a new item onto the top of the stack.

        Args:
            item: The element to add.
        """
        self._list.prepend(item)

    def pop(self):
        """Removes and returns the top item from the stack.

        Returns:
            The most recently pushed item.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError
        return self._list.remove_at(0)

    def peek(self):
        """Looks at the top item without removing it.

        Returns:
            The top item on the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError
        return self._list.get(0)

    def is_empty(self):
        """Checks if the stack has no elements.

        Returns:
            True if empty, False otherwise.
        """
        return len(self._list) == 0

    def clear(self):
        """Removes all elements from the stack."""
        self._list.clear()

    def to_list(self):
        """Converts stack contents into a standard list.

        Returns:
            A list ordered from top to bottom.
        """
        return self._list.to_list()

    def __len__(self):
        """Returns the total number of items in the stack."""
        return len(self._list)


def is_balanced(text):
    """Checks whether bracket pairs in a string are balanced.

    Args:
        text: The string containing parentheses, brackets, or braces.

    Returns:
        True if all opening symbols match their closing counterparts.

    Raises:
        TypeError: If input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError

    stack = Stack()
    matching_pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching_pairs[char]:
                return False

    return stack.is_empty()