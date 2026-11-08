class MinHeap:
    def __init__(self):
        self._data = []

    def push(self, priority, item):
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
        if len(self._data) == 0:
            raise IndexError
        return self._data[0]

    @staticmethod
    def build_heap(pairs):
        """Static method returning a NEW heap built bottom-up."""
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
        result = []
        while not self.is_empty():
            result.append(self.pop())
        return result

    def to_list(self):
        return self._data[:]

    def is_valid_heap(self):
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
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)