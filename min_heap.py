class MinHeap:
    """An array-backed binary min-heap for priority items.

    Attributes:
        _data: Internal array storing (priority, item) tuples.
    """

    def __init__(self):
        """Initializes an empty min-heap."""
        self._data = []

    def push(self, priority, item):
        """Pushes a new item with a priority score into the heap.

        Args:
            priority: Numerical priority for ordering.
            item: Data payload attached to priority.
        """
        self._data.append((priority, item))
        index = len(self._data) - 1

        while index > 0:
            parent_index = (index - 1) // 2

            if self._data[index][0] < self._data[parent_index][0]:
                self._data[index], self._data[parent_index] = (
                    self._data[parent_index],
                    self._data[index],
                )
                index = parent_index
            else:
                break

    def pop(self):
        """Pops and returns the (priority, item) pair with minimum priority.

        Returns:
            The minimum (priority, item) tuple pair.

        Raises:
            IndexError: If the heap is empty.
        """
        if len(self._data) == 0:
            raise IndexError

        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        min_pair = self._data.pop()

        index = 0
        length = len(self._data)

        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child < length and self._data[left_child][0] < self._data[smallest][0]:
                smallest = left_child
            if right_child < length and self._data[right_child][0] < self._data[smallest][0]:
                smallest = right_child

            if smallest != index:
                self._data[index], self._data[smallest] = (
                    self._data[smallest],
                    self._data[index],
                )
                index = smallest
            else:
                break

        return min_pair

    def peek(self):
        """Peeks at minimum priority pair without removing it.

        Returns:
            The root (priority, item) tuple.

        Raises:
            IndexError: If heap is empty.
        """
        if len(self._data) == 0:
            raise IndexError
        return self._data[0]

    @staticmethod
    def build_heap(pairs):
        """Builds a new valid min-heap from an existing list of pairs.

        Args:
            pairs: A list of (priority, item) tuples.

        Returns:
            A newly constructed MinHeap instance.
        """
        heap = MinHeap()
        heap._data = pairs[:]
        length = len(heap._data)

        for i in range(length // 2 - 1, -1, -1):
            index = i
            while True:
                left_child = 2 * index + 1
                right_child = 2 * index + 2
                smallest = index

                if left_child < length and heap._data[left_child][0] < heap._data[smallest][0]:
                    smallest = left_child
                if right_child < length and heap._data[right_child][0] < heap._data[smallest][0]:
                    smallest = right_child

                if smallest != index:
                    heap._data[index], heap._data[smallest] = (
                        heap._data[smallest],
                        heap._data[index],
                    )
                    index = smallest
                else:
                    break

        return heap

    def drain(self):
        """Pops and drains all items from the heap in sorted priority order.

        Returns:
            A list of all (priority, item) pairs sorted from smallest to largest.
        """
        result = []
        while not self.is_empty():
            result.append(self.pop())
        return result

    def to_list(self):
        """Copies current internal heap array representation.

        Returns:
            A shallow copy list of internal data pairs.
        """
        return self._data[:]

    def is_valid_heap(self):
        """Verifies if min-heap structural rules are preserved throughout.

        Returns:
            True if valid, False if parent priority exceeds child priority.
        """
        length = len(self._data)
        for i in range(length):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < length and self._data[i][0] > self._data[left][0]:
                return False
            if right < length and self._data[i][0] > self._data[right][0]:
                return False
        return True

    def is_empty(self):
        """Checks if the heap has no items.

        Returns:
            True if empty, False otherwise.
        """
        return len(self._data) == 0

    def __len__(self):
        """Returns the total number of items stored in the heap."""
        return len(self._data)