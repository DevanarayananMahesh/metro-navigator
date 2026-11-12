from linked_list import LinkedList


class Queue:
    """A FIFO queue built on a custom LinkedList."""

    def __init__(self):
        # Must store storage ONLY in self._list
        self._list = LinkedList()

    def enqueue(self, item):
        """Add item to the back of the queue (tail of LinkedList) in O(1) time."""
        self._list.append(item)

    def dequeue(self):
        """Remove and return front item (head of LinkedList). Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._list.remove_at(0)

    def peek(self):
        """Return front item without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek on empty queue")
        return self._list.get(0)

    def is_empty(self):
        """Return True if queue contains no elements."""
        return len(self._list) == 0

    def clear(self):
        """Remove all items from the queue."""
        self._list.clear()

    def to_list(self):
        """Return a new Python list of items, front to back."""
        return self._list.to_list()

    def __len__(self):
        """Return the number of items stored in the queue."""
        return len(self._list)


def hot_potato(names, num):
    """
    Simulates Hot Potato game returning (eliminated_list, winner).
    - Rotates the potato 'num - 1' times.
    - Dequeues the eliminated person at the front.
    """
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("num must be an integer.")
    if num < 1:
        raise ValueError("num must be at least 1.")
    if not names:
        raise ValueError("names list cannot be empty.")

    q = Queue()
    for name in names:
        q.enqueue(name)

    eliminated = []

    while len(q) > 1:
        for _ in range(num - 1):
            q.enqueue(q.dequeue())
        
        eliminated.append(q.dequeue())

    winner = q.dequeue()
    return (eliminated, winner)


def board_passengers(names, seats_available):
    if not isinstance(seats_available, int) or isinstance(seats_available, bool):
        raise TypeError("seats_available must be an integer.")
    if seats_available < 0:
        raise ValueError("seats_available cannot be negative.")

    q = Queue()
    for name in names:
        q.enqueue(name)

    boarded = []
    seats_left = seats_available

    while seats_left > 0 and not q.is_empty():
        boarded.append(q.dequeue())
        seats_left -= 1

    return (boarded, q.to_list())