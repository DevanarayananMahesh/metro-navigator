from linked_list import LinkedList


class Queue:
    """A FIFO queue implementation built on top of a LinkedList.

    Attributes:
        _list: The internal LinkedList storing queue elements.
    """

    def __init__(self):
        """Initializes an empty queue."""
        self._list = LinkedList()

    def enqueue(self, item):
        """Adds an item to the back of the queue.

        Args:
            item: The element to add.
        """
        self._list.append(item)

    def dequeue(self):
        """Removes and returns the front item of the queue.

        Returns:
            The front element.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._list.remove_at(0)

    def peek(self):
        """Looks at the front item without removing it.

        Returns:
            The front element.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek on empty queue")
        return self._list.get(0)

    def is_empty(self):
        """Checks if the queue has no elements.

        Returns:
            True if empty, False otherwise.
        """
        return len(self._list) == 0

    def clear(self):
        """Removes all items from the queue."""
        self._list.clear()

    def to_list(self):
        """Converts queue elements into a standard list from front to back.

        Returns:
            A list of elements.
        """
        return self._list.to_list()

    def __len__(self):
        """Returns the total number of items stored in the queue."""
        return len(self._list)


def hot_potato(names, num):
    """Simulates the Hot Potato elimination game using a Queue.

    Args:
        names: List of player names.
        num: Number of passes per elimination round.

    Returns:
        A tuple of (eliminated_players_list, winner_name).

    Raises:
        TypeError: If num is not an integer.
        ValueError: If num is less than 1 or names list is empty.
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
    """Boards waiting passengers onto a transport line up to available seat capacity.

    Args:
        names: List of passenger names in queue order.
        seats_available: Total number of open seats.

    Returns:
        A tuple of (boarded_passengers_list, remaining_queue_list).

    Raises:
        TypeError: If seats_available is not an integer.
        ValueError: If seats_available is negative.
    """
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