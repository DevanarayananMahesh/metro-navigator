class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # type: ignore
            self.head = new_node
        self._size += 1

    def insert_at(self, index, value):
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
            current = current.next  # type: ignore
            counter += 1

        new_node.next = current.next  # type: ignore
        current.next = new_node  # type: ignore
        self._size += 1

    def get(self, index):
        if type(index) is not int:
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")

        current = self.head
        for useless_i in range(index):
            current = current.next  # type: ignore

        return current.value  # type: ignore

    def find(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def remove(self, value):
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
        if type(index) is not int:
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")

        if index == 0:
            removed_value = self.head.value  # type: ignore
            self.head = self.head.next  # type: ignore

            if self.head is None:
                self.tail = None

            self._size -= 1
            return removed_value

        current = self.head
        for useless_i in range(index - 1):
            current = current.next  # type: ignore

        node_to_remove = current.next  # type: ignore
        current.next = node_to_remove.next  # type: ignore

        if node_to_remove is self.tail:
            self.tail = current

        self._size -= 1
        return node_to_remove.value  # type: ignore

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        prev = None
        current = self.head
        old_head = self.head

        while current is not None:
            temp_next = current.next
            current.next = prev # type: ignore
            prev = current
            current = temp_next

        self.tail = old_head
        self.head = prev

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def to_list(self):
        out = []
        current = self.head
        while current is not None:
            out.append(current.value)
            current = current.next
        return out

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.value))
            current = current.next

        elements.append("None")
        return " -> ".join(elements)