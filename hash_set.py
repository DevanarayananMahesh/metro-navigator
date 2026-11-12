from hash_table import HashTable


class HashSet:
    """A set implementation storing unique string elements backed by a HashTable.

    Attributes:
        _map: The internal HashTable storing items as keys.
    """

    def __init__(self):
        """Initializes an empty hash set."""
        self._map = HashTable()

    def add(self, item):
        """Adds an item to the set if not already present.

        Args:
            item: String item to add.

        Returns:
            True if item was new, False if it was already in the set.

        Raises:
            TypeError: If item is not a string.
        """
        if type(item) is not str:
            raise TypeError
        if self._map.contains(item):
            return False
        self._map.put(item, True)
        return True

    def remove(self, item):
        """Removes an item from the set.

        Args:
            item: String item to remove.

        Raises:
            TypeError: If item is not a string.
            KeyError: If item is not in the set.
        """
        if type(item) is not str:
            raise TypeError

        if not self._map.contains(item):
            raise KeyError

        self._map.remove(item)

    def discard(self, item):
        """Removes an item from the set if present without raising an error.

        Args:
            item: String item to discard.

        Returns:
            True if item was present and removed, False otherwise.

        Raises:
            TypeError: If item is not a string.
        """
        if type(item) is not str:
            raise TypeError

        if self._map.contains(item):
            self._map.remove(item)
            return True

        return False

    def contains(self, item):
        """Checks if an item exists in the set.

        Args:
            item: String item to look for.

        Returns:
            True if found, False otherwise.

        Raises:
            TypeError: If item is not a string.
        """
        if type(item) is not str:
            raise TypeError

        return self._map.contains(item)

    def __contains__(self, item):
        """Enables 'in' membership testing."""
        return self.contains(item)

    def union(self, other):
        """Creates a new set with items present in either set.

        Args:
            other: Another HashSet instance.

        Returns:
            A new HashSet containing combined elements.

        Raises:
            TypeError: If other is not a HashSet.
        """
        if not isinstance(other, HashSet):
            raise TypeError

        result = HashSet()

        for item in self.to_list():
            result.add(item)

        for item in other.to_list():
            result.add(item)

        return result

    def intersection(self, other):
        """Creates a new set with items present in both sets.

        Args:
            other: Another HashSet instance.

        Returns:
            A new HashSet containing overlapping elements.

        Raises:
            TypeError: If other is not a HashSet.
        """
        if not isinstance(other, HashSet):
            raise TypeError

        result = HashSet()

        for item in self.to_list():
            if item in other:
                result.add(item)

        return result

    def difference(self, other):
        """Creates a new set with items in this set but not in the other.

        Args:
            other: Another HashSet instance.

        Returns:
            A new HashSet containing unique elements of this set.

        Raises:
            TypeError: If other is not a HashSet.
        """
        if not isinstance(other, HashSet):
            raise TypeError

        result = HashSet()

        for item in self.to_list():
            if item not in other:
                result.add(item)

        return result

    def symmetric_difference(self, other):
        """Creates a new set with items in exactly one of the sets.

        Args:
            other: Another HashSet instance.

        Returns:
            A new HashSet containing non-overlapping elements.

        Raises:
            TypeError: If other is not a HashSet.
        """
        if not isinstance(other, HashSet):
            raise TypeError

        result = HashSet()

        for item in self.to_list():
            if item not in other:
                result.add(item)

        for item in other.to_list():
            if item not in self:
                result.add(item)

        return result

    def is_subset(self, other):
        """Checks if every item in this set exists in the other set.

        Args:
            other: Another HashSet instance.

        Returns:
            True if this set is a subset of other, False otherwise.

        Raises:
            TypeError: If other is not a HashSet.
        """
        if not isinstance(other, HashSet):
            raise TypeError

        if len(self) > len(other):
            return False

        for item in self.to_list():
            if item not in other:
                return False

        return True

    def is_empty(self):
        """Checks if the set contains no elements.

        Returns:
            True if empty, False otherwise.
        """
        return len(self._map) == 0

    def clear(self):
        """Removes all elements from the set."""
        self._map = HashTable()

    def __len__(self):
        """Returns the number of items stored in the set."""
        return len(self._map)

    def to_list(self):
        """Returns a list of all stored items.

        Returns:
            A list containing all set elements.
        """
        return self._map.keys()